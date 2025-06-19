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
from typing import Dict, List, Union, Optional, Tuple
from dicionario_quimica import tabela_periodica, tabela_massa, tabela_potenciais, entalpias_formacao

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
            return {'Pureza da Substância': pureza}, {'Pureza da Substância': '%'}
        elif massa_da_substancia_pura is None:
            massa_da_substancia_pura = (pureza / massa_da_substancia_amostra) * 100
            return {'Massa da Substância Pura': massa_da_substancia_pura}, {'Massa da Substância Pura': 'g'}
        else: 
            if massa_da_substancia_amostra == 0:
                    raise ValueError("Velocidade média não pode ser zero para calcular o tempo.")
            massa_da_substancia_amostra = (pureza / 100) * massa_da_substancia_pura
            return {'Massa da Substância Amostra': massa_da_substancia_amostra}, {'Massa da Substância Amostra': 'g'}
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
        if none_count != 1:
                raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
        if rendimento is None:
            if rendimento == 0:
                raise ValueError("Tempo não pode ser zero para calcular a velocidade média.")
            rendimento = (rendimento_real / rendimento_teorico) * 100
            return {'Rendimento da Reação': rendimento}, {'Rendimento da Reação': '%'}
        elif rendimento_real is None:
            rendimento_real = (rendimento / rendimento_teorico) * 100
            return {'Rendimento Real': rendimento_real}, {'Rendimento Real': 'g'}
        else: 
            if rendimento_teorico == 0:
                    raise ValueError("Velocidade média não pode ser zero para calcular o tempo.")
            rendimento_teorico = (rendimento / 100) * rendimento_real
            return {'Rendimento Teórico': rendimento_teorico}, {'Rendimento Teórico': 'g'}
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
        
        if none_count > 0:
            raise ValueError("Todos os valores devem ser fornecidos para calcular o excesso.")
        
        def obter_massa_molar(composto, tabela_massa):
            elementos = re.findall(r'([A-Z][a-z]*)(\d*)', composto)
            massa_molar = 0
            for elemento, quantidade in elementos:
                quantidade = int(quantidade) if quantidade else 1
                if elemento in tabela_massa:
                    massa_molar += tabela_massa[elemento] * quantidade
                else:
                    raise ValueError(f"O elemento '{elemento}' não foi encontrado na tabela periódica ou foi escrito incorretamente.")
            return massa_molar

        # Entrada de dados
        reagentes = [r.strip() for r in equacao_reagentes.split(',')]
        
        # Processar coeficientes estequiométricos
        reagentes_esteq = {}
        massas_disponiveis = {}
        
        for termo in reagentes:
            match = re.match(r'(\d*)([A-Za-z0-9]+)', termo)
            coef = int(match.group(1)) if match.group(1) else 1
            substancia = match.group(2)
            reagentes_esteq[substancia] = coef
            massas_disponiveis[substancia] = massa_disponivel
        
        # Converter massas em mols
        mols_disponiveis = {}
        for substancia in reagentes_esteq:
            massa_molar = obter_massa_molar(substancia, tabela_massa)
            mols_disponiveis[substancia] = massas_disponiveis[substancia] / massa_molar
        
        # Determinar o reagente limitante
        razoes = {r: mols_disponiveis[r] / reagentes_esteq[r] for r in reagentes_esteq}
        limitante = min(razoes, key=razoes.get)
        
        # Calcular excesso
        excesso = {}
        for r in reagentes_esteq:
            if r != limitante:
                mols_consumidos = mols_disponiveis[limitante] * (reagentes_esteq[r] / reagentes_esteq[limitante])
                mols_excesso = mols_disponiveis[r] - mols_consumidos
                excesso[r] = mols_excesso * obter_massa_molar(r, tabela_massa)
        
        # Preparar resultado
        resultado = {
            'Reagente Limitante': limitante,
            'Massa do Reagente Limitante': massas_disponiveis[limitante]
        }
        unidades = {
            'Reagente Limitante': '',
            'Massa do Reagente Limitante': 'g'
        }
        
        for r, e in excesso.items():
            resultado[f'Excesso de {r}'] = e
            unidades[f'Excesso de {r}'] = 'g'
        
        return resultado, unidades
         
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
        def decompor_formula_quimica(fml_quimica):
            elementos_quimicos = defaultdict(int)
            indice = 0
            while indice < len(fml_quimica):
                if fml_quimica[indice].isalpha():
                    elemento_atual = fml_quimica[indice]
                    if indice + 1 < len(fml_quimica) and fml_quimica[indice + 1].islower():
                        elemento_atual += fml_quimica[indice + 1]
                        indice += 1
                    indice += 1
                    quantidade_elemento = ""
                    while indice < len(fml_quimica) and fml_quimica[indice].isdigit():
                        quantidade_elemento += fml_quimica[indice]
                        indice += 1
                    quantidade_elemento = int(quantidade_elemento) if quantidade_elemento else 1
                    elementos_quimicos[elemento_atual] += quantidade_elemento
            return elementos_quimicos

        def calcular_massa_molar(composto_quimico):
            composicao = decompor_formula_quimica(composto_quimico)
            massa_total = 0
            for elemento, quantidade in composicao.items():
                if elemento in tabela_massa:
                    massa_total += tabela_massa[elemento] * quantidade
                else:
                    print(f"O elemento '{elemento}' não foi encontrado no dicionário de massas atômicas ou foi escrito incorretamente.")
                    return None
            return massa_total

        # Calcular as massas molares dos reagentes e produtos
        massas_molares_reagentes = {reagente: calcular_massa_molar(reagente) for reagente in equacao_reagentes}
        massas_molares_produtos = {produto: calcular_massa_molar(produto) for produto in equacao_produtos}

        # Exibir as massas molares calculadas
        for reagente_atual, massa_reagente in massas_molares_reagentes.items():
            if massa_reagente:
                print(f"{reagente_atual}: {massa_reagente:.2f} g/mol")
                
        for produto_atual, massa_produto in massas_molares_produtos.items():
            if massa_produto:
                print(f"{produto_atual}: {massa_produto:.2f} g/mol")

        # Entrada da massa desejada para cada produto
        massas_produtos_desejadas = {}
        for produto_atual in equacao_produtos:
            massa_dos_produtos_desejada = float(input(f"\nDigite a massa desejada do produto {produto_atual} (em gramas): "))
            massas_produtos_desejadas[produto_atual] = massa_dos_produtos_desejada

        # Calcular as proporções com base nas massas molares
        proporcoes_produtos = {
            produto: massas_produtos_desejadas[produto] / massas_molares_produtos[produto]
            for produto in equacao_produtos
        }

        # Assumir a maior proporção como base para a reação
        maior_proporcao = max(proporcoes_produtos.values())

        for reagente_atual, massa_reagente in massas_molares_reagentes.items():
            if massa_reagente:
                quantidade_reagente_necessaria = massa_reagente * maior_proporcao
                print(f"{reagente_atual}: {quantidade_reagente_necessaria:.2f} g")

    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Quantidade de Reagentes Necessário: {str(e)}")
        
