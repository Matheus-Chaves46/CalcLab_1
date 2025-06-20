""" 
Aplicação principal do CalcLab.
"""

from typing import Dict, Any, Optional
from flask import Flask, render_template, request, jsonify, Response, redirect, url_for, flash, session, send_file
from datetime import datetime, timedelta
from werkzeug.exceptions import NotFound, BadRequest
import config
import calc_matematica as calc_mat
import calc_fisica as calc_fis
import calc_quimica as calc_qui
import json
import os
from werkzeug.security import generate_password_hash, check_password_hash
import logging
from pymongo import MongoClient
from dotenv import load_dotenv
from functools import wraps
from bson.objectid import ObjectId
import sqlite3
import pytz
import shutil
from chatbot_logic import chatbot

# Carrega variáveis de ambiente
load_dotenv()

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(config)
app.secret_key = os.getenv('SECRET_KEY', 'sua_chave_secreta_aqui')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # Session lasts 7 days
print(f"DEBUG: Flask SECRET_KEY in app.py: {app.secret_key}")

# Configuração do banco de dados
DATABASE = 'calclab.db'

# Adicione estas constantes no início do arquivo, após as importações
ADMIN_USERNAME = "matheus"
ADMIN_PASSWORD = "123456"  # Em produção, use uma senha mais segura

print('Banco de dados será criado em:', os.path.abspath(DATABASE))

def get_db():
    """Conecta ao banco de dados SQLite"""
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def get_brazil_time():
    """Retorna o horário atual do Brasil (UTC-3)"""
    return (datetime.utcnow() - timedelta(hours=3)).strftime('%d/%m/%Y %H:%M:%S')

