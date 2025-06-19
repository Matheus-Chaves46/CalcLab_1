"""
Módulo de cálculos matemáticos.
"""

import math
import numpy as np
from typing import List, Dict, Union, Tuple, Optional

def calculate_matematica(tipo_calculo: str, **kwargs) -> Tuple[Dict[str, float], Dict[str, str]]:
    """
    Função principal para calcular resultados de matemática.
    
    Args:
        tipo_calculo (str): Tipo de cálculo a ser realizado
        **kwargs: Valores necessários para o cálculo
        
    Returns:
        Tuple[Dict[str, float], Dict[str, str]]: Resultado do cálculo e suas unidades
    """
    # Mapeamento de tipos de cálculo para suas respectivas funções
    calculos = {
        'produtos_notaveis': produtos_notaveis,
        'formula_do_delta': formula_do_delta,
        'funcao_do_1_grau': funcao_do_1_grau,
        'funcao_do_2_grau': funcao_do_2_grau,
        'vertice_de_parabola': vertice_de_parabola,
        'funcao_exponencial': funcao_exponencial,
        'funcao_logaritmica': funcao_logaritmica,
        'pa_termo_geral': pa_termo_geral,
        'pa_soma_dos_termos': pa_soma_dos_termos,
        'pg_termo_geral': pg_termo_geral,  
        'pg_soma_dos_termos_finitos': pg_soma_dos_termos_finitos,
        'pg_soma_infinita': pg_soma_infinita,
        'relacoes_fundamentais': relacoes_fundamentais,
        'lei_dos_senos': lei_dos_senos,
        'lei_dos_cossenos': lei_dos_cossenos,
        'area_do_triangulo': area_do_triangulo,
        'area_do_circulo': area_do_circulo,
        'volume_do_cubo': volume_do_cubo,
        'volume_da_esfera': volume_da_esfera,
        'volume_do_cilindro': volume_do_cilindro, 
        'fatorial': fatorial,
        'permutacao_simples': permutacao_simples,
        'combinacao_simples': combinacao_simples,
        'probabilidade': probabilidade,
        'determinante_da_matriz': determinante_da_matriz, 
        'multiplicacao_de_matriz': multiplicacao_de_matriz,
        'limite': limite,
        'derivada_de_funcao_potencia': derivada_de_funcao_potencia
    }
    # Verifica se o tipo de cálculo existe
    if tipo_calculo not in calculos:
        raise ValueError(f"Tipo de cálculo '{tipo_calculo}' não encontrado.")
    
    # Lista de campos que devem permanecer como texto
    campos_texto = ['equacao_reagentes', 'equacao_produtos', 'composto_quimico', 'elemento']
    
    # Converte os valores de string para float apenas se não forem campos de texto
    valores = {}
    for chave, valor in kwargs.items():
        if valor is not None and valor != '':
            if chave in campos_texto:
                valores[chave] = valor
            else:
                try:
                    valores[chave] = float(valor)
                except ValueError:
                    raise ValueError(f"Valor inválido para {chave}: {valor}")
    
    # Executa o cálculo
    try:
        resultado, unidades = calculos[tipo_calculo](**valores)
        if not isinstance(resultado, dict) or not isinstance(unidades, dict):
            raise ValueError('Função de cálculo deve retornar dois dicionários.')
        return resultado, unidades
    except Exception as e:
        raise ValueError(f"Erro ao executar cálculo: {str(e)}")
    