def massa_dos_reagentes_ou_dos_produtos(
    composto_quimico: Optional[str] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'composto_quimico': composto_quimico}
        none_count = sum(1 for v in valores.values() if v is None)
        def calcular_massa_molar(composto, tabela_massa):
            elementos = re.findall(r'([A-Z][a-z]*)(\d*)', composto)
            massa_total = 0
            for elemento, quantidade in elementos:
                if elemento in tabela_massa:
                    massa_elemento = tabela_massa[elemento]
                    quantidade = int(quantidade) if quantidade else 1
                    massa_total += massa_elemento * quantidade
                else:
                    print(f"O elemento '{elemento}' não foi encontrado na tabela ou foi escrito incorretamente.")
            return massa_total

        def main():
                compostos = []
                while True:
                    if composto_quimico.lower() == 'sair':
                        break
                    compostos.append(composto_quimico)
                
                massa_total = 0
                for composto_quimico in compostos:
                    massa = calcular_massa_molar(composto_quimico, tabela_massa)
                    print(f"Massa molar de {composto_quimico}: {massa:.3f} g/mol")
                    massa_total += massa

                print(f"Massa molar total dos compostos: {massa_total:.3f} g/mol")

        if __name__ == "__main__":
                main()
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Massa dos Reagentes ou dos produtos: {str(e)}")
    
