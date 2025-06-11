"""
Módulo de cálculos químicos.
"""

from typing import Dict, List, Union
import math

def massa_molar(formula: str) -> float:
    # Tabela de massas atômicas (simplificada)
    massas_atomicas = {
        'H': 1.008,
        'He': 4.003,
        'Li': 6.941,
        'Be': 9.012,
        'B': 10.811,
        'C': 12.011,
        'N': 14.007,
        'O': 15.999,
        'F': 18.998,
        'Ne': 20.180,
        'Na': 22.990,
        'Mg': 24.305,
        'Al': 26.982,
        'Si': 28.086,
        'P': 30.974,
        'S': 32.065,
        'Cl': 35.453,
        'K': 39.098,
        'Ca': 40.078,
        'Fe': 55.845,
        'Cu': 63.546,
        'Zn': 65.380,
        'Br': 79.904,
        'Ag': 107.868,
        'I': 126.904,
        'Au': 196.967
    }
    
    massa_total = 0
    elemento_atual = ''
    numero_atual = ''
    
    for char in formula:
        if char.isupper():
            if elemento_atual:
                numero = int(numero_atual) if numero_atual else 1
                massa_total += massas_atomicas[elemento_atual] * numero
            elemento_atual = char
            numero_atual = ''
        elif char.islower():
            elemento_atual += char
        elif char.isdigit():
            numero_atual += char
    
    if elemento_atual:
        numero = int(numero_atual) if numero_atual else 1
        massa_total += massas_atomicas[elemento_atual] * numero
    
    return massa_total

def concentracao_molar(mols: float, volume: float) -> float:
    return mols / volume

def ph(concentracao_h: float) -> float:
    return -math.log10(concentracao_h)

def poh(concentracao_oh: float) -> float:
    return -math.log10(concentracao_oh)

def constante_equilibrio(produtos: Dict[str, float], reagentes: Dict[str, float]) -> float:
    numerador = 1
    denominador = 1
    
    for produto, concentracao in produtos.items():
        numerador *= concentracao
    
    for reagente, concentracao in reagentes.items():
        denominador *= concentracao
    
    return numerador / denominador

def energia_livre_gibbs(entalpia: float, entropia: float, temperatura: float) -> float:
    return entalpia - (temperatura * entropia / 1000)

def lei_henry(pressao: float, constante_henry: float) -> float:
    return pressao * constante_henry

def razao_molar(mols_reagente: float, mols_produto: float) -> float:
    return mols_produto / mols_reagente

def rendimento_teorico(mols_obtidos: float, mols_esperados: float) -> float:
    return (mols_obtidos / mols_esperados) * 100

def pressao_osmotica(concentracao: float, temperatura: float) -> float:
    R = 0.082  # Constante dos gases em L·atm/(mol·K)
    return concentracao * R * temperatura
