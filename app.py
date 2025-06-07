"""
Aplicação principal do CalcLab.
"""

from typing import Dict, Any, Optional
from flask import Flask, render_template, request, jsonify, Response, redirect, url_for, flash, session
from datetime import datetime
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

def get_db():
    """Conecta ao banco de dados SQLite"""
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    """Inicializa o banco de dados criando a tabela de usuários se não existir"""
    if not os.path.exists(DATABASE):
        db = get_db()
        with app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))
        db.commit()
        db.close()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Por favor, faça login para acessar esta página.', 'error')
            return redirect(url_for('login'))
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

# Inicializa o banco de dados quando a aplicação inicia
init_db()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)