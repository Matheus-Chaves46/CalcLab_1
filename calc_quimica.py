"""
Módulo de cálculos químicos.
"""

from typing import Dict, List, Union
import math
import os
import sys
import re  
from collections import Counter
from sympy import Matrix, lcm
from collections import defaultdict
from collections import defaultdict
from typing import Dict, List, Union, Optional, Tuple

def calculate_quimica(tipo_calculo: str, **kwargs) -> Tuple[Dict[str, float], Dict[str, str]]:
    """
    Função principal para calcular resultados de química.
    
    Args:
        tipo_calculo (str): Tipo de cálculo a ser realizado
        **kwargs: Valores necessários para o cálculo
        
    Returns:
        Tuple[Dict[str, float], Dict[str, str]]: Resultado do cálculo e suas unidades
    """
    # Mapeamento de tipos de cálculo para suas respectivas funções
    calculos = {
        'pureza': pureza,
        'rendimento': rendimento,
        'excesso': excesso,
        'quantidade_de_reagentes_necessario': quantidade_de_reagentes_necessario,
        'balanceamento': balanceamento,
        'gases': gases,
        'tabela_periodica': tabela_periodica,
        'pilha_de_daniels': pilha_de_daniels,
        'termoquimica': termoquimica,
        'equilibrio_ionico': equilibrio_ionico
    }
    # Verifica se o tipo de cálculo existe
    if tipo_calculo not in calculos:
        raise ValueError(f"Tipo de cálculo '{tipo_calculo}' não encontrado.")
    
    # Converte os valores de string para float
    valores = {}
    for chave, valor in kwargs.items():
        if valor is not None and valor != '':
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
    
def pureza(
    pureza: Optional[float] = None,
    massa_da_substancia_pura: Optional[float] = None,
    massa_da_substancia_amostra: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'pureza':pureza, 'massa_da_substancia_pura':massa_da_substancia_pura, 'massa_da_substancia_amostra':massa_da_substancia_amostra}
        none_count = sum(1 for v in valores.values() if v is None)
        if none_count != 1:
                raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
        if pureza is None:
            if pureza == 0:
                raise ValueError("Tempo não pode ser zero para calcular a velocidade média.")
            pureza = (massa_da_substancia_pura / massa_da_substancia_amostra) * 100
            return {'pureza': pureza}, {'pureza': '%'}
        elif massa_da_substancia_pura is None:
            massa_da_substancia_pura = (pureza / massa_da_substancia_amostra) * 100
            return {'massa_da_substancia_pura': massa_da_substancia_pura}, {'massa_da_substancia_pura': 'g'}
        else: 
            if massa_da_substancia_amostra == 0:
                    raise ValueError("Velocidade média não pode ser zero para calcular o tempo.")
            massa_da_substancia_amostra = (pureza / 100) * massa_da_substancia_pura
            return {'massa_da_substancia_amostra': massa_da_substancia_amostra}, {'massa_da_substancia_amostra': 'g'}
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Pureza: {str(e)}")
    
def rendimento(
    rendimento: Optional[float] = None,
    rendimento_real: Optional[float] = None,
    rendimento_teorico: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'rendimento': rendimento, 'rendimento_real': rendimento_real, 'rendimento_teorico': rendimento_teorico}
        none_count = sum(1 for v in valores.values() if v is None)
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no Rendimento: {str(e)}")
    
def excesso(
    equacao_reagentes: Optional[str] = None,
    equacao_produtos: Optional[str] = None,
    massa_disponivel: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'equacao_reagentes': equacao_reagentes, 'equacao_produtos': equacao_produtos, 'massa_disponivel': massa_disponivel}
        none_count = sum(1 for v in valores.values() if v is None)
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no Excesso: {str(e)}")
    
def quantidade_de_reagentes_necessario(
    equacao_reagentes: Optional[str] = None,
    equacao_produtos: Optional[str] = None,
    massa_dos_produtos_desejada: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'equacao_reagentes': equacao_reagentes, 'equacao_produtos': equacao_produtos, 'massa_dos_produtos_desejada': massa_dos_produtos_desejada}
        none_count = sum(1 for v in valores.values() if v is None)
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Quantidade de Reagentes Necessário: {str(e)}")
    
def balanceamento(
    equacao_reagentes: Optional[str] = None,
    equacao_produtos: Optional[str] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'equacao_reagentes': equacao_reagentes, 'equacao_produtos': equacao_produtos}
        none_count = sum(1 for v in valores.values() if v is None)
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no Balanceamento: {str(e)}")
    
def gases(
    pressao: Optional[float] = None,
    volume: Optional[float] = None,
    numero_de_mols: Optional[float] = None,
    temperatura: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'pressao': pressao, 'volume': volume, 'numero_de_mols': numero_de_mols, 'temperatura': temperatura}
        none_count = sum(1 for v in valores.values() if v is None)
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro nos Gases: {str(e)}")
    
def tabela_periodica(
    elemento: Optional[str] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'elemento': elemento}
        none_count = sum(1 for v in valores.values() if v is None)
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Tabela Periódica: {str(e)}")
    
def pilha_de_daniels(
    equacao_reagentes: Optional[str] = None,
    equacao_produtos: Optional[str] = None,
    concentracao_dos_reagentes: Optional[float] = None,
    concentracao_dos_produtos: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'equacao_reagentes': equacao_reagentes, 'equacao_produtos': equacao_produtos, 'concentracao_dos_produtos':concentracao_dos_produtos, 'concentracao_dos_reagentes': concentracao_dos_reagentes}
        none_count = sum(1 for v in valores.values() if v is None)
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Pilha de Daniels: {str(e)}")
    
def termoquimica(
    delta_h: Optional[float] = None,
    entalpia_dos_reagentes: Optional[float] = None,
    entalpia_dos_produtos: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'delta_h': delta_h, 'entalpia_dos_produtos': entalpia_dos_produtos, 'entalpia_dos_reagentes': entalpia_dos_reagentes}
        none_count = sum(1 for v in valores.values() if v is None)
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Termoquímica: {str(e)}")
    
def equilibrio_ionico(
    acido_ou_base: Optional[float] = None,
    constante_de_equilibrio: Optional[float] = None,
    concentracao_incial: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'acido_ou_base': acido_ou_base, 'constante_de_equilibrio': constante_de_equilibrio, 'concentracao_incial': concentracao_incial}
        none_count = sum(1 for v in valores.values() if v is None)
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no Equilíbrio Iônico: {str(e)}")
    