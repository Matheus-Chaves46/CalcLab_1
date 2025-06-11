from typing import Dict, List, Union, Optional, Tuple
import math

def calculate_fisica(tipo_calculo: str, **kwargs) -> Tuple[Dict[str, float], Dict[str, str]]:
    """
    Função principal para calcular resultados de física.
    
    Args:
        tipo_calculo (str): Tipo de cálculo a ser realizado
        **kwargs: Valores necessários para o cálculo
        
    Returns:
        Tuple[Dict[str, float], Dict[str, str]]: Resultado do cálculo e suas unidades
    """
    # Mapeamento de tipos de cálculo para suas respectivas funções
    calculos = {
        'velocidade_media': velocidade_media,
        'movimento_uniforme': movimento_uniforme,
        'movimento_uniformemente_variado': movimento_uniformemente_variado,
        'equacao_torricelli': equacao_torricelli,
        'principio_fundamental_dinamica': principio_fundamental_dinamica,
        'forca_peso': forca_peso,
        'forca_atrito': forca_atrito,
        'trabalho_forca_constante': trabalho_forca_constante,
        'energia_cinetica': energia_cinetica,
        'energia_potencial': energia_potencial,
        'energia_potencial_elastica': energia_potencial_elastica,
        'potencia': potencia,
        'pressao': pressao,
        'pressao_hidrostatica': pressao_hidrostatica,
        'empuxo': empuxo,
        'dilatacao_linear': dilatacao_linear,
        'equacao_fundamental_calorimetria': equacao_fundamental_calorimetria,
        'primeira_lei_termodinamica': primeira_lei_termodinamica,
        'equacao_dos_espelhos_e_lentes': equacao_dos_espelhos_e_lentes,
        'formula_do_aumento_da_imagem': formula_do_aumento_da_imagem,
        'velocidade_onda': velocidade_onda,
        'lei_ohm': lei_ohm,
        'potencia_eletrica': potencia_eletrica,
        'forca_entre_cargas_eletricas': forca_entre_cargas_eletricas,
        'energia_potencial_elastica': energia_potencial_elastica,
        'energia_mecanica': energia_mecanica
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

def velocidade_media(
    velocidade_media: Optional[float] = None,
    deslocamento: Optional[float] = None,
    tempo: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'velocidade_media': velocidade_media, 'deslocamento': deslocamento, 'tempo': tempo}
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
        
        if velocidade_media is None:
            if tempo == 0:
                raise ValueError("Tempo não pode ser zero para calcular a velocidade média.")
            velocidade_media = deslocamento / tempo
            return {'velocidade_media': velocidade_media}, {'velocidade_media': 'm/s'}
        elif deslocamento is None:
            deslocamento = velocidade_media * tempo
            return {'deslocamento': deslocamento}, {'deslocamento': 'm'}
        else: # tempo is None
            if velocidade_media == 0:
                raise ValueError("Velocidade média não pode ser zero para calcular o tempo.")
            tempo = deslocamento / velocidade_media
            return {'tempo': tempo}, {'tempo': 's'}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Velocidade Média: {str(e)}")

def movimento_uniforme(
    posicao_final: Optional[float] = None,
    posicao_inicial: Optional[float] = None,
    tempo: Optional[float] = None,
    velocidade: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'posicao_final': posicao_final, 'posicao_inicial': posicao_inicial, 'tempo': tempo, 'velocidade': velocidade}
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")
        
        if posicao_final is None:
            posicao_final = posicao_inicial + velocidade * tempo
            return {'posicao_final': posicao_final}, {'posicao_final': 'm'}
        elif posicao_inicial is None:
            posicao_inicial = posicao_final - velocidade * tempo
            return {'posicao_inicial': posicao_inicial}, {'posicao_inicial': 'm'}
        elif tempo is None:
            if velocidade == 0:
                raise ValueError("Velocidade não pode ser zero para calcular o tempo.")
            tempo = (posicao_final - posicao_inicial) / velocidade
            if tempo < 0:
                raise ValueError("Tempo negativo não é fisicamente possível.")
            return {'tempo': tempo}, {'tempo': 's'}
        else: # velocidade is None
            if tempo == 0:
                raise ValueError("Tempo não pode ser zero para calcular a velocidade.")
            velocidade = (posicao_final - posicao_inicial) / tempo
            return {'velocidade': velocidade}, {'velocidade': 'm/s'}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no Movimento Uniforme: {str(e)}")

def movimento_uniformemente_variado(
    posicao_final: Optional[float] = None,
    posicao_inicial: Optional[float] = None,
    velocidade_inicial: Optional[float] = None,
    tempo: Optional[float] = None,
    aceleracao: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'posicao_final': posicao_final, 'posicao_inicial': posicao_inicial, 
                  'velocidade_inicial': velocidade_inicial, 'tempo': tempo, 'aceleracao': aceleracao}
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente quatro valores devem ser fornecidos para calcular o quinto.")
        
        if posicao_final is None:
            posicao_final = posicao_inicial + velocidade_inicial * tempo + (aceleracao * tempo**2) / 2
            return {'posicao_final': posicao_final}, {'posicao_final': 'm'}
        elif posicao_inicial is None:
            posicao_inicial = posicao_final - velocidade_inicial * tempo - (aceleracao * tempo**2) / 2
            return {'posicao_inicial': posicao_inicial}, {'posicao_inicial': 'm'}
        elif velocidade_inicial is None:
            if tempo == 0:
                raise ValueError("Tempo não pode ser zero para calcular a velocidade inicial.")
            velocidade_inicial = (posicao_final - posicao_inicial - (aceleracao * tempo**2) / 2) / tempo
            return {'velocidade_inicial': velocidade_inicial}, {'velocidade_inicial': 'm/s'}
        elif tempo is None:
            # Resolve equação quadrática
            a = aceleracao/2
            b = velocidade_inicial
            c = posicao_inicial - posicao_final

            if a == 0 and b == 0: # Caso degenerado
                 raise ValueError("Não é possível calcular o tempo com os valores fornecidos (aceleração e velocidade inicial são zero).")

            if a == 0: # Equação linear
                if b == 0:
                    raise ValueError("Não é possível calcular o tempo. Velocidade inicial não pode ser zero se aceleração é zero.")
                tempo = -c / b
                if tempo < 0:
                    raise ValueError("Tempo negativo não é fisicamente possível.")
                return {'tempo': tempo}, {'tempo': 's'}

            delta = b**2 - 4*a*c
            if delta < 0:
                raise ValueError("Não há solução real para o tempo com os valores fornecidos.")
            
            tempo1 = (-b + math.sqrt(delta))/(2*a)
            tempo2 = (-b - math.sqrt(delta))/(2*a)
            
            # Retorna o tempo positivo, se houver
            if tempo1 >= 0 and tempo2 >= 0:
                return {'tempo': min(tempo1, tempo2)}, {'tempo': 's'} # Retorna o menor tempo positivo
            elif tempo1 >= 0:
                return {'tempo': tempo1}, {'tempo': 's'}
            elif tempo2 >= 0:
                return {'tempo': tempo2}, {'tempo': 's'}
            else:
                raise ValueError("Não há tempos positivos válidos com os valores fornecidos.")
        else:
            if tempo == 0:
                raise ValueError("Tempo não pode ser zero para calcular a aceleração.")
            aceleracao = 2*(posicao_final - posicao_inicial - velocidade_inicial * tempo)/tempo**2
            return {'aceleracao': aceleracao}, {'aceleracao': 'm/s²'}

    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no MUV: {str(e)}")

def equacao_torricelli(
    velocidade_final: Optional[float] = None,
    velocidade_inicial: Optional[float] = None,
    aceleracao: Optional[float] = None,
    deslocamento: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'velocidade_final': velocidade_final, 'velocidade_inicial': velocidade_inicial,
                  'aceleracao': aceleracao, 'deslocamento': deslocamento}
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")
        
        if velocidade_final is None:
            if aceleracao == 0:
                raise ValueError("Aceleração não pode ser zero para calcular a velocidade final.")
            vf2 = velocidade_inicial**2 + 2 * aceleracao * deslocamento
            if vf2 < 0:
                raise ValueError("Não é possível ter velocidade real com os valores fornecidos (raiz de número negativo).")
            velocidade_final = math.sqrt(vf2)
            return {'velocidade_final': velocidade_final}, {'velocidade_final': 'm/s'}
        elif velocidade_inicial is None:
            if aceleracao == 0:
                raise ValueError("Aceleração não pode ser zero para calcular a velocidade inicial.")
            vi2 = velocidade_final**2 - 2 * aceleracao * deslocamento
            if vi2 < 0:
                raise ValueError("Não é possível ter velocidade real com os valores fornecidos (raiz de número negativo).")
            velocidade_inicial = math.sqrt(vi2)
            return {'velocidade_inicial': velocidade_inicial}, {'velocidade_inicial': 'm/s'}
        elif aceleracao is None:
            if deslocamento == 0:
                raise ValueError("Deslocamento não pode ser zero para calcular a aceleração.")
            aceleracao = (velocidade_final**2 - velocidade_inicial**2) / (2 * deslocamento)
            return {'aceleracao': aceleracao}, {'aceleracao': 'm/s²'}
        else: # deslocamento is None
            if aceleracao == 0:
                raise ValueError("Aceleração não pode ser zero para calcular o deslocamento.")
            deslocamento = (velocidade_final**2 - velocidade_inicial**2) / (2 * aceleracao)
            return {'deslocamento': deslocamento}, {'deslocamento': 'm'}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Equação de Torricelli: {str(e)}")

def principio_fundamental_dinamica(
    forca: Optional[float] = None,
    massa: Optional[float] = None,
    aceleracao: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'forca': forca, 'massa': massa, 'aceleracao': aceleracao}
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
        
        if forca is None:
            forca = massa * aceleracao
            return {'forca': forca}, {'forca': 'N'}
        elif massa is None:
            if aceleracao == 0:
                raise ValueError("Aceleração não pode ser zero para calcular a massa.")
            massa = forca / aceleracao
            return {'massa': massa}, {'massa': 'kg'}
        else: # aceleracao is None
            if massa == 0:
                raise ValueError("Massa não pode ser zero para calcular a aceleração.")
            aceleracao = forca / massa
            return {'aceleracao': aceleracao}, {'aceleracao': 'm/s²'}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no Princípio Fundamental da Dinâmica: {str(e)}")

def forca_peso(
    forca_peso: Optional[float] = None,
    massa: Optional[float] = None,
    gravidade: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'forca_peso': forca_peso, 'massa': massa, 'gravidade': gravidade}
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
        
        if forca_peso is None:
            forca_peso = massa * gravidade
            return {'forca_peso': forca_peso}, {'forca_peso': 'N'}
        elif massa is None:
            if gravidade == 0:
                raise ValueError("Gravidade não pode ser zero para calcular a massa.")
            massa = forca_peso / gravidade
            return {'massa': massa}, {'massa': 'kg'}
        else: # gravidade is None
            if massa == 0:
                raise ValueError("Massa não pode ser zero para calcular a gravidade.")
            gravidade = forca_peso / massa
            return {'gravidade': gravidade}, {'gravidade': 'm/s²'}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Força Peso: {str(e)}")

def forca_atrito(
    forca_atrito: Optional[float] = None,
    coeficiente: Optional[float] = None,
    normal: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'forca_atrito': forca_atrito, 'coeficiente': coeficiente, 'normal': normal}
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
        
        if forca_atrito is None:
            forca_atrito = coeficiente * normal
            return {'forca_atrito': forca_atrito}, {'forca_atrito': 'N'}
        elif coeficiente is None:
            if normal == 0:
                raise ValueError("Força normal não pode ser zero para calcular o coeficiente.")
            coeficiente = forca_atrito / normal
            return {'coeficiente': coeficiente}, {'coeficiente': '(adimensional)'}
        else: # normal is None
            if coeficiente == 0:
                raise ValueError("Coeficiente não pode ser zero para calcular a força normal.")
            normal = forca_atrito / coeficiente
            return {'normal': normal}, {'normal': 'N'}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Força de Atrito: {str(e)}")

def trabalho_forca_constante(
    trabalho: Optional[float] = None,
    forca: Optional[float] = None,
    deslocamento: Optional[float] = None,
    angulo: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'trabalho': trabalho, 'forca': forca, 'deslocamento': deslocamento, 'angulo': angulo}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")
        
        if trabalho is None:
            trabalho = forca * deslocamento * math.cos(math.radians(angulo))
            return {'trabalho': trabalho}, {'trabalho': 'J'}
        elif forca is None:
            den = (deslocamento * math.cos(math.radians(angulo)))
            if den == 0:
                raise ValueError("Denominador não pode ser zero para calcular a força.")
            forca = trabalho / den
            return {'forca': forca}, {'forca': 'N'}
        elif deslocamento is None:
            den = (forca * math.cos(math.radians(angulo)))
            if den == 0:
                raise ValueError("Denominador não pode ser zero para calcular o deslocamento.")
            deslocamento = trabalho / den
            return {'deslocamento': deslocamento}, {'deslocamento': 'm'}
        else: # angulo is None
            den = (forca * deslocamento)
            if den == 0:
                raise ValueError("Denominador não pode ser zero para calcular o ângulo.")
            cos_angulo = trabalho / den
            if not -1 <= cos_angulo <= 1:
                raise ValueError("Não é possível calcular o ângulo real com os valores fornecidos.")
            angulo = math.degrees(math.acos(cos_angulo))
            return {'angulo': angulo}, {'angulo': '°'}
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro no cálculo do Trabalho de Força Constante: {str(e)}")

def energia_cinetica(
    energia_cinetica: Optional[float] = None,
    massa: Optional[float] = None,
    velocidade: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'energia_cinetica': energia_cinetica, 'massa': massa, 'velocidade': velocidade}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
        
        if energia_cinetica is None:
            energia_cinetica = (massa * velocidade**2) / 2
            return {'energia_cinetica': energia_cinetica}, {'energia_cinetica': 'J'}
        elif massa is None:
            den = (velocidade**2)
            if den == 0:
                raise ValueError("Velocidade não pode ser zero para calcular a massa.")
            massa = (2 * energia_cinetica) / den
            return {'massa': massa}, {'massa': 'kg'}
        else: # velocidade is None
            arg = (2 * energia_cinetica) / massa
            if arg < 0:
                raise ValueError("Não é possível ter velocidade real com os valores fornecidos (raiz de número negativo).")
            velocidade = math.sqrt(arg)
            return {'velocidade': velocidade}, {'velocidade': 'm/s'}
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro no cálculo da Energia Cinética: {str(e)}")

def energia_potencial(
    energia_potencial: Optional[float] = None,
    massa: Optional[float] = None,
    altura: Optional[float] = None,
    gravidade: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'energia_potencial': energia_potencial, 'massa': massa, 'altura': altura, 'gravidade': gravidade}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")
        
        if energia_potencial is None:
            energia_potencial = massa * gravidade * altura
            return {'energia_potencial': energia_potencial}, {'energia_potencial': 'J'}
        elif massa is None:
            den = (gravidade * altura)
            if den == 0:
                raise ValueError("Gravidade ou altura não podem ser zero para calcular a massa.")
            massa = energia_potencial / den
            return {'massa': massa}, {'massa': 'kg'}
        elif altura is None:
            den = (massa * gravidade)
            if den == 0:
                raise ValueError("Massa ou gravidade não podem ser zero para calcular a altura.")
            altura = energia_potencial / den
            return {'altura': altura}, {'altura': 'm'}
        else: # gravidade is None
            den = (massa * altura)
            if den == 0:
                raise ValueError("Massa ou altura não podem ser zero para calcular a gravidade.")
            gravidade = energia_potencial / den
            return {'gravidade': gravidade}, {'gravidade': 'm/s²'}
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro no cálculo da Energia Potencial Gravitacional: {str(e)}")

def pressao_hidrostatica(
    pressao_hidrostatica: Optional[float] = None,
    densidade: Optional[float] = None,
    altura: Optional[float] = None,
    gravidade: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'pressao_hidrostatica': pressao_hidrostatica, 'densidade': densidade, 'altura': altura, 'gravidade': gravidade}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")
        
        if pressao_hidrostatica is None:
            pressao_hidrostatica = densidade * gravidade * altura
            return {'pressao_hidrostatica': pressao_hidrostatica}, {'pressao_hidrostatica': 'Pa'}
        elif densidade is None:
            densidade = (pressao_hidrostatica) / (gravidade * altura) 
            if densidade == 0:
                raise ValueError("Gravidade ou altura não podem ser zero para calcular a densidade.")
            return {'densidade': densidade}, {'densidade': 'kg/m³'}
        elif altura is None:
            altura = (densidade) / (gravidade * pressao_hidrostatica)
            if altura == 0:
                raise ValueError("Densidade ou gravidade não podem ser zero para calcular a altura.")
            return {'altura': altura}, {'altura': 'm'}
        else: # gravidade is None
            gravidade = (pressao_hidrostatica) / (densidade * altura)
            if gravidade == 0:
                raise ValueError("Densidade ou altura não podem ser zero para calcular a gravidade.")
            return {'gravidade': gravidade}, {'gravidade': 'm/s²'}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no cálculo da Pressão Hidrostática: {str(e)}")

def primeira_lei_termodinamica(
    variacao_interna: Optional[float] = None,
    calor: Optional[float] = None,
    trabalho: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'variacao_interna': variacao_interna, 'calor': calor, 'trabalho': trabalho}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")

        if variacao_interna is None:
            variacao_interna = calor - trabalho
            return {'variacao_interna': variacao_interna}, {'variacao_interna': 'J'}
        elif calor is None:
            calor = variacao_interna + trabalho
            return {'calor': calor}, {'calor': 'J'}
        else: # trabalho is None
            trabalho = calor - variacao_interna
            return {'trabalho': trabalho}, {'trabalho': 'J'}
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro na Primeira Lei da Termodinâmica: {str(e)}")

def lei_ohm(
    tensao: Optional[float] = None,
    resistencia: Optional[float] = None,
    corrente: Optional[float] = None
) -> Dict[str, str]:
    try:
        valores = {'tensao': tensao, 'resistencia': resistencia, 'corrente': corrente}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")

        if tensao is None:
            tensao = resistencia * corrente
            return {'tensao': f"{tensao:.2f} V"}
        elif resistencia is None:
            if corrente == 0:
                raise ValueError("Corrente não pode ser zero para calcular a resistência.")
            resistencia = tensao / corrente
            return {'resistencia': f"{resistencia:.2f} Ω"}
        else: # corrente is None
            if resistencia == 0:
                raise ValueError("Resistência não pode ser zero para calcular a corrente.")
            corrente = tensao / resistencia
            return {'corrente': f"{corrente:.2f} A"}
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro na Lei de Ohm: {str(e)}")

def potencia(
    potencia_media: Optional[float] = None,
    trabalho: Optional[float] = None,
    tempo: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'potencia_media': potencia_media, 'trabalho': trabalho, 'tempo': tempo}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
        
        if potencia_media is None:
            if tempo == 0:
                raise ValueError("Tempo não pode ser zero para calcular a potência.")
            potencia_media = trabalho / tempo
            return {'potencia_media': potencia_media}, {'potencia_media': 'W'}
        elif trabalho is None:
            trabalho = potencia_media * tempo
            return {'trabalho': trabalho}, {'trabalho': 'J'}
        else: # tempo is None
            if potencia_media == 0:
                raise ValueError("Potência não pode ser zero para calcular o tempo.")
            tempo = trabalho / potencia_media
            return {'tempo': tempo}, {'tempo': 's'}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no cálculo da Potência: {str(e)}")

def pressao(
    pressao: Optional[float] = None,
    forca: Optional[float] = None,
    area: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'pressao': pressao, 'forca': forca, 'area': area}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
        
        if pressao is None:
            if area == 0:
                raise ValueError("Área não pode ser zero para calcular a pressão.")
            pressao = forca / area
            return {'pressao': pressao}, {'pressao': 'Pa'}
        elif forca is None:
            forca = pressao * area
            return {'forca': forca}, {'forca': 'N'}
        else: # area is None
            if pressao == 0:
                raise ValueError("Pressão não pode ser zero para calcular a área.")
            area = forca / pressao
            return {'area': area}, {'area': 'm²'}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no cálculo da Pressão: {str(e)}")

def equacao_dos_espelhos_e_lentes(
    distancia_focal: Optional[float] = None,
    distancia_objeto: Optional[float] = None,
    distancia_imagem: Optional[float] = None
) -> Dict[str, str]:
    try:
        valores = {'distancia_focal': distancia_focal, 'distancia_objeto': distancia_objeto, 'distancia_imagem': distancia_imagem}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")

        if distancia_focal is None:
            if distancia_objeto == 0 or distancia_imagem == 0: 
                raise ValueError("Distância do objeto ou da imagem não podem ser zero para calcular a distância focal.")
            distancia_focal = 1 / ((1 / distancia_objeto) + (1 / distancia_imagem))
            return {'distancia_focal': f"{distancia_focal:.2f} m"}
        elif distancia_objeto is None:
            if distancia_focal == 0 or distancia_imagem == 0 or (distancia_imagem - distancia_focal) == 0:
                raise ValueError("Distância focal ou da imagem não podem ser zero para calcular a distância do objeto, ou a diferença entre elas.")
            distancia_objeto = 1 / ((1 / distancia_focal) - (1 / distancia_imagem))
            return {'distancia_objeto': f"{distancia_objeto:.2f} m"}
        else: # distancia_imagem is None
            if distancia_focal == 0 or distancia_objeto == 0 or (distancia_objeto - distancia_focal) == 0:
                raise ValueError("Distância focal ou do objeto não podem ser zero para calcular a distância da imagem, ou a diferença entre elas.")
            distancia_imagem = 1 / ((1 / distancia_focal) - (1 / distancia_objeto))
            return {'distancia_imagem': f"{distancia_imagem:.2f} m"}
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro no cálculo da Equação dos Espelhos e Lentes: {str(e)}")

def formula_do_aumento_da_imagem(
    altura_imagem: Optional[float] = None,
    altura_objeto: Optional[float] = None,
    distancia_objeto: Optional[float] = None,
    distancia_imagem: Optional[float] = None
) -> Dict[str, str]:
    try:
        valores = {'altura_imagem': altura_imagem, 'altura_objeto': altura_objeto, 'distancia_objeto': distancia_objeto, 'distancia_imagem': distancia_imagem}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")

        if altura_imagem is None:
            if distancia_objeto == 0:
                raise ValueError("Distância do objeto não pode ser zero para calcular a altura da imagem.")
            altura_imagem = (-distancia_imagem / distancia_objeto) * altura_objeto
            return {'altura_imagem': f"{altura_imagem:.2f} m"}
        elif altura_objeto is None:
            if distancia_objeto == 0:
                raise ValueError("Distância do objeto não pode ser zero para calcular a altura do objeto.")
            altura_objeto = altura_imagem / (-distancia_imagem / distancia_objeto)
            return {'altura_objeto': f"{altura_objeto:.2f} m"}
        elif distancia_objeto is None:
            if altura_objeto == 0:
                raise ValueError("Altura do objeto não pode ser zero para calcular a distância do objeto.")
            distancia_objeto = distancia_imagem / (altura_imagem / altura_objeto)
            return {'distancia_objeto': f"{distancia_objeto:.2f} m"}
        else: # distancia_imagem is None
            if altura_objeto == 0:
                raise ValueError("Altura do objeto não pode ser zero para calcular a distância da imagem.")
            distancia_imagem = (-altura_imagem / altura_objeto) * distancia_objeto
            return {'distancia_imagem': f"{distancia_imagem:.2f} m"}
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro no cálculo do Aumento da Imagem: {str(e)}")

def velocidade_onda(
    velocidade: Optional[float] = None,
    frequencia: Optional[float] = None,
    comprimento_onda: Optional[float] = None
) -> Dict[str, str]:
    try:
        valores = {'velocidade': velocidade, 'frequencia': frequencia, 'comprimento_onda': comprimento_onda}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")

        if velocidade is None:
            velocidade = frequencia * comprimento_onda
            return {'velocidade': f"{velocidade:.2f} m/s"}
        elif frequencia is None:
            if comprimento_onda == 0:
                raise ValueError("Comprimento de onda não pode ser zero para calcular a frequência.")
            frequencia = velocidade / comprimento_onda
            return {'frequencia': f"{frequencia:.2f} Hz"}
        else: # comprimento_onda is None
            if frequencia == 0:
                raise ValueError("Frequência não pode ser zero para calcular o comprimento de onda.")
            comprimento_onda = velocidade / frequencia
            return {'comprimento_onda': f"{comprimento_onda:.2f} m"}
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro no cálculo da Velocidade da Onda: {str(e)}")

def empuxo(
    empuxo: Optional[float] = None,
    densidade: Optional[float] = None,
    volume: Optional[float] = None,
    gravidade: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'empuxo': empuxo, 'densidade': densidade, 'volume': volume, 'gravidade': gravidade}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")
        
        if empuxo is None:
            empuxo = densidade * volume * gravidade
            return {'empuxo': empuxo}, {'empuxo': 'N'}
        elif densidade is None:
            den = (volume * gravidade)
            if den == 0:
                raise ValueError("Volume ou gravidade não podem ser zero para calcular a densidade.")
            densidade = empuxo / den
            return {'densidade': densidade}, {'densidade': 'kg/m³'}
        elif volume is None:
            den = (densidade * gravidade)
            if den == 0:
                raise ValueError("Densidade ou gravidade não podem ser zero para calcular o volume.")
            volume = empuxo / den
            return {'volume': volume}, {'volume': 'm³'}
        else: # gravidade is None
            den = (densidade * volume)
            if den == 0:
                raise ValueError("Densidade ou volume não podem ser zero para calcular a gravidade.")
            gravidade = empuxo / den
            return {'gravidade': gravidade}, {'gravidade': 'm/s²'}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no cálculo do Empuxo: {str(e)}")

def dilatacao_linear(
    coeficiente_dilatacao: Optional[float] = None,
    comprimento_inicial: Optional[float] = None,
    dilatacao_linear: Optional[float] = None,
    variacao_de_temperatura: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    coeficiente_dilatacao = coeficiente_dilatacao * 10**-5
    try:
        valores = {'coeficiente_dilataco': coeficiente_dilatacao, 'comprimento_inicial': comprimento_inicial, 'variacao_de_temperatura': variacao_de_temperatura, 'dilatacao_linear': dilatacao_linear}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")
        
        if coeficiente_dilatacao is None:
            coeficiente_dilatacao = (dilatacao_linear) / (variacao_de_temperatura * comprimento_inicial)
            return {'coeficiente_dilatacao': coeficiente_dilatacao}, {'coeficiente_dilatacao': 'm'}
        elif comprimento_inicial is None:
            if comprimento_inicial == 0:
                raise ValueError("Denominador não pode ser zero para calcular o comprimento inicial.")
            comprimento_inicial = (dilatacao_linear) / (coeficiente_dilatacao * variacao_de_temperatura)
            return {'comprimento_inicial': comprimento_inicial}, {'comprimento_inicial': 'm'}
        elif dilatacao_linear is None:
            if dilatacao_linear == 0:
                raise ValueError("Comprimento inicial ou variação de temperatura não podem ser zero para calcular o coeficiente.")
            dilatacao_linear = (comprimento_inicial * coeficiente_dilatacao * variacao_de_temperatura)
            return {f'dilatacao_linear': dilatacao_linear}, {'dilatacao_linear': '°C⁻¹'}
        else: # variacao_de_temperatura is None
            if variacao_de_temperatura == 0:
                raise ValueError("Comprimento inicial ou coeficiente não podem ser zero para calcular a variação de temperatura.")
            variacao_de_temperatura = (dilatacao_linear) / (coeficiente_dilatacao * comprimento_inicial)
            return {'variacao_de_temperatura': variacao_de_temperatura}, {'variacao_de_temperatura': '°C'}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no cálculo da Dilatação Linear: {str(e)}")

def equacao_fundamental_calorimetria(
    calor: Optional[float] = None,
    massa: Optional[float] = None,
    calor_especifico: Optional[float] = None,
    variacao_temperatura: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'calor': calor, 'massa': massa, 'calor_especifico': calor_especifico,
                  'variacao_temperatura': variacao_temperatura}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")
        
        if calor is None:
            calor = massa * calor_especifico * variacao_temperatura
            return {'calor': calor}, {'calor': 'J'}
        elif massa is None:
            den = (calor_especifico * variacao_temperatura)
            if den == 0:
                raise ValueError("Calor específico ou variação de temperatura não podem ser zero para calcular a massa.")
            massa = calor / den
            return {'massa': massa}, {'massa': 'kg'}
        elif calor_especifico is None:
            den = (massa * variacao_temperatura)
            if den == 0:
                raise ValueError("Massa ou variação de temperatura não podem ser zero para calcular o calor específico.")
            calor_especifico = calor / den
            return {'calor_especifico': calor_especifico}, {'calor_especifico': 'J/(kg·°C)'}
        else: # variacao_temperatura is None
            den = (massa * calor_especifico)
            if den == 0:
                raise ValueError("Massa ou calor específico não podem ser zero para calcular a variação de temperatura.")
            variacao_temperatura = calor / den
            return {'variacao_temperatura': variacao_temperatura}, {'variacao_temperatura': '°C'}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no cálculo da Equação Fundamental da Calorimetria: {str(e)}")

def potencia_eletrica(
    potencia: Optional[float] = None,
    tensao: Optional[float] = None,
    corrente: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'potencia': potencia, 'tensao': tensao, 'corrente': corrente}
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
        
        if potencia is None:
            potencia = tensao * corrente
            return {'potencia': potencia}, {'potencia': 'W'}
        elif tensao is None:
            if corrente == 0:
                raise ValueError("Corrente não pode ser zero para calcular a tensão.")
            tensao = potencia / corrente
            return {'tensao': tensao}, {'tensao': 'V'}
        else: # corrente is None
            if tensao == 0:
                raise ValueError("Tensão não pode ser zero para calcular a corrente.")
            corrente = potencia / tensao
            return {'corrente': corrente}, {'corrente': 'A'}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Potência Elétrica: {str(e)}")

def forca_entre_cargas_eletricas(
    forca: Optional[float] = None,
    carga1: Optional[float] = None,
    carga2: Optional[float] = None,
    distancia: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'forca': forca, 'carga1': carga1, 'carga2': carga2, 'distancia': distancia}
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")
        
        k = 9e9  # Constante de Coulomb
        
        if forca is None:
            if distancia == 0:
                raise ValueError("Distância não pode ser zero para calcular a força.")
            forca = k * abs(carga1 * carga2) / (distancia ** 2)
            return {'forca': forca}, {'forca': 'N'}
        elif carga1 is None:
            if carga2 == 0 or distancia == 0:
                raise ValueError("Carga2 e distância não podem ser zero para calcular carga1.")
            carga1 = (forca * distancia ** 2) / (k * abs(carga2))
            return {'carga1': carga1}, {'carga1': 'C'}
        elif carga2 is None:
            if carga1 == 0 or distancia == 0:
                raise ValueError("Carga1 e distância não podem ser zero para calcular carga2.")
            carga2 = (forca * distancia ** 2) / (k * abs(carga1))
            return {'carga2': carga2}, {'carga2': 'C'}
        else: # distancia is None
            if carga1 == 0 or carga2 == 0:
                raise ValueError("Cargas não podem ser zero para calcular a distância.")
            distancia = math.sqrt(k * abs(carga1 * carga2) / forca)
            return {'distancia': distancia}, {'distancia': 'm'}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Força entre Cargas Elétricas: {str(e)}")

def energia_potencial_elastica(
    energia_potencial_elastica: Optional[float] = None,
    constante_elastica: Optional[float] = None,
    deformacao: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'energia_potencial_elastica': energia_potencial_elastica, 'constante_elastica': constante_elastica, 'deformacao': deformacao}
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
        
        if energia is None:
            energia = (constante_elastica * deformacao ** 2) / 2
            return {'energia': energia}, {'energia': 'J'}
        elif constante_elastica is None:
            if deformacao == 0:
                raise ValueError("Deformação não pode ser zero para calcular a constante elástica.")
            constante_elastica = (2 * energia) / (deformacao ** 2)
            return {'constante_elastica': constante_elastica}, {'constante_elastica': 'N/m'}
        else: # deformacao is None
            if constante_elastica == 0:
                raise ValueError("Constante elástica não pode ser zero para calcular a deformação.")
            deformacao = math.sqrt((2 * energia) / constante_elastica)
            return {'deformacao': deformacao}, {'deformacao': 'm'}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Energia Potencial Elástica: {str(e)}")

def energia_mecanica(
    energia_mecanica: Optional[float] = None,
    energia_cinetica: Optional[float] = None,
    energia_potencial: Optional[float] = None
) -> Tuple[Dict[str, float], Dict[str, str]]:
    try:
        valores = {'energia_mecanica': energia_mecanica, 'energia_cinetica': energia_cinetica, 'energia_potencial': energia_potencial}
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
        
        if energia_mecanica is None:
            energia_mecanica = energia_cinetica + energia_potencial
            return {'energia_mecanica': energia_mecanica}, {'energia_mecanica': 'J'}
        elif energia_cinetica is None:
            energia_cinetica = energia_mecanica - energia_potencial
            return {'energia_cinetica': energia_cinetica}, {'energia_cinetica': 'J'}
        else: # energia_potencial is None
            energia_potencial = energia_mecanica - energia_cinetica
            return {'energia_potencial': energia_potencial}, {'energia_potencial': 'J'}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Energia Mecânica: {str(e)}")