def balanceamento(equacao_reagentes: str, equacao_produtos: str) -> Tuple[Dict[str, str], Dict[str, str]]:
    """Balanceia uma equação química."""
    try:
        # Verifica se as entradas são válidas
        if not equacao_reagentes or not equacao_produtos:
            raise ValueError("Todas as equações devem ser fornecidas para o balanceamento.")

        # Importa as dependências necessárias
        from collections import defaultdict
        from sympy import Matrix, lcm

        # Função para processar uma fórmula química
        def parse_formula(formula):
            elements = defaultdict(int)
            i = 0
            while i < len(formula):
                if formula[i].isalpha():
                    element = formula[i]
                    if i + 1 < len(formula) and formula[i + 1].islower():
                        element += formula[i + 1]
                        i += 1
                    i += 1
                    qty = ""
                    while i < len(formula) and formula[i].isdigit():
                        qty += formula[i]
                        i += 1
                    qty = int(qty) if qty else 1
                    elements[element] += qty
            return elements

        # Função para balancear a equação
        def balance_chemical_equation(reactants, products):
            # Obtém todos os elementos únicos
            elements = set()
            for compound in reactants + products:
                elements.update(parse_formula(compound).keys())
            elements = sorted(elements)
            
            # Cria os vetores para cada composto
            compound_vectors = []
            for compound in reactants + products:
                compound_vector = [parse_formula(compound).get(element, 0) for element in elements]
                compound_vectors.append(compound_vector)
            
            # Cria as matrizes
            reactant_matrix = Matrix(compound_vectors[:len(reactants)]).transpose()
            product_matrix = Matrix(compound_vectors[len(reactants):]).transpose()
            
            # Resolve o sistema
            coeff_matrix = reactant_matrix.row_join(-product_matrix)
            solution = coeff_matrix.nullspace()[0]
            
            # Calcula os coeficientes
            lcm_val = lcm([term.q for term in solution])
            coefficients = [abs(int(term * lcm_val)) for term in solution]
            
            # Formata a equação balanceada
            balanced_reactants = []
            for i, reactant in enumerate(reactants):
                coef = coefficients[i]
                if coef == 1:
                    balanced_reactants.append(reactant)
                else:
                    balanced_reactants.append(f"{coef}{reactant}")
            
            balanced_products = []
            for i, product in enumerate(products):
                coef = coefficients[i + len(reactants)]
                if coef == 1:
                    balanced_products.append(product)
                else:
                    balanced_products.append(f"{coef}{product}")
            
            return " + ".join(balanced_reactants) + " → " + " + ".join(balanced_products)

        # Processa as entradas
        print(f"Debug - Reagentes recebidos: {equacao_reagentes}")
        print(f"Debug - Produtos recebidos: {equacao_produtos}")

        # Separa os reagentes e produtos
        reactants = [r.strip() for r in equacao_reagentes.replace(',', '+').split('+') if r.strip()]
        products = [p.strip() for p in equacao_produtos.replace(',', '+').split('+') if p.strip()]

        print(f"Debug - Reagentes processados: {reactants}")
        print(f"Debug - Produtos processados: {products}")

        if not reactants or not products:
            raise ValueError("As equações dos reagentes e produtos não podem estar vazias.")

        # Balanceia a equação
        balanced_equation = balance_chemical_equation(reactants, products)
        print(f"Debug - Equação balanceada: {balanced_equation}")

        return {'equacao_balanceada': balanced_equation}, {'equacao_balanceada': ''}
        
    except ValueError as e:
        print(f"Debug - Erro de valor: {str(e)}")
        raise ValueError(f"Erro no Balanceamento: {str(e)}")
    except Exception as e:
        print(f"Debug - Erro inesperado: {str(e)}")
        raise ValueError(f"Erro inesperado no Balanceamento: {str(e)}")
    
