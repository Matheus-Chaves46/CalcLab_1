"""
Aplicação principal do CalcLab.
"""

from typing import Dict, Any, Optional
from flask import Flask, render_template, request, jsonify, Response, redirect, url_for, flash
from datetime import datetime
from werkzeug.exceptions import NotFound, BadRequest
import config
import calc_matematica as calc_mat
import calc_fisica as calc_fis
import calc_quimica as calc_qui
import json
import os
from werkzeug.security import generate_password_hash
import logging
from pymongo import MongoClient
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(config)
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))

# Configuração do MongoDB
try:
    # Tenta obter a URL do MongoDB das variáveis de ambiente
    mongo_url = os.environ.get('MONGODB_URI')
    if not mongo_url:
        # Se não estiver definida, usa uma URL local para desenvolvimento
        mongo_url = "mongodb://localhost:27017/"
    
    client = MongoClient(mongo_url)
    db = client.calclab  # Nome do banco de dados
    usuarios_collection = db.usuarios  # Nome da coleção
    logger.info("Conexão com MongoDB estabelecida com sucesso")
except Exception as e:
    logger.error(f"Erro ao conectar com MongoDB: {str(e)}")
    raise

# Função para carregar usuários do MongoDB
def carregar_usuarios():
    try:
        usuarios = list(usuarios_collection.find({}, {'_id': 0}))
        return {"usuarios": usuarios}
    except Exception as e:
        logger.error(f"Erro ao carregar usuários: {str(e)}")
        return {"usuarios": []}

# Função para salvar usuário no MongoDB
def salvar_usuario(usuario):
    try:
        usuarios_collection.insert_one(usuario)
    except Exception as e:
        logger.error(f"Erro ao salvar usuário: {str(e)}")
        raise

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

@app.route('/criar-conta', methods=['GET', 'POST'])
def criar_conta():
    try:
        if request.method == 'POST':
            # Verifica se o nome de usuário já existe
            nome_usuario = request.form.get('nome_usuario')
            if usuarios_collection.find_one({'nome_usuario': nome_usuario}):
                flash('Este nome de usuário já está em uso.', 'error')
                return redirect(url_for('criar_conta'))
            
            # Cria novo usuário
            novo_usuario = {
                'nome_completo': request.form.get('nome_completo'),
                'nome_usuario': nome_usuario,
                'email': request.form.get('email'),
                'senha': generate_password_hash(request.form.get('senha')),
                'data_nascimento': request.form.get('data_nascimento'),
                'serie': request.form.get('serie'),
                'materia_dificuldade': request.form.get('materia_dificuldade')
            }
            
            salvar_usuario(novo_usuario)
            flash('Conta criada com sucesso! Faça login para continuar.', 'success')
            return redirect(url_for('index'))
        
        return render_template('criar_conta.html')
    except Exception as e:
        logger.error(f"Erro na rota criar_conta: {str(e)}")
        flash('Ocorreu um erro ao processar sua solicitação. Por favor, tente novamente.', 'error')
        return redirect(url_for('index'))

@app.route('/verificar-usuario', methods=['POST'])
def verificar_usuario():
    try:
        data = request.get_json()
        nome_usuario = data.get('username')
        
        if usuarios_collection.find_one({'nome_usuario': nome_usuario}):
            return jsonify({'exists': True})
        
        return jsonify({'exists': False})
    except Exception as e:
        logger.error(f"Erro na rota verificar_usuario: {str(e)}")
        return jsonify({'error': 'Erro ao verificar usuário'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)