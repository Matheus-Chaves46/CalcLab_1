"""
Módulo de cálculos matemáticos.
"""

import math
import numpy as np
from typing import List, Dict, Union, Tuple, Optional

def funcao_quadratica(a: float, b: float, c: float, x: float) -> float:
    try:
        return float(a * x**2 + b * x + c)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular função quadrática: {str(e)}")

def equacao_linear(a: float, b: float, x: float) -> float:
    if a == 0:
        raise ValueError("Coeficiente 'a' não pode ser zero")
    try:
        return float(-b / a)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao resolver equação linear: {str(e)}")

def sistema_linear(a1: float, b1: float, c1: float, a2: float, b2: float, c2: float) -> Dict[str, float]:
    try:
        det = float(a1 * b2 - a2 * b1)
        if det == 0:
            raise ValueError("Sistema indeterminado ou impossível")
        x = float((c1 * b2 - c2 * b1) / det)
        y = float((a1 * c2 - a2 * c1) / det)
        return {'x': x, 'y': y}
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao resolver sistema linear: {str(e)}")

def progressao_aritmetica(a1: float, r: float, n: int) -> float:
    if n < 1:
        raise ValueError("A posição do termo deve ser maior ou igual a 1")
    try:
        return float(a1 + (n - 1) * r)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular termo da PA: {str(e)}")

def progressao_geometrica(a1: float, q: float, n: int) -> float:
    if n < 1:
        raise ValueError("A posição do termo deve ser maior ou igual a 1")
    try:
        return float(a1 * q**(n - 1))
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular termo da PG: {str(e)}")

def area(tipo: str, **kwargs) -> float:
    try:
        if tipo == 'quadrado':
            if 'lado' not in kwargs:
                raise ValueError("Parâmetro 'lado' é obrigatório para quadrado")
            return float(kwargs['lado'] ** 2)
        elif tipo == 'retangulo':
            if 'base' not in kwargs or 'altura' not in kwargs:
                raise ValueError("Parâmetros 'base' e 'altura' são obrigatórios para retângulo")
            return float(kwargs['base'] * kwargs['altura'])
        elif tipo == 'triangulo':
            if 'base' not in kwargs or 'altura' not in kwargs:
                raise ValueError("Parâmetros 'base' e 'altura' são obrigatórios para triângulo")
            return float((kwargs['base'] * kwargs['altura']) / 2)
        elif tipo == 'circulo':
            if 'raio' not in kwargs:
                raise ValueError("Parâmetro 'raio' é obrigatório para círculo")
            return float(math.pi * kwargs['raio'] ** 2)
        else:
            raise ValueError(f"Tipo de figura '{tipo}' não suportado")
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular área: {str(e)}")

def volume(tipo: str, **kwargs) -> float:
    try:
        if tipo == 'cubo':
            if 'lado' not in kwargs:
                raise ValueError("Parâmetro 'lado' é obrigatório para cubo")
            return float(kwargs['lado'] ** 3)
        elif tipo == 'paralelepipedo':
            if not all(k in kwargs for k in ['base', 'altura', 'profundidade']):
                raise ValueError("Parâmetros 'base', 'altura' e 'profundidade' são obrigatórios para paralelepípedo")
            return float(kwargs['base'] * kwargs['altura'] * kwargs['profundidade'])
        elif tipo == 'esfera':
            if 'raio' not in kwargs:
                raise ValueError("Parâmetro 'raio' é obrigatório para esfera")
            return float((4/3) * math.pi * kwargs['raio'] ** 3)
        elif tipo == 'cilindro':
            if 'raio' not in kwargs or 'altura' not in kwargs:
                raise ValueError("Parâmetros 'raio' e 'altura' são obrigatórios para cilindro")
            return float(math.pi * kwargs['raio'] ** 2 * kwargs['altura'])
        else:
            raise ValueError(f"Tipo de sólido '{tipo}' não suportado")
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular volume: {str(e)}")