def produtos_notaveis( #! REVISAR COMO FAZER OS TIPOS DE PRODUTOS NOTÁVEIS
    a: Optional[float] = None,
    b: Optional[float] = None,
    c: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro nos Produtos Notáveis : {str(e)}")
from typing import Optional, Tuple, Dict

def formula_do_delta(
    delta: Optional[float] = None,
    b: Optional[float] = None,
    a: Optional[float] = None,
    c: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na formula_do_delta: {str(e)}")

def formula_de_bhaskara(
    x: Optional[float] = None,
    b: Optional[float] = None,
    delta: Optional[float] = None,
    a: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na funcao_do_1_grau: {str(e)}")
    
def funcao_do_1_grau(
    fx: Optional[float] = None,
    ax: Optional[float] = None,
    b: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na funcao_do_1_grau: {str(e)}")


def funcao_do_2_grau(
    fx: Optional[float] = None,
    ax2: Optional[float] = None,
    bx: Optional[float] = None,
    c: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na funcao_do_2_grau: {str(e)}")


def vertice_de_parabola(
    vertice_da_parabola: Optional[float] = None,
    b: Optional[float] = None,
    a: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na vertice_parabola: {str(e)}")


def funcao_exponencial(
    fx: Optional[float] = None,
    a: Optional[float] = None,
    b: Optional[float] = None,
    x: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na funcao_exponencial: {str(e)}")


def funcao_logaritmica(
    fx: Optional[float] = None,
    b: Optional[float] = None,
    x: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na funcao_logaritmica: {str(e)}")


def pa_termo_geral(
    termo_geral: Optional[float] = None,
    primeiro_termo: Optional[float] = None,
    termo_em_sequencia: Optional[float] = None,
    razao_da_pa: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na pa_termo_geral: {str(e)}")


def pa_soma_dos_termos(
    soma_dos_termos: Optional[float] = None,
    termos_somados: Optional[float] = None,
    primeiro_termo: Optional[float] = None,
    ultimo_termo: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na pa_soma_termos: {str(e)}")


def pg_termo_geral(
    termo_geral: Optional[float] = None,
    primeiro_termo: Optional[float] = None,
    razao_da_pg: Optional[float] = None,
    termo_em_sequencia: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na pg_termo_geral: {str(e)}")


def pg_soma_dos_termos_finitos(
    soma_dos_termos: Optional[float] = None,
    primeiro_termo: Optional[float] = None,
    razao_da_pg: Optional[float] = None,
    termos_somados: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na pg_soma_termos_finitos: {str(e)}")


def pg_soma_infinita(
    soma_infinita: Optional[float] = None,
    primeiro_termo: Optional[float] = None,
    razao_da_pg: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na pg_soma_infinita: {str(e)}")


def relacoes_fundamentais( #! REVISAR VARIÁVEIS 
    a: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na relacoes_fundamentais: {str(e)}")


def lei_dos_senos(
    a: Optional[float] = None,
    a_: Optional[float] = None,
    b: Optional[float] = None,
    b_: Optional[float] = None,
    c: Optional[float] = None,
    c_: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na lei_dos_senos: {str(e)}")


def lei_dos_cossenos(
    a: Optional[float] = None,
    a_: Optional[float] = None,
    b: Optional[float] = None,
    c: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na lei_dos_cossenos: {str(e)}")


def area_do_triangulo(
    area_do_triangulo: Optional[float] = None,
    base: Optional[float] = None,
    altura: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na area_do_triangulo: {str(e)}")


def area_do_circulo(
    area_do_circulo: Optional[float] = None,
    raio: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na area_do_circulo: {str(e)}")


def volume_do_cubo(
    volume_do_cubo: Optional[float] = None,
    aresta: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na volume_do_cubo: {str(e)}")


def volume_da_esfera(
    volume_da_esfera: Optional[float] = None,
    raio: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na volume_da_esfera: {str(e)}")


def volume_do_cilindro(
    volume_do_cilindro: Optional[float] = None,
    raio: Optional[float] = None,
    altura: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na volume_do_cilindro: {str(e)}")


def fatorial( #! REVISAR VARIÁVEIS
    n_fatorial: Optional[float] = None,
    n: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na fatorial: {str(e)}")


def permutacao_simples(
    pn: Optional[float] = None,
    n_fatorial: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na permutacao_simples: {str(e)}")


def combinacao_simples( #! REVISAR VARIÁVEIS
    a: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na combinacao_simples: {str(e)}")


def probabilidade(
    probabilidade: Optional[float] = None,
    casos_favoraveis: Optional[float] = None,
    casos_possiveis: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na probabilidade: {str(e)}")


def determinante_da_matriz( # ! VERIFICAR VARIÁVEIS
    a: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na determinante_da_matriz: {str(e)}")


def multiplicacao_de_matriz( # ! VERIFICAR VARIÁVEIS
    a: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na multiplicacao_de_matriz: {str(e)}")


def limite(
    limite_fx: Optional[float] = None,
    l: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na limite: {str(e)}")


def derivada_de_funcao_potencia(
    f_x: Optional[float] = None,
    n: Optional[float] = None,
    x: Optional[float] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        ...
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na derivada_de_funcao_potencia: {str(e)}")

