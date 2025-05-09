"""
Módulo de cálculos químicos.
"""

from typing import Dict, List, Union
import math

def massa_molar(formula: str) -> float:
    """
    Calcula a massa molar de uma substância.
    
    Args:
        formula: Fórmula molecular da substância
        
    Returns:
        Massa molar em g/mol
    """
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
    """
    Calcula a concentração molar de uma solução.
    
    Args:
        mols: Quantidade de matéria em mols
        volume: Volume da solução em litros
        
    Returns:
        Concentração molar em mol/L
    """
    return mols / volume

def ph(concentracao_h: float) -> float:
    """
    Calcula o pH de uma solução.
    
    Args:
        concentracao_h: Concentração de íons H+ em mol/L
        
    Returns:
        pH da solução
    """
    return -math.log10(concentracao_h)

def poh(concentracao_oh: float) -> float:
    """
    Calcula o pOH de uma solução.
    
    Args:
        concentracao_oh: Concentração de íons OH- em mol/L
        
    Returns:
        pOH da solução
    """
    return -math.log10(concentracao_oh)

def constante_equilibrio(produtos: Dict[str, float], reagentes: Dict[str, float]) -> float:
    """
    Calcula a constante de equilíbrio de uma reação.
    
    Args:
        produtos: Dicionário com as concentrações dos produtos
        reagentes: Dicionário com as concentrações dos reagentes
        
    Returns:
        Constante de equilíbrio
    """
    numerador = 1
    denominador = 1
    
    for produto, concentracao in produtos.items():
        numerador *= concentracao
    
    for reagente, concentracao in reagentes.items():
        denominador *= concentracao
    
    return numerador / denominador

def energia_livre_gibbs(entalpia: float, entropia: float, temperatura: float) -> float:
    """
    Calcula a energia livre de Gibbs.
    
    Args:
        entalpia: Variação de entalpia em kJ/mol
        entropia: Variação de entropia em J/(mol·K)
        temperatura: Temperatura em Kelvin
        
    Returns:
        Energia livre de Gibbs em kJ/mol
    """
    return entalpia - (temperatura * entropia / 1000)

def lei_henry(pressao: float, constante_henry: float) -> float:
    """
    Calcula a solubilidade de um gás em um líquido usando a Lei de Henry.
    
    Args:
        pressao: Pressão parcial do gás em atm
        constante_henry: Constante de Henry em mol/(L·atm)
        
    Returns:
        Solubilidade do gás em mol/L
    """
    return pressao * constante_henry

def razao_molar(mols_reagente: float, mols_produto: float) -> float:
    """
    Calcula a razão molar entre reagente e produto.
    
    Args:
        mols_reagente: Quantidade de matéria do reagente em mols
        mols_produto: Quantidade de matéria do produto em mols
        
    Returns:
        Razão molar (mols_produto/mols_reagente)
    """
    return mols_produto / mols_reagente

def rendimento_teorico(mols_obtidos: float, mols_esperados: float) -> float:
    """
    Calcula o rendimento teórico de uma reação.
    
    Args:
        mols_obtidos: Quantidade de matéria obtida em mols
        mols_esperados: Quantidade de matéria esperada em mols
        
    Returns:
        Rendimento teórico em porcentagem
    """
    return (mols_obtidos / mols_esperados) * 100

def pressao_osmotica(concentracao: float, temperatura: float) -> float:
    """
    Calcula a pressão osmótica de uma solução.
    
    Args:
        concentracao: Concentração molar em mol/L
        temperatura: Temperatura em Kelvin
        
    Returns:
        Pressão osmótica em atm
    """
    R = 0.082  # Constante dos gases em L·atm/(mol·K)
    return concentracao * R * temperatura
