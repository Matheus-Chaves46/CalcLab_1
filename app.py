"""
Aplicação principal do CalcLab.
"""

from typing import Dict, Any, Optional
from flask import Flask, render_template, request, jsonify, Response, redirect, url_for, flash, session
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

# Configuração do banco de dados
DATABASE = 'calclab.db'

# Adicione estas constantes no início do arquivo, após as importações
ADMIN_USERNAME = "matheus"
ADMIN_PASSWORD = "123456"  # Em produção, use uma senha mais segura

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
        
        # Criar tabela de usuários
        db.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_usuario TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL,
                email TEXT NOT NULL,
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
            flash('Por favor, faça login para acessar esta página.', 'error')
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
    return render_template('index.html')

@app.route('/matematica', methods=['GET', 'POST'])
def matematica() -> Response:
    """Página de cálculos matemáticos.
    
    Returns:
        Response: Resposta HTTP com o resultado do cálculo ou página HTML.
        
    Raises:
        BadRequest: Se os dados da requisição são inválidos.
        NotFound: Se o cálculo solicitado não existe.
    """
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not data:
                raise BadRequest('Dados da requisição inválidos')
                
            tipo_calculo = data.get('tipo_calculo')
            if not tipo_calculo:
                raise BadRequest('Tipo de cálculo não especificado')
            
            resultado = None
            
            # Encontra o cálculo nas categorias
            calc_info = None
            for categoria in config.CALCULATORS['matematica']['categories'].values():
                if tipo_calculo in categoria['calculations']:
                    calc_info = categoria['calculations'][tipo_calculo]
                    break
            
            if not calc_info:
                raise NotFound('Cálculo não encontrado')
            
            # Coleta os valores das variáveis
            variaveis = {}
            for var in calc_info['variables']:
                if var in data:
                    variaveis[var] = float(data[var])
            
            # Chama a função apropriada baseada no tipo de cálculo
            if tipo_calculo == 'funcao_quadratica':
                resultado = calc_mat.produtos_notaveis(**variaveis)
                
            elif tipo_calculo == 'formula_delta':
                resultado = calc_mat.formula_delta(**variaveis)
                
            elif tipo_calculo == "formula_bhaskara":
                resultado = calc_mat.formula_bhaskara(**variaveis)
                
            elif tipo_calculo == "funcao_1_grau":
                resultado = calc_mat.funcao_1_grau(**variaveis)

            elif tipo_calculo == "funcao_2_grau":
                resultado = calc_mat.funcao_2_grau(**variaveis)

            elif tipo_calculo == "vertice_parabolica":
                resultado = calc_mat.vertice_parabolica(**variaveis)

            elif tipo_calculo == "funcao_exponencial":
                resultado = calc_mat.funcao_exponencial(**variaveis)

            elif tipo_calculo == "funcao_logaritmica":
                resultado = calc_mat.funcao_logaritmica(**variaveis)

            elif tipo_calculo == "pa_termo_geral":
                resultado = calc_mat.pa_termo_geral(**variaveis)

            elif tipo_calculo == "pa_soma_termos":
                resultado = calc_mat.pa_soma_termos(**variaveis)

            elif tipo_calculo == "pg_termo_geral":
                resultado = calc_mat.pg_termo_geral(**variaveis)

            elif tipo_calculo == "pg_soma_termos_finitos":
                resultado = calc_mat.pg_soma_termos_finitos(**variaveis)

            elif tipo_calculo == "pg_soma_infinita":
                resultado = calc_mat.pg_soma_infinita(**variaveis)

            elif tipo_calculo == "trigonometria_relacoes_fundamentais":
                resultado = calc_mat.trigonometria_relacoes_fundamentais(**variaveis)

            elif tipo_calculo == "lei_senos":
                resultado = calc_mat.lei_senos(**variaveis)

            elif tipo_calculo == "lei_cossenos":
                resultado = calc_mat.lei_cossenos(**variaveis)

            elif tipo_calculo == "area_triangulo":
                resultado = calc_mat.area_triangulo(**variaveis)

            elif tipo_calculo == "area_circulo":
                resultado = calc_mat.area_circulo(**variaveis)

            elif tipo_calculo == "volume_cubo":
                resultado = calc_mat.volume_cubo(**variaveis)

            elif tipo_calculo == "volume_esfera":
                resultado = calc_mat.volume_esfera(**variaveis)

            elif tipo_calculo == "volume_cilindro":
                resultado = calc_mat.volume_cilindro(**variaveis)

            elif tipo_calculo == "fatorial":
                resultado = calc_mat.fatorial(**variaveis)

            elif tipo_calculo == "permutacao_simples":
                resultado = calc_mat.permutacao_simples(**variaveis)

            elif tipo_calculo == "combinacao_simples":
                resultado = calc_mat.combinacao_simples(**variaveis)

            elif tipo_calculo == "probabilidade":
                resultado = calc_mat.probabilidade(**variaveis)

            elif tipo_calculo == "determinante_matriz":
                resultado = calc_mat.determinante_matriz(**variaveis)

            elif tipo_calculo == "multiplicacao_matriz":
                resultado = calc_mat.multiplicacao_matriz(**variaveis)

            elif tipo_calculo == "limite":
                resultado = calc_mat.limite(**variaveis)

            elif tipo_calculo == "derivada_funcao_potencia":
                resultado = calc_mat.derivada_funcao_potencia(**variaveis)

            
            return jsonify({'resultado': resultado})
            
        except ValueError as e:
            return jsonify({'erro': str(e)}), 400
        except Exception as e:
            return jsonify({'erro': f'Erro inesperado: {str(e)}'}), 500
            
    return render_template('matematica.html')