def gases(
    pressao: Optional[float] = None,
    volume: Optional[float] = None,
    numero_de_mols: Optional[float] = None,
    temperatura: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        # Validação dos tipos de entrada
        for param_name, param_value in [('pressao', pressao), ('volume', volume), 
                                      ('numero_de_mols', numero_de_mols), ('temperatura', temperatura)]:
            if param_value is not None and not isinstance(param_value, (int, float)):
                raise TypeError(f"O parâmetro {param_name} deve ser um número.")

        valores = {'pressao': pressao, 'volume': volume, 'numero_de_mols': numero_de_mols, 'temperatura': temperatura}
        none_count = sum(1 for v in valores.values() if v is None)
        constante_gases = 0.082

        if none_count != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")
        
        # Validações para valores não nulos
        if pressao is not None and pressao <= 0:
            raise ValueError("A pressão deve ser maior que zero.")
        if volume is not None and volume <= 0:
            raise ValueError("O volume deve ser maior que zero.")
        if numero_de_mols is not None and numero_de_mols <= 0:
            raise ValueError("O número de mols deve ser maior que zero.")
        if temperatura is not None and temperatura <= 0:
            raise ValueError("A temperatura deve ser maior que zero.")

        # Cálculos com tratamento de overflow
        try:
            if pressao is None:
                pressao = (numero_de_mols * constante_gases * temperatura) / volume
                if not math.isfinite(pressao):
                    raise ValueError("Resultado do cálculo da pressão é inválido.")
                return {'Pressão do Gás': pressao}, {'Pressão do Gás': 'atm'}
            elif volume is None:
                volume = (numero_de_mols * constante_gases * temperatura) / pressao
                if not math.isfinite(volume):
                    raise ValueError("Resultado do cálculo do volume é inválido.")
                return {'Volume do Gás': volume}, {'Volume do Gás': 'L'}
            elif numero_de_mols is None:
                numero_de_mols = (pressao * volume) / (constante_gases * temperatura)
                if not math.isfinite(numero_de_mols):
                    raise ValueError("Resultado do cálculo do número de mols é inválido.")
                return {'Número de Mols': numero_de_mols}, {'Número de Mols': 'mol'}
            else:
                temperatura = (pressao * volume) / (numero_de_mols * constante_gases)
                if not math.isfinite(temperatura):
                    raise ValueError("Resultado do cálculo da temperatura é inválido.")
                return {'Temperatura do Gás': temperatura}, {'Temperatura do Gás': 'K'}
        except OverflowError:
            raise ValueError("O resultado do cálculo é muito grande para ser representado.")
        except ZeroDivisionError:
            raise ValueError("Divisão por zero detectada. Verifique os valores de entrada.")
            
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro nos Gases: {str(e)}")
    
def tabela_periodica(
    elemento: Optional[str] = None,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        if elemento is None:
            raise ValueError("O elemento deve ser fornecido.")
        
        if not isinstance(elemento, str):
            raise TypeError("O elemento deve ser uma string.")
        
        elemento = elemento.strip().capitalize()
        if not elemento:
            raise ValueError("O nome do elemento não pode estar vazio.")
        
        if elemento not in tabela_periodica:
            raise ValueError(f"O elemento '{elemento}' não foi encontrado na tabela periódica ou foi escrito incorretamente.")
        
        info = tabela_periodica[elemento]
        resultado = {
            'Elemento': elemento,
            'Símbolo': info['símbolo'],
            'Número Atômico': info['número_atômico'],
            'Massa Atômica': info['massa_atômica']
        }
        unidades = {
            'Elemento': '',
            'Símbolo': '',
            'Número Atômico': '',
            'Massa Atômica': 'u'
        }
        return resultado, unidades
    except (TypeError, ValueError, KeyError) as e:
        raise ValueError(f"Erro na Tabela Periódica: {str(e)}")
    
def pilha_de_daniels(
    equacao_reagentes: Optional[str] = None,
    equacao_produtos: Optional[str] = None,
    concentracao_dos_reagentes: Optional[float] = None,
    concentracao_dos_produtos: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        # Validação dos tipos de entrada
        if not isinstance(equacao_reagentes, str) or not isinstance(equacao_produtos, str):
            raise TypeError("As equações devem ser strings.")
        
        for param_name, param_value in [('concentracao_dos_reagentes', concentracao_dos_reagentes),
                                      ('concentracao_dos_produtos', concentracao_dos_produtos)]:
            if param_value is not None and not isinstance(param_value, (int, float)):
                raise TypeError(f"O parâmetro {param_name} deve ser um número.")

        valores = {
            'equacao_reagentes': equacao_reagentes,
            'equacao_produtos': equacao_produtos,
            'concentracao_dos_produtos': concentracao_dos_produtos,
            'concentracao_dos_reagentes': concentracao_dos_reagentes
        }
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count > 0:
            raise ValueError("Todos os valores devem ser fornecidos para calcular o potencial da pilha.")
        
        if concentracao_dos_reagentes <= 0 or concentracao_dos_produtos <= 0:
            raise ValueError("As concentrações devem ser maiores que zero.")
        
        # Validação e processamento das equações
        reagentes = [r.strip() for r in equacao_reagentes.split(',')]
        produtos = [p.strip() for p in equacao_produtos.split(',')]
        
        if len(reagentes) != 2 or len(produtos) != 2:
            raise ValueError("As equações devem conter exatamente dois elementos separados por vírgula.")
        
        # Obter os potenciais padrão dos eletrodos
        try:
            potencial_catodo = tabela_potenciais[produtos[1]]  # Redução
            potencial_anodo = tabela_potenciais[reagentes[0]]  # Oxidação
        except KeyError as e:
            raise ValueError(f"O elemento '{e}' não foi encontrado na tabela de potenciais ou foi escrito incorretamente.")
        
        # Calcular diferença de potencial padrão
        E_pilha_0 = potencial_catodo - potencial_anodo
        
        # Aplicação da equação de Nernst com tratamento de erros
        try:
            n = 2  # Número de elétrons transferidos (caso da pilha de Daniell Zn-Cu)
            from math import log10
            E_pilha = E_pilha_0 - (0.0592 / n) * log10(concentracao_dos_produtos / concentracao_dos_reagentes)
            
            if not math.isfinite(E_pilha):
                raise ValueError("O resultado do cálculo do potencial é inválido.")
            
            resultado = {
                'Potencial Padrão da Pilha': E_pilha_0,
                'Potencial Real da Pilha': E_pilha
            }
            unidades = {
                'Potencial Padrão da Pilha': 'V',
                'Potencial Real da Pilha': 'V'
            }
            
            return resultado, unidades
        except (OverflowError, ZeroDivisionError) as e:
            raise ValueError(f"Erro no cálculo do potencial: {str(e)}")
        
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro na Pilha de Daniels: {str(e)}")
    
def termoquimica(
    delta_h: Optional[float] = None,
    entalpia_dos_reagentes: Optional[float] = None,
    entalpia_dos_produtos: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        # Validação dos tipos de entrada
        for param_name, param_value in [('delta_h', delta_h), 
                                      ('entalpia_dos_reagentes', entalpia_dos_reagentes),
                                      ('entalpia_dos_produtos', entalpia_dos_produtos)]:
            if param_value is not None and not isinstance(param_value, (int, float)):
                raise TypeError(f"O parâmetro {param_name} deve ser um número.")

        valores = {
            'delta_h': delta_h,
            'entalpia_dos_produtos': entalpia_dos_produtos,
            'entalpia_dos_reagentes': entalpia_dos_reagentes
        }
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
        
        # Cálculos com tratamento de overflow
        try:
            if delta_h is None:
                delta_h = entalpia_dos_produtos - entalpia_dos_reagentes
                if not math.isfinite(delta_h):
                    raise ValueError("Resultado do cálculo da variação de entalpia é inválido.")
                return {'Variação de Entalpia': delta_h}, {'Variação de Entalpia': 'kJ/mol'}
            elif entalpia_dos_produtos is None:
                entalpia_dos_produtos = delta_h + entalpia_dos_reagentes
                if not math.isfinite(entalpia_dos_produtos):
                    raise ValueError("Resultado do cálculo da entalpia dos produtos é inválido.")
                return {'Entalpia dos Produtos': entalpia_dos_produtos}, {'Entalpia dos Produtos': 'kJ/mol'}
            else:
                entalpia_dos_reagentes = entalpia_dos_produtos - delta_h
                if not math.isfinite(entalpia_dos_reagentes):
                    raise ValueError("Resultado do cálculo da entalpia dos reagentes é inválido.")
                return {'Entalpia dos Reagentes': entalpia_dos_reagentes}, {'Entalpia dos Reagentes': 'kJ/mol'}
        except OverflowError:
            raise ValueError("O resultado do cálculo é muito grande para ser representado.")
            
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro na Termoquímica: {str(e)}")
    
def equilibrio_ionico(
    acido_ou_base: Optional[str] = None,
    constante_de_equilibrio: Optional[float] = None,
    concentracao_incial: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        # Validação dos tipos de entrada
        if not isinstance(acido_ou_base, str):
            raise TypeError("O tipo (ácido/base) deve ser uma string.")
        
        for param_name, param_value in [('constante_de_equilibrio', constante_de_equilibrio),
                                      ('concentracao_incial', concentracao_incial)]:
            if param_value is not None and not isinstance(param_value, (int, float)):
                raise TypeError(f"O parâmetro {param_name} deve ser um número.")

        acido_ou_base = acido_ou_base.strip().lower()
        if acido_ou_base not in ["ácido", "base"]:
            raise ValueError("O tipo deve ser 'ácido' ou 'base'.")
        
        if constante_de_equilibrio is None or concentracao_incial is None:
            raise ValueError("A constante de equilíbrio e a concentração inicial são obrigatórias.")
        
        if constante_de_equilibrio <= 0:
            raise ValueError("A constante de equilíbrio deve ser maior que zero.")
        
        if concentracao_incial <= 0:
            raise ValueError("A concentração inicial deve ser maior que zero.")
        
        # Resolver a equação do equilíbrio: Ka ou Kb = x² / (C - x)
        try:
            a = 1  # Coeficiente de x²
            b = constante_de_equilibrio  # Coeficiente de x
            c = -constante_de_equilibrio * concentracao_incial  # Termo constante

            # Resolvendo a equação quadrática: ax² + bx + c = 0
            delta = b**2 - 4*a*c
            if delta < 0:
                raise ValueError("Não há solução real para essa equação de equilíbrio.")
            
            x = (-b + math.sqrt(delta)) / (2*a)  # Apenas a solução positiva faz sentido
            
            if not math.isfinite(x):
                raise ValueError("O resultado do cálculo da concentração é inválido.")
            
            # Concentrações no equilíbrio
            H3O_OH = x  # H3O+ se for um ácido, OH- se for uma base
            C_remanescente = concentracao_incial - x  # Concentração restante do ácido/base não dissociado
            
            if C_remanescente < 0:
                raise ValueError("A concentração remanescente não pode ser negativa.")
            
            resultado = {}
            unidades = {}
            
            if acido_ou_base == "ácido":
                pH = -math.log10(H3O_OH)
                if not math.isfinite(pH):
                    raise ValueError("O resultado do cálculo do pH é inválido.")
                resultado = {
                    'Concentração de H3O⁺': H3O_OH,
                    'pH': pH,
                    'Ácido não dissociado': C_remanescente
                }
                unidades = {
                    'Concentração de H3O⁺': 'mol/L',
                    'pH': '',
                    'Ácido não dissociado': 'mol/L'
                }
            else:  # base
                pOH = -math.log10(H3O_OH)
                pH = 14 - pOH
                if not math.isfinite(pH) or not math.isfinite(pOH):
                    raise ValueError("O resultado do cálculo do pH/pOH é inválido.")
                resultado = {
                    'Concentração de OH⁻': H3O_OH,
                    'pOH': pOH,
                    'pH': pH,
                    'Base não dissociada': C_remanescente
                }
                unidades = {
                    'Concentração de OH⁻': 'mol/L',
                    'pOH': '',
                    'pH': '',
                    'Base não dissociada': 'mol/L'
                }
            
            return resultado, unidades
            
        except (OverflowError, ZeroDivisionError) as e:
            raise ValueError(f"Erro no cálculo do equilíbrio: {str(e)}")
        
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro no Equilíbrio Iônico: {str(e)}")
    