def perimetro(tipo: str, **kwargs) -> float:
    try:
        if tipo == 'quadrado':
            if 'lado' not in kwargs:
                raise ValueError("Parâmetro 'lado' é obrigatório para quadrado")
            return float(4 * kwargs['lado'])
        elif tipo == 'retangulo':
            if 'base' not in kwargs or 'altura' not in kwargs:
                raise ValueError("Parâmetros 'base' e 'altura' são obrigatórios para retângulo")
            return float(2 * (kwargs['base'] + kwargs['altura']))
        elif tipo == 'triangulo':
            if not all(k in kwargs for k in ['lado1', 'lado2', 'lado3']):
                raise ValueError("Parâmetros 'lado1', 'lado2' e 'lado3' são obrigatórios para triângulo")
            return float(kwargs['lado1'] + kwargs['lado2'] + kwargs['lado3'])
        elif tipo == 'circulo':
            if 'raio' not in kwargs:
                raise ValueError("Parâmetro 'raio' é obrigatório para círculo")
            return float(2 * math.pi * kwargs['raio'])
        else:
            raise ValueError(f"Tipo de figura '{tipo}' não suportado")
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular perímetro: {str(e)}")

def teorema_pitagoras(a: Optional[float], b: Optional[float], c: Optional[float]) -> float:
    try:
        none_count = sum(1 for x in [a, b, c] if x is None)
        if none_count != 1:
            raise ValueError("Exatamente um lado deve ser None para ser calculado")
            
        if c is None and a is not None and b is not None:
            return float(math.sqrt(a**2 + b**2))
        elif a is None and b is not None and c is not None:
            if c <= b:
                raise ValueError("Hipotenusa deve ser maior que o cateto")
            return float(math.sqrt(c**2 - b**2))
        elif b is None and a is not None and c is not None:
            if c <= a:
                raise ValueError("Hipotenusa deve ser maior que o cateto")
            return float(math.sqrt(c**2 - a**2))
        else:
            raise ValueError("Combinação inválida de lados")
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao aplicar teorema de Pitágoras: {str(e)}")

def trigonometria(angulo: float, hipotenusa: Optional[float] = None, 
                cateto_oposto: Optional[float] = None, 
                cateto_adjacente: Optional[float] = None) -> float:
    try:
        angulo_rad = float(math.radians(angulo))
        
        if hipotenusa is not None and cateto_oposto is not None:
            if hipotenusa <= cateto_oposto:
                raise ValueError("Hipotenusa deve ser maior que o cateto oposto")
            return float(math.sin(angulo_rad))
        elif hipotenusa is not None and cateto_adjacente is not None:
            if hipotenusa <= cateto_adjacente:
                raise ValueError("Hipotenusa deve ser maior que o cateto adjacente")
            return float(math.cos(angulo_rad))
        elif cateto_oposto is not None and cateto_adjacente is not None:
            return float(math.tan(angulo_rad))
        else:
            raise ValueError("Combinação de lados não válida")
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular função trigonométrica: {str(e)}")

def media(valores: List[float]) -> float:
    try:
        if not valores:
            raise ValueError("Lista de valores não pode estar vazia")
        return float(sum(valores) / len(valores))
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular média: {str(e)}")

def mediana(valores: List[float]) -> float:
    try:
        if not valores:
            raise ValueError("Lista de valores não pode estar vazia")
        valores_ordenados = sorted(valores)
        n = len(valores_ordenados)
        if n % 2 == 0:
            return float((valores_ordenados[n//2 - 1] + valores_ordenados[n//2]) / 2)
        else:
            return float(valores_ordenados[n//2])
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular mediana: {str(e)}")

def moda(valores: List[float]) -> float:
    try:
        if not valores:
            raise ValueError("Lista de valores não pode estar vazia")
        from collections import Counter
        contador = Counter(valores)
        return float(max(contador.items(), key=lambda x: x[1])[0])
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular moda: {str(e)}")

def desvio_padrao(valores: List[float]) -> float:
    try:
        if not valores:
            raise ValueError("Lista de valores não pode estar vazia")
        return float(np.std(valores))
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular desvio padrão: {str(e)}")

def quadrado_soma(a: float, b: float) -> float:
    try:
        return float(a**2 + 2*a*b + b**2)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular quadrado da soma: {str(e)}")

def quadrado_diferenca(a: float, b: float) -> float:
    try:
        return float(a**2 - 2*a*b + b**2)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular quadrado da diferença: {str(e)}")

def diferenca_quadrados(a: float, b: float) -> float:
    try:
        return float((a + b) * (a - b))
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular diferença dos quadrados: {str(e)}")