@app.route('/fisica', methods=['GET', 'POST'])
def fisica() -> Response:
    """Página de cálculos físicos.
    
    Returns:
        Response: Resposta HTTP com o resultado do cálculo ou página HTML.
        
    Raises:
        BadRequest: Se os dados da requisição são inválidos.
        NotFound: Se o cálculo solicitado não existe.
    """
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not data:
                raise BadRequest('Dados da requisição inválidos')
                
            tipo_calculo = data.get('tipo_calculo')
            if not tipo_calculo:
                raise BadRequest('Tipo de cálculo não especificado')
            
            resultado = None
            
            # Encontra o cálculo nas categorias
            calc_info = None
            for categoria in config.CALCULATORS['fisica']['categories'].values():
                if tipo_calculo in categoria['calculations']:
                    calc_info = categoria['calculations'][tipo_calculo]
                    break
            
            if not calc_info:
                raise NotFound('Cálculo não encontrado')
            
            # Coleta os valores das variáveis
            variaveis = {}
            for var in calc_info['variables']:
                if var in data:
                    variaveis[var] = float(data[var])
            
            # Chama a função apropriada baseada no tipo de cálculo
            if tipo_calculo == "velocidade_media":
                resultado = calc_fis.velocidade_media(**variaveis)

            elif tipo_calculo == "movimento_uniforme":
                resultado = calc_fis.movimento_uniforme(**variaveis)

            elif tipo_calculo == "movimento_uniformemente_variado":
                resultado = calc_fis.movimento_uniformemente_variado(**variaveis)

            elif tipo_calculo == "equacao_torricelli":
                resultado = calc_fis.equacao_torricelli(**variaveis)

            elif tipo_calculo == "principio_fundamental_dinamica":
                resultado = calc_fis.principio_fundamental_dinamica(**variaveis)

            elif tipo_calculo == "forca_peso":
                resultado = calc_fis.forca_peso(**variaveis)

            elif tipo_calculo == "forca_atrito":
                resultado = calc_fis.forca_atrito(**variaveis)

            elif tipo_calculo == "trabalho_forca_constante":
                resultado = calc_fis.trabalho_forca_constante(**variaveis)

            elif tipo_calculo == "energia_cinetica":
                resultado = calc_fis.energia_cinetica(**variaveis)

            elif tipo_calculo == "energia_potencial":
                resultado = calc_fis.energia_potencial(**variaveis)

            elif tipo_calculo == "potencia_media":
                resultado = calc_fis.potencia_media(**variaveis)

            elif tipo_calculo == "pressao":
                resultado = calc_fis.pressao(**variaveis)

            elif tipo_calculo == "pressao_hidrostatica":
                resultado = calc_fis.pressao_hidrostatica(**variaveis)

            elif tipo_calculo == "empuxo":
                resultado = calc_fis.empuxo(**variaveis)

            elif tipo_calculo == "dilatacao_linear":
                resultado = calc_fis.dilatacao_linear(**variaveis)

            elif tipo_calculo == "equacao_fundamental_calorimetria":
                resultado = calc_fis.equacao_fundamental_calorimetria(**variaveis)

            elif tipo_calculo == "primeira_lei_termodinamica":
                resultado = calc_fis.primeira_lei_termodinamica(**variaveis)

            elif tipo_calculo == "equacao_dos_espelhos_e_lentes":
                resultado = calc_fis.equacao_dos_espelhos_e_lentes(**variaveis)

            elif tipo_calculo == "formula_do_aumento_da_imagem":
                resultado = calc_fis.formula_do_aumento_da_imagem(**variaveis)

            elif tipo_calculo == "velocidade_onda":
                resultado = calc_fis.velocidade_onda(**variaveis)

            elif tipo_calculo == "lei_ohm":
                resultado = calc_fis.lei_ohm(**variaveis)

            elif tipo_calculo == "potencia_eletrica":
                resultado = calc_fis.potencia_eletrica(**variaveis)

            elif tipo_calculo == "forca_entre_cargas_eletricas":
                resultado = calc_fis.forca_entre_cargas_eletricas(**variaveis)

            
            return jsonify({'resultado': resultado})
            
        except ValueError as e:
            return jsonify({'erro': str(e)}), 400
        except Exception as e:
            return jsonify({'erro': f'Erro inesperado: {str(e)}'}), 500
            
    return render_template('fisica.html')