def init_db():
    """Inicializa o banco de dados criando a tabela de usuários se não existir"""
    try:
        db = get_db()
        
        # Criar tabela de usuários com todos os campos
        db.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_usuario TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL,
                email TEXT NOT NULL,
                nome_completo TEXT,
                data_nascimento TEXT,
                serie TEXT,
                materia_dificuldade TEXT,
                is_admin INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Criar tabela de admins
        db.execute('''
            CREATE TABLE IF NOT EXISTS admins (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        
        # Verificar se já existe um admin
        admin = db.execute('SELECT * FROM admins WHERE username = ?', ('admin',)).fetchone()
        if not admin:
            # Inserir admin padrão
            db.execute('INSERT INTO admins (username, password) VALUES (?, ?)', ('admin', 'admin123'))
            logger.info("Admin padrão criado com sucesso")
        
        db.commit()
        db.close()
        logger.info("Banco de dados inicializado com sucesso")
    except Exception as e:
        logger.error(f"Erro ao inicializar banco de dados: {str(e)}")
        raise

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('is_admin'):
            flash('Acesso restrito. Faça login como administrador.', 'error')
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

@app.context_processor
def inject_now() -> Dict[str, datetime]:
    """Adiciona a data atual ao contexto de todos os templates.
    
    Returns:
        Dict[str, datetime]: Dicionário com a data atual.
    """
    return {'now': datetime.utcnow()}

# Rotas principais
@app.route('/')
def index() -> str:
    """Página inicial.
    
    Returns:
        str: HTML renderizado da página inicial.
    """
    print("DEBUG: Session contents:", dict(session))  # Debug print
    return render_template('index.html')

@app.route('/matematica', methods=['GET', 'POST'])
# @login_required # Temporariamente desativado para edição
def matematica():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Requisição inválida: dados JSON não encontrados'}), 400

        tipo_calculo = data.get('tipo_calculo')
        valores = {k: v for k, v in data.items() if k != 'tipo_calculo'}
        
        try:
            resultado, unidades = calc_mat.calculate_matematica(tipo_calculo, **valores)
            resultado_formatado = {
                k: f"{v} {unidades.get(k, '')}" for k, v in resultado.items()
            }
            return jsonify({'resultado': resultado_formatado})
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            logger.exception("Erro inesperado no cálculo de matemática")
            return jsonify({'error': 'Ocorreu um erro inesperado ao calcular.'}), 500
    return render_template('matematica.html')

@app.route('/fisica', methods=['GET', 'POST'])
# @login_required # Temporariamente desativado para edição
def fisica():
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'Dados não fornecidos'}), 400

            tipo_calculo = data.get('tipo_calculo')
            if not tipo_calculo:
                return jsonify({'error': 'Tipo de cálculo não especificado'}), 400

            # Remove o tipo_calculo dos dados para passar para a função de cálculo
            valores = {k: v for k, v in data.items() if k != 'tipo_calculo'}

            # Converte os valores para float
            valores = {k: float(v) if v is not None and v != '' else None for k, v in valores.items()}

            # Chama a função de cálculo apropriada
            resultado, unidades = calc_fis.calculate_fisica(tipo_calculo, **valores)

            # Formata o resultado com as unidades
            resultado_formatado = {}
            for variavel, valor in resultado.items():
                unidade = unidades.get(variavel, '')
                resultado_formatado[variavel] = f"{valor:.5f} {unidade}".strip()

            return jsonify({'resultado': resultado_formatado})

        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': f'Erro ao processar cálculo: {str(e)}'}), 500

    return render_template('fisica.html')

@app.route('/quimica', methods=['GET', 'POST'])
# @login_required # Temporariamente desativado para edição
def quimica():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Requisição inválida: dados JSON não encontrados'}), 400

        tipo_calculo = data.get('tipo_calculo')
        valores = {k: v for k, v in data.items() if k != 'tipo_calculo'}
        
        try:
            resultado, unidades = calc_qui.calculate_quimica(tipo_calculo, **valores)
            
            # Formatação simplificada dos resultados
            resultado_formatado = ""
            for variavel, valor in resultado.items():
                unidade = unidades.get(variavel, '')
                # Simplifica o nome da variável
                nome_variavel = variavel.split(' da ')[-1].split(' do ')[-1].split(' de ')[-1]
                # Formata números com 1 casa decimal se for float
                if isinstance(valor, float):
                    valor_formatado = f"{valor:.1f}"
                else:
                    valor_formatado = str(valor)
                # Adiciona a unidade apenas se ela existir
                if unidade:
                    resultado_formatado += f"{nome_variavel}: {valor_formatado}{unidade}\n"
                else:
                    resultado_formatado += f"{nome_variavel}: {valor_formatado}\n"
            
            # Retorna o texto formatado dentro de um JSON válido
            return jsonify({'resultado': resultado_formatado.strip()})
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            logger.exception("Erro inesperado no cálculo de química")
            return jsonify({'error': 'Ocorreu um erro inesperado ao calcular.'}), 500
    return render_template('quimica.html')

@app.route('/contato')
def contato() -> str:
    """Página de contato.
    
    Returns:
        str: HTML renderizado da página de contato.
    """
    return render_template('contato.html')

@app.route('/criar_conta', methods=['GET', 'POST'])
def criar_conta():
    if request.method == 'POST':
        db = get_db()
        nome_usuario = request.form.get('nome_usuario')
        if db.execute('SELECT id FROM usuarios WHERE nome_usuario = ?', (nome_usuario,)).fetchone():
            db.close()
            flash('Este nome de usuário já está em uso.', 'error')
            return redirect(url_for('criar_conta'))
        # Coletar todos os campos do formulário
        nome_completo = request.form.get('nome_completo')
        email = request.form.get('email')
        senha = generate_password_hash(request.form.get('senha'))
        data_nascimento = request.form.get('data_nascimento')
        serie = request.form.get('serie')
        materia_dificuldade = request.form.get('materia_dificuldade')
        # Inserir no banco
        db.execute(
            'INSERT INTO usuarios (nome_usuario, senha, email, nome_completo, data_nascimento, serie, materia_dificuldade) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (nome_usuario, senha, email, nome_completo, data_nascimento, serie, materia_dificuldade)
        )
        db.commit()
        db.close()
        flash('Conta criada com sucesso! Faça login para continuar.', 'success')
        return redirect(url_for('login'))
    return render_template('criar_conta.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_input = request.form.get('username')
        password_input = request.form.get('password')
        
        if not username_input or not password_input:
            flash('Por favor, preencha todos os campos.', 'error')
            return render_template('login.html')

        # Test account credentials
        if username_input == 'teste' and password_input == '123456':
            session['user_id'] = 999  # Special test user ID
            session['nome_usuario'] = 'teste'
            session['is_admin'] = True
            session.permanent = True  # Make session persistent
            flash('Bem-vindo! Login realizado com sucesso.', 'success')
            return redirect(url_for('index'))
        
        # Regular user login logic
        conn = get_db()
        user = conn.execute('SELECT * FROM usuarios WHERE nome_usuario = ?', (username_input,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user['senha'], password_input):
            session['user_id'] = user['id']
            session['nome_usuario'] = user['nome_usuario']
            session['is_admin'] = user['is_admin'] if 'is_admin' in user.keys() else False
            session.permanent = True  # Make session persistent
            flash('Bem-vindo! Login realizado com sucesso.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Usuário ou senha inválidos.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()  # Clear all session data
    flash('Logout realizado com sucesso.', 'success')
    return redirect(url_for('index'))

@app.route('/esqueceu-senha')
def esqueceu_senha():
    return render_template('esqueceu_senha.html')

@app.route('/minha_conta')
@login_required
def minha_conta():
    db = get_db()
    user = db.execute('SELECT * FROM usuarios WHERE id = ?', (session['user_id'],)).fetchone()
    db.close()
    
    if not user:
        session.pop('user_id', None)
        session.pop('nome_usuario', None)
        flash('Usuário não encontrado.', 'error')
        return redirect(url_for('login'))
    
    return render_template('minha_conta.html', usuario=dict(user))

@app.route('/editar_conta', methods=['GET', 'POST'])
@login_required
def editar_conta():
    db = get_db()
    user = db.execute('SELECT * FROM usuarios WHERE id = ?', (session['user_id'],)).fetchone()
    
    if not user:
        db.close()
        session.pop('user_id', None)
        session.pop('nome_usuario', None)
        flash('Usuário não encontrado.', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        nova_senha = request.form.get('nova_senha')
        
        if nova_senha:
            db.execute(
                'UPDATE usuarios SET email = ?, senha = ? WHERE id = ?',
                (email, generate_password_hash(nova_senha), session['user_id'])
            )
        else:
            db.execute(
                'UPDATE usuarios SET email = ? WHERE id = ?',
                (email, session['user_id'])
            )
        
        db.commit()
        db.close()
        flash('Dados atualizados com sucesso!', 'success')
        return redirect(url_for('minha_conta'))
    
    db.close()
    return render_template('editar_conta.html', usuario=dict(user))

@app.route('/verificar-usuario', methods=['POST'])
def verificar_usuario():
    try:
        data = request.get_json()
        nome_usuario = data.get('username')
        
        db = get_db()
        usuario = db.execute('SELECT id FROM usuarios WHERE nome_usuario = ?', (nome_usuario,)).fetchone()
        db.close()
        
        if usuario:
            return jsonify({'exists': True})
        
        return jsonify({'exists': False})
    except Exception as e:
        logger.error(f"Erro na rota verificar_usuario: {str(e)}")
        return jsonify({'error': 'Erro ao verificar usuário'}), 500

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        logger.info(f"Tentativa de login admin - Usuário: {username}")
        
        try:
            db = get_db()
            admin = db.execute('SELECT * FROM admins WHERE username = ?', (username,)).fetchone()
            db.close()
            
            if admin and admin['password'] == password:
                session['is_admin'] = True
                session['admin_username'] = username
                flash('Login administrativo realizado com sucesso!', 'success')
                logger.info(f"Login admin bem-sucedido para usuário: {username}")
                return redirect(url_for('admin_usuarios'))
            else:
                flash('Usuário ou senha incorretos.', 'error')
                logger.warning(f"Tentativa de login admin falhou - Usuário: {username}")
        except Exception as e:
            logger.error(f"Erro durante login admin: {str(e)}")
            flash('Erro ao tentar fazer login. Por favor, tente novamente.', 'error')
    
    return render_template('admin_login.html')

@app.route('/admin/usuarios')
@admin_required
def admin_usuarios():
    try:
        db = get_db()
        usuarios = db.execute('SELECT id, nome_usuario, email, created_at FROM usuarios').fetchall()
        db.close()
        return render_template('admin_usuarios.html', usuarios=usuarios)
    except Exception as e:
        logger.error(f"Erro ao listar usuários: {str(e)}")
        flash('Erro ao carregar lista de usuários.', 'error')
        return redirect(url_for('admin_login'))

@app.route('/admin/logout')
def admin_logout():
    session.pop('is_admin', None)
    session.pop('admin_username', None)
    flash('Logout realizado com sucesso.', 'success')
    return redirect(url_for('admin_login'))

@app.route('/admin-secret-123', methods=['GET', 'POST'])
def secret_admin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['is_admin'] = True
            return redirect(url_for('secret_admin_dashboard'))
        else:
            flash('Usuário ou senha incorretos', 'error')
    
    return render_template('secret_admin.html')

@app.route('/admin-secret-123/dashboard')
def secret_admin_dashboard():
    if not session.get('is_admin'):
        return redirect(url_for('secret_admin'))
    
    try:
        db = get_db()
        usuarios = db.execute('SELECT id, nome_usuario, email, nome_completo, data_nascimento, serie, materia_dificuldade, created_at FROM usuarios').fetchall()
        db.close()
        
        # Converte os timestamps para o formato brasileiro
        usuarios_formatados = []
        for usuario in usuarios:
            usuario_dict = dict(usuario)
            # Formatar data de nascimento se existir
            if usuario_dict.get('data_nascimento'):
                try:
                    dt_nasc = datetime.strptime(usuario_dict['data_nascimento'], '%Y-%m-%d')
                    usuario_dict['data_nascimento'] = dt_nasc.strftime('%d/%m/%Y')
                except:
                    pass
            # Formatar data de cadastro
            if usuario_dict['created_at']:
                try:
                    dt = datetime.strptime(usuario_dict['created_at'], '%Y-%m-%d %H:%M:%S')
                    dt = dt - timedelta(hours=3)
                    usuario_dict['created_at'] = dt.strftime('%d/%m/%Y %H:%M:%S')
                except:
                    pass
            usuarios_formatados.append(usuario_dict)
        
        return render_template('secret_admin_dashboard.html', usuarios=usuarios_formatados)
    except Exception as e:
        logger.error(f"Erro ao listar usuários: {str(e)}")
        flash('Erro ao carregar lista de usuários.', 'error')
        return redirect(url_for('secret_admin'))

@app.route('/admin-secret-123/logout')
def secret_admin_logout():
    session.pop('is_admin', None)
    return redirect(url_for('secret_admin'))

@app.route('/chatbot', methods=['POST'])
def chatbot_endpoint():
    """Endpoint para o chatbot"""
    # Verifica se o usuário está logado
    if not session.get('user_id'):
        return jsonify({'response': 'Por favor, faça login para usar o assistente.'}), 401
    
    try:
        data = request.get_json()
        message = data.get('message', '')
        user_id = session.get('user_id')
        user_name = session.get('nome_usuario')
        
        # Gera resposta
        response = chatbot.generate_response(message, user_name)
        
        # Salva conversa
        chatbot.save_conversation(user_id, message, response)
        
        return jsonify({'response': response})
    except Exception as e:
        logger.error(f"Erro no chatbot: {str(e)}")
        return jsonify({'response': 'Desculpe, ocorreu um erro. Tente novamente.'}), 500

def backup_database():
    """Faz backup do banco de dados"""
    try:
        if os.path.exists(DATABASE):
            backup_dir = 'backups'
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
            
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_file = os.path.join(backup_dir, f'calclab_{timestamp}.db')
            
            shutil.copy2(DATABASE, backup_file)
            logger.info(f"Backup criado: {backup_file}")
            
            # Mantém apenas os últimos 5 backups
            backups = sorted([f for f in os.listdir(backup_dir) if f.startswith('calclab_')])
            if len(backups) > 5:
                for old_backup in backups[:-5]:
                    os.remove(os.path.join(backup_dir, old_backup))
    except Exception as e:
        logger.error(f"Erro ao fazer backup: {str(e)}")

@app.before_request
def before_request():
    """Executado antes de cada requisição"""
    # Faz backup do banco de dados a cada 24 horas
    if not hasattr(app, 'last_backup'):
        app.last_backup = datetime.now()
    
    if (datetime.now() - app.last_backup) > timedelta(hours=24):
        backup_database()
        app.last_backup = datetime.now()

# Manipuladores de erro para retornar JSON para requisições de API
@app.errorhandler(400)
def bad_request_error(error):
    logger.exception("Erro de requisição inválida")
    if request.path.startswith(('/matematica', '/fisica', '/quimica', '/chatbot', '/verificar-usuario')):
        return jsonify(error="Requisição inválida. Verifique os dados enviados."), 400
    return render_template('400.html'), 400

@app.errorhandler(404)
def not_found_error(error):
    if request.path.startswith(('/matematica', '/fisica', '/quimica', '/chatbot', '/verificar-usuario')):
        return jsonify(error="Recurso não encontrado."), 404
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    logger.exception("Erro interno do servidor") # Loga a exceção completa
    if request.path.startswith(('/matematica', '/fisica', '/quimica', '/chatbot', '/verificar-usuario')):
        return jsonify(error="Ocorreu um erro interno no servidor."), 500
    return render_template('500.html'), 500

# Inicializa o banco de dados quando a aplicação inicia
init_db()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)