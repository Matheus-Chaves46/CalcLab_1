"""
Módulo de cálculos matemáticos.
"""

import math
import numpy as np
from typing import List, Dict, Union, Tuple, Optional

def funcao_quadratica(a: float, b: float, c: float, x: float) -> float:
    """Calcula o valor da função quadrática f(x) = ax² + bx + c.
    
    Args:
        a (float): Coeficiente do termo quadrático
        b (float): Coeficiente do termo linear
        c (float): Termo constante
        x (float): Valor de x
        
    Returns:
        float: Valor da função no ponto x
    """
    try:
        return float(a * x**2 + b * x + c)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular função quadrática: {str(e)}")

def equacao_linear(a: float, b: float, x: float) -> float:
    """Resolve a equação linear ax + b = 0.
    
    Args:
        a (float): Coeficiente de x
        b (float): Termo constante
        x (float): Valor de x
        
    Returns:
        float: Solução da equação
        
    Raises:
        ValueError: Se a = 0 (equação impossível)
    """
    if a == 0:
        raise ValueError("Coeficiente 'a' não pode ser zero")
    try:
        return float(-b / a)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao resolver equação linear: {str(e)}")

def sistema_linear(a1: float, b1: float, c1: float, a2: float, b2: float, c2: float) -> Dict[str, float]:
    """Resolve um sistema de duas equações lineares.
    
    Args:
        a1 (float): Coeficiente de x na primeira equação
        b1 (float): Coeficiente de y na primeira equação
        c1 (float): Termo constante na primeira equação
        a2 (float): Coeficiente de x na segunda equação
        b2 (float): Coeficiente de y na segunda equação
        c2 (float): Termo constante na segunda equação
        
    Returns:
        Dict[str, float]: Dicionário com as soluções x e y
        
    Raises:
        ValueError: Se o sistema é indeterminado ou impossível
    """
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
    """Calcula o n-ésimo termo da PA.
    
    Args:
        a1 (float): Primeiro termo
        r (float): Razão
        n (int): Posição do termo
        
    Returns:
        float: N-ésimo termo da PA
        
    Raises:
        ValueError: Se n é menor que 1
    """
    if n < 1:
        raise ValueError("A posição do termo deve ser maior ou igual a 1")
    try:
        return float(a1 + (n - 1) * r)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular termo da PA: {str(e)}")

def progressao_geometrica(a1: float, q: float, n: int) -> float:
    """Calcula o n-ésimo termo da PG.
    
    Args:
        a1 (float): Primeiro termo
        q (float): Razão
        n (int): Posição do termo
        
    Returns:
        float: N-ésimo termo da PG
        
    Raises:
        ValueError: Se n é menor que 1
    """
    if n < 1:
        raise ValueError("A posição do termo deve ser maior ou igual a 1")
    try:
        return float(a1 * q**(n - 1))
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular termo da PG: {str(e)}")

def area(tipo: str, **kwargs) -> float:
    """Calcula a área de diferentes figuras geométricas.
    
    Args:
        tipo (str): Tipo da figura ('quadrado', 'retangulo', 'triangulo', 'circulo')
        **kwargs: Parâmetros específicos para cada tipo de figura
        
    Returns:
        float: Área da figura
        
    Raises:
        ValueError: Se o tipo não é suportado ou se faltam parâmetros
    """
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
    """Calcula o volume de diferentes sólidos geométricos.
    
    Args:
        tipo (str): Tipo do sólido ('cubo', 'paralelepipedo', 'esfera', 'cilindro')
        **kwargs: Parâmetros específicos para cada tipo de sólido
        
    Returns:
        float: Volume do sólido
        
    Raises:
        ValueError: Se o tipo não é suportado ou se faltam parâmetros
    """
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
    """Calcula o perímetro de diferentes figuras planas.
    
    Args:
        tipo (str): Tipo da figura ('quadrado', 'retangulo', 'triangulo', 'circulo')
        **kwargs: Parâmetros específicos para cada tipo de figura
        
    Returns:
        float: Perímetro da figura
        
    Raises:
        ValueError: Se o tipo não é suportado ou se faltam parâmetros
    """
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
    """Calcula o lado desconhecido de um triângulo retângulo.
    
    Args:
        a (Optional[float]): Cateto a
        b (Optional[float]): Cateto b
        c (Optional[float]): Hipotenusa
        
    Returns:
        float: Valor do lado desconhecido
        
    Raises:
        ValueError: Se mais de um lado é None ou se nenhum lado é None
    """
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
    """Calcula funções trigonométricas.
    
    Args:
        angulo (float): Ângulo em graus
        hipotenusa (Optional[float]): Valor da hipotenusa
        cateto_oposto (Optional[float]): Valor do cateto oposto
        cateto_adjacente (Optional[float]): Valor do cateto adjacente
        
    Returns:
        float: Valor da função trigonométrica (seno, cosseno ou tangente)
        
    Raises:
        ValueError: Se a combinação de lados não é válida
    """
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
    """Calcula a média aritmética.
    
    Args:
        valores (List[float]): Lista de valores
        
    Returns:
        float: Média aritmética dos valores
        
    Raises:
        ValueError: Se a lista está vazia
    """
    try:
        if not valores:
            raise ValueError("Lista de valores não pode estar vazia")
        return float(sum(valores) / len(valores))
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular média: {str(e)}")

def mediana(valores: List[float]) -> float:
    """Calcula a mediana.
    
    Args:
        valores (List[float]): Lista de valores
        
    Returns:
        float: Mediana dos valores
        
    Raises:
        ValueError: Se a lista está vazia
    """
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
    """Calcula a moda.
    
    Args:
        valores (List[float]): Lista de valores
        
    Returns:
        float: Moda dos valores
        
    Raises:
        ValueError: Se a lista está vazia
    """
    try:
        if not valores:
            raise ValueError("Lista de valores não pode estar vazia")
        from collections import Counter
        contador = Counter(valores)
        return float(max(contador.items(), key=lambda x: x[1])[0])
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular moda: {str(e)}")

def desvio_padrao(valores: List[float]) -> float:
    """Calcula o desvio padrão.
    
    Args:
        valores (List[float]): Lista de valores
        
    Returns:
        float: Desvio padrão dos valores
        
    Raises:
        ValueError: Se a lista está vazia
    """
    try:
        if not valores:
            raise ValueError("Lista de valores não pode estar vazia")
        return float(np.std(valores))
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular desvio padrão: {str(e)}")