@app.route('/quimica', methods=['GET', 'POST'])
def quimica() -> Response:
    """Página de cálculos químicos.
    
    Returns:
        Response: Resposta HTTP com o resultado do cálculo ou página HTML.
        
    Raises:
        BadRequest: Se os dados da requisição são inválidos.
        NotFound: Se o cálculo solicitado não existe.
    """
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not data:
                raise BadRequest('Dados da requisição inválidos')
                
            tipo_calculo = data.get('tipo_calculo')
            if not tipo_calculo:
                raise BadRequest('Tipo de cálculo não especificado')
            
            resultado = None
            
            # Encontra o cálculo nas categorias
            calc_info = None
            for categoria in config.CALCULATORS['quimica']['categories'].values():
                if tipo_calculo in categoria['calculations']:
                    calc_info = categoria['calculations'][tipo_calculo]
                    break
            
            if not calc_info:
                raise NotFound('Cálculo não encontrado')
            
            # Coleta os valores das variáveis
            variaveis = {}
            for var in calc_info['variables']:
                if var in data:
                    variaveis[var] = float(data[var])
            
            # Chama a função apropriada baseada no tipo de cálculo
            if tipo_calculo == "pureza":
                resultado = calc_qui.pureza(**variaveis)

            elif tipo_calculo == "gases":
                resultado = calc_qui.gases(**variaveis)

            elif tipo_calculo == "balanceamento":
                resultado = calc_qui.balanceamento(**variaveis)

            elif tipo_calculo == "excesso":
                resultado = calc_qui.excesso(**variaveis)

            elif tipo_calculo == "massa_reagentes_produtos":
                resultado = calc_qui.massa_reagentes_produtos(**variaveis)

            elif tipo_calculo == "quantidade_reagente_necessario":
                resultado = calc_qui.quantidade_reagente_necessario(**variaveis)

            elif tipo_calculo == "tabela_periodica":
                resultado = calc_qui.tabela_periodica(**variaveis)

            elif tipo_calculo == "pilha_daniels":
                resultado = calc_qui.pilha_daniels(**variaveis)

            elif tipo_calculo == "termoquimica":
                resultado = calc_qui.termoquimica(**variaveis)

            elif tipo_calculo == "equilibrio_ionico":
                resultado = calc_qui.equilibrio_ionico(**variaveis)

            
            return jsonify({'resultado': resultado})
            
        except ValueError as e:
            return jsonify({'erro': str(e)}), 400
        except Exception as e:
            return jsonify({'erro': f'Erro inesperado: {str(e)}'}), 500
            
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
        
        # Verifica se o nome de usuário já existe
        nome_usuario = request.form.get('nome_usuario')
        if db.execute('SELECT id FROM usuarios WHERE nome_usuario = ?', (nome_usuario,)).fetchone():
            db.close()
            flash('Este nome de usuário já está em uso.', 'error')
            return redirect(url_for('criar_conta'))
        
        # Cria novo usuário
        db.execute(
            'INSERT INTO usuarios (nome_usuario, senha, email) VALUES (?, ?, ?)',
            (nome_usuario, generate_password_hash(request.form.get('senha')), request.form.get('email'))
        )
        db.commit()
        db.close()
        
        flash('Conta criada com sucesso! Faça login para continuar.', 'success')
        return redirect(url_for('login'))
    
    return render_template('criar_conta.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome_usuario = request.form.get('nome_usuario')
        senha = request.form.get('senha')
        
        db = get_db()
        user = db.execute('SELECT * FROM usuarios WHERE nome_usuario = ?', (nome_usuario,)).fetchone()
        db.close()
        
        if user and check_password_hash(user['senha'], senha):
            session['user_id'] = user['id']
            session['nome_usuario'] = user['nome_usuario']
            flash('Bem-vindo(a), ' + user['nome_usuario'] + '!', 'success')
            return redirect(url_for('index'))
        
        flash('Nome de usuário ou senha inválidos.', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('nome_usuario', None)
    flash('Você foi desconectado com sucesso.', 'success')
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
        usuarios = db.execute('SELECT id, nome_usuario, email, created_at FROM usuarios').fetchall()
        db.close()
        
        # Converte os timestamps para o formato brasileiro
        usuarios_formatados = []
        for usuario in usuarios:
            usuario_dict = dict(usuario)
            if usuario_dict['created_at']:
                try:
                    # Converte o timestamp do SQLite para datetime
                    dt = datetime.strptime(usuario_dict['created_at'], '%Y-%m-%d %H:%M:%S')
                    # Ajusta para o fuso horário do Brasil (UTC-3)
                    dt = dt - timedelta(hours=3)
                    # Formata a data
                    usuario_dict['created_at'] = dt.strftime('%d/%m/%Y %H:%M:%S')
                except:
                    # Se houver erro na conversão, mantém o valor original
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

# Inicializa o banco de dados quando a aplicação inicia
init_db()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)