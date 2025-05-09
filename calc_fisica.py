from typing import Dict, List, Union, Optional, Tuple
import math
def velocidade_media(deslocamento: Optional[float] = None, 
                  tempo: Optional[float] = None, 
                  velocidade_media: Optional[float] = None) -> Dict[str, float]:
    try:
        valores = {'deslocamento': deslocamento, 'tempo': tempo, 'velocidade': velocidade_media}
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos")
            
        if deslocamento is None:
            if tempo == 0:
                raise ValueError("Tempo não pode ser zero")
            deslocamento = f"{velocidade_media * tempo} m"
            return {'deslocamento': deslocamento}
        elif tempo is None:
            if velocidade_media == 0:
                raise ValueError("Velocidade não pode ser zero")
            tempo = f"{deslocamento / velocidade_media} s"
            return {'tempo': tempo}
        else:  # velocidade is None
            if tempo == 0:
                raise ValueError("Tempo não pode ser zero")
            velocidade_media = f"{deslocamento / tempo} m/s"
            return {'velocidade': velocidade_media}
            
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular velocidade média: {str(e)}")

def movimento_uniforme(posicao_final: Optional[float] = None,
                    posicao_inicial: Optional[float] = None,
                    velocidade: Optional[float] = None,
                    tempo: Optional[float] = None) -> Dict[str, float]:
    try:
        valores = {
            'posicao_final': posicao_final,
            'posicao_inicial': posicao_inicial,
            'velocidade': velocidade,
            'tempo': tempo
        }
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos")
            
        if posicao_final is None:
            return {'posicao_final': posicao_inicial + velocidade * tempo}
        elif posicao_inicial is None:
            return {'posicao_inicial': posicao_final - velocidade * tempo}
        elif velocidade is None:
            if tempo == 0:
                raise ValueError("Tempo não pode ser zero")
            return {'velocidade': (posicao_final - posicao_inicial) / tempo}
        else:  # tempo is None
            if velocidade == 0:
                raise ValueError("Velocidade não pode ser zero")
            return {'tempo': (posicao_final - posicao_inicial) / velocidade}
            
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular movimento uniforme: {str(e)}")

def movimento_uniformemente_variado(
    posicao_final: Optional[float] = None,
    posicao_inicial: Optional[float] = None,
    velocidade_inicial: Optional[float] = None,
    tempo: Optional[float] = None,
    aceleracao: Optional[float] = None
) -> Dict[str, float]:
    
    valores = {
        'posicao_final': posicao_final,
        'posicao_inicial': posicao_inicial,
        'velocidade_inicial': velocidade_inicial,
        'tempo': tempo,
        'aceleracao': aceleracao
    }
    
    none_count = sum(1 for v in valores.values() if v is None)
    if none_count != 1:
        raise ValueError("Exatamente quatro valores devem ser fornecidos")

    try:
        if posicao_final is None:
            return {'posicao_final': posicao_inicial + velocidade_inicial * tempo + (aceleracao * tempo**2)/2}
        elif posicao_inicial is None:
            return {'posicao_inicial': posicao_final - velocidade_inicial * tempo - (aceleracao * tempo**2)/2}
        elif velocidade_inicial is None:
            return {'velocidade_inicial': (posicao_final - posicao_inicial - (aceleracao * tempo**2)/2) / tempo}
        elif tempo is None:
            # Resolve equação quadrática
            a = aceleracao/2
            b = velocidade_inicial
            c = posicao_inicial - posicao_final
            delta = b**2 - 4*a*c
            tempo = (-b + math.sqrt(delta))/(2*a)
            return {'tempo': tempo}
        else:
            return {'aceleracao': 2*(posicao_final - posicao_inicial - velocidade_inicial * tempo)/tempo**2}

    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no MUV: {str(e)}")
def equacao_torricelli(
    velocidade_final: Optional[float] = None,
    velocidade_inicial: Optional[float] = None,
    aceleracao: Optional[float] = None,
    deslocamento: Optional[float] = None) -> Dict[str, float]:
    
    valores = {
        'velocidade_final': velocidade_final,
        'velocidade_inicial': velocidade_inicial,
        'aceleracao': aceleracao,
        'deslocamento': deslocamento
    }
    
    none_count = sum(1 for v in valores.values() if v is None)
    if none_count != 1:
        raise ValueError("Exatamente três valores devem ser fornecidos")

    try:
        if velocidade_final is None:
            return {'velocidade_final': math.sqrt(velocidade_inicial**2 + 2 * aceleracao * deslocamento)}
        elif velocidade_inicial is None:
            return {'velocidade_inicial': math.sqrt(velocidade_final**2 - 2 * aceleracao * deslocamento)}
        elif aceleracao is None:
            return {'aceleracao': (velocidade_final**2 - velocidade_inicial**2)/(2 * deslocamento)}
        else:
            return {'deslocamento': (velocidade_final**2 - velocidade_inicial**2)/(2 * aceleracao)}

    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Equação de Torricelli: {str(e)}")

def principio_fundamental_dinamica(
    forca: Optional[float] = None,
    massa: Optional[float] = None,
    aceleracao: Optional[float] = None
) -> Dict[str, float]:
    
    valores = {'forca': forca, 'massa': massa, 'aceleracao': aceleracao}
    none_count = sum(1 for v in valores.values() if v is None)
    
    if none_count != 1:
        raise ValueError("Exatamente dois valores devem ser fornecidos")

    try:
        if forca is None:
            return {'forca': massa * aceleracao}
        elif massa is None:
            if aceleracao == 0:
                raise ValueError("Aceleração não pode ser zero")
            return {'massa': forca / aceleracao}
        else:
            if massa == 0:
                raise ValueError("Massa não pode ser zero")
            return {'aceleracao': forca / massa}

    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no Princípio Fundamental: {str(e)}")
def forca_peso(
    forca_peso: Optional[float] = None,
    massa: Optional[float] = None,
    gravidade: Optional[float] = None
) -> Dict[str, float]:
    
    valores = {'forca_peso': forca_peso, 'massa': massa, 'gravidade': gravidade}
    none_count = sum(1 for v in valores.values() if v is None)
    
    if none_count != 1:
        raise ValueError("Exatamente dois valores devem ser fornecidos")

    try:
        if forca_peso is None:
            return {'forca_peso': massa * gravidade}
        elif massa is None:
            if gravidade == 0:
                raise ValueError("Gravidade não pode ser zero")
            return {'massa': forca_peso / gravidade}
        else:
            if massa == 0:
                raise ValueError("Massa não pode ser zero")
            return {'gravidade': forca_peso / massa}

    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Força Peso: {str(e)}")
def forca_atrito(
    forca_atrito: Optional[float] = None,
    coeficiente: Optional[float] = None,
    normal: Optional[float] = None
) -> Dict[str, float]:
    
    valores = {'forca_atrito': forca_atrito, 'coeficiente': coeficiente, 'normal': normal}
    none_count = sum(1 for v in valores.values() if v is None)
    
    if none_count != 1:
        raise ValueError("Exatamente dois valores devem ser fornecidos")

    try:
        if forca_atrito is None:
            return {'forca_atrito': coeficiente * normal}
        elif coeficiente is None:
            if normal == 0:
                raise ValueError("Força normal não pode ser zero")
            return {'coeficiente': forca_atrito / normal}
        else:
            if coeficiente == 0:
                raise ValueError("Coeficiente não pode ser zero")
            return {'normal': forca_atrito / coeficiente}

    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Força de Atrito: {str(e)}")
def trabalho_forca_constante(
    trabalho: Optional[float] = None,
    forca: Optional[float] = None,
    deslocamento: Optional[float] = None,
    angulo: Optional[float] = None
) -> Dict[str, float]:
    try:
        valores = {'trabalho': trabalho, 'forca': forca, 'deslocamento': deslocamento, 'angulo': angulo}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos")
        
        if trabalho is None:
            return {'trabalho': forca * deslocamento * math.cos(math.radians(angulo))}
        elif forca is None:
            return {'forca': trabalho / (deslocamento * math.cos(math.radians(angulo)))}
        elif deslocamento is None:
            return {'deslocamento': trabalho / (forca * math.cos(math.radians(angulo)))}
        else:
            return {'angulo': math.degrees(math.acos(trabalho / (forca * deslocamento)))}
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no cálculo: {str(e)}")
def energia_cinetica(
    energia_cinetica: Optional[float] = None,
    massa: Optional[float] = None,
    velocidade: Optional[float] = None
) -> Dict[str, float]:
    try:
        valores = {'energia_cinetica': energia_cinetica, 'massa': massa, 'velocidade': velocidade}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos")
        
        if energia_cinetica is None:
            return {'energia_cinetica': (massa * velocidade**2) / 2}
        elif massa is None:
            return {'massa': (2 * energia_cinetica) / (velocidade**2)}
        else:
            return {'velocidade': math.sqrt((2 * energia_cinetica) / massa)}
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no cálculo: {str(e)}")
    
def pressao_hidrostatica(
    pressao: Optional[float] = None,
    densidade: Optional[float] = None,
    gravidade: Optional[float] = None,
    altura: Optional[float] = None
) -> Dict[str, float]:
    try:
        valores = {'pressao': pressao, 'densidade': densidade, 'gravidade': gravidade, 'altura': altura}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos")
        
        if pressao is None:
            return {'pressao': densidade * gravidade * altura}
        elif densidade is None:
            return {'densidade': pressao / (gravidade * altura)}
        elif gravidade is None:
            return {'gravidade': pressao / (densidade * altura)}
        else:
            return {'altura': pressao / (densidade * gravidade)}
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no cálculo: {str(e)}")
    
def primeira_lei_termodinamica(
    variacao_interna: Optional[float] = None,
    calor: Optional[float] = None,
    trabalho: Optional[float] = None
) -> Dict[str, float]:
    try:
        valores = {'variacao_interna': variacao_interna, 'calor': calor, 'trabalho': trabalho}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos")
        
        if variacao_interna is None:
            return {'variacao_interna': calor - trabalho}
        elif calor is None:
            return {'calor': variacao_interna + trabalho}
        else:
            return {'trabalho': calor - variacao_interna}
    except TypeError as e:
        raise ValueError(f"Erro no cálculo: {str(e)}")
    
def lei_ohm(
    tensao: Optional[float] = None,
    resistencia: Optional[float] = None,
    corrente: Optional[float] = None
) -> Dict[str, float]:
    try:
        valores = {'tensao': tensao, 'resistencia': resistencia, 'corrente': corrente}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos")
        
        if tensao is None:
            return {'tensao': resistencia * corrente}
        elif resistencia is None:
            return {'resistencia': tensao / corrente}
        else:
            return {'corrente': tensao / resistencia}
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no cálculo: {str(e)}")

def potencia_eletrica(potencia: Optional[float] = None, 
                      tensao: Optional[float] = None, 
                      corrente: Optional[float] = None) -> Dict[str, float]:
    try:
        valores = {'potencia': potencia, 'tensao': tensao, 'corrente': corrente}
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos")
        
        if potencia is None:
            if tensao is None or corrente is None:
                raise ValueError("Valores insuficientes para calcular potência")
            return {'potencia': tensao * corrente}
        elif tensao is None:
            if corrente == 0:
                raise ValueError("Corrente não pode ser zero")
            return {'tensao': potencia / corrente}
        else:
            if tensao == 0:
                raise ValueError("Tensão não pode ser zero")
            return {'corrente': potencia / tensao}
            
    except (TypeError, ValueError, ZeroDivisionError) as e:
        raise ValueError(f"Erro ao calcular potência elétrica: {str(e)}")


def forca_entre_cargas_eletricas(forca: Optional[float] = None,
                                 k: Optional[float] = None,
                                 q1: Optional[float] = None,
                                 q2: Optional[float] = None,
                                 d: Optional[float] = None) -> Dict[str, float]:
    try:
        valores = {'forca': forca, 'k': k, 'q1': q1, 'q2': q2, 'd': d}
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente quatro valores devem ser fornecidos")
        
        if forca is None:
            if any(v is None for v in [k, q1, q2, d]):
                raise ValueError("Valores insuficientes para calcular força")
            if d == 0:
                raise ValueError("Distância não pode ser zero")
            return {'forca': (k * abs(q1 * q2)) / (d ** 2)}
        
        elif k is None:
            if any(v is None for v in [forca, q1, q2, d]):
                raise ValueError("Valores insuficientes para calcular constante k")
            if abs(q1 * q2) == 0:
                raise ValueError("Cargas não podem ser zero")
            return {'k': (forca * (d ** 2)) / abs(q1 * q2)}
        
        elif q1 is None:
            if any(v is None for v in [forca, k, q2, d]):
                raise ValueError("Valores insuficientes para calcular q1")
            if k * q2 == 0:
                raise ValueError("k ou q2 não podem ser zero")
            return {'q1': (forca * (d ** 2)) / (k * q2)}
        
        elif q2 is None:
            if any(v is None for v in [forca, k, q1, d]):
                raise ValueError("Valores insuficientes para calcular q2")
            if k * q1 == 0:
                raise ValueError("k ou q1 não podem ser zero")
            return {'q2': (forca * (d ** 2)) / (k * q1)}
        
        else:  # d is None
            if any(v is None for v in [forca, k, q1, q2]):
                raise ValueError("Valores insuficientes para calcular distância")
            if forca == 0:
                raise ValueError("Força não pode ser zero")
            return {'d': math.sqrt((k * abs(q1 * q2)) / forca)}
            
    except (TypeError, ValueError, ZeroDivisionError) as e:
        raise ValueError(f"Erro ao calcular força entre cargas: {str(e)}")


def energia_potencial_elastica(energia: Optional[float] = None,
                               constante: Optional[float] = None,
                               deformacao: Optional[float] = None) -> Dict[str, float]:
    try:
        valores = {'energia': energia, 'constante': constante, 'deformacao': deformacao}
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos")
        
        if energia is None:
            if constante is None or deformacao is None:
                raise ValueError("Valores insuficientes para calcular energia")
            return {'energia': 0.5 * constante * (deformacao ** 2)}
        
        elif constante is None:
            if energia is None or deformacao is None:
                raise ValueError("Valores insuficientes para calcular constante")
            if deformacao == 0:
                raise ValueError("Deformação não pode ser zero")
            return {'constante': (2 * energia) / (deformacao ** 2)}
        
        else:  # deformacao is None
            if energia is None or constante is None:
                raise ValueError("Valores insuficientes para calcular deformação")
            if constante == 0:
                raise ValueError("Constante elástica não pode ser zero")
            return {'deformacao': math.sqrt((2 * energia) / constante)}
            
    except (TypeError, ValueError, ZeroDivisionError) as e:
        raise ValueError(f"Erro ao calcular energia potencial elástica: {str(e)}")


def energia_mecanica(energia_mec: Optional[float] = None,
                     energia_cinetica: Optional[float] = None,
                     energia_potencial: Optional[float] = None) -> Dict[str, float]:
    try:
        valores = {
            'energia_mec': energia_mec,
            'energia_cinetica': energia_cinetica,
            'energia_potencial': energia_potencial
        }
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos")
        
        if energia_mec is None:
            if any(v is None for v in [energia_cinetica, energia_potencial]):
                raise ValueError("Valores insuficientes para calcular energia mecânica")
            return {'energia_mec': energia_cinetica + energia_potencial}
        
        elif energia_cinetica is None:
            if energia_mec is None or energia_potencial is None:
                raise ValueError("Valores insuficientes para calcular energia cinética")
            return {'energia_cinetica': energia_mec - energia_potencial}
        
        else:  # energia_potencial is None
            if energia_mec is None or energia_cinetica is None:
                raise ValueError("Valores insuficientes para calcular energia potencial")
            return {'energia_potencial': energia_mec - energia_cinetica}
            
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular energia mecânica: {str(e)}")
def energia_potencial(
    energia_potencial: Optional[float] = None,
    massa: Optional[float] = None,
    altura: Optional[float] = None,
    gravidade: Optional[float] = None
) -> Dict[str, float]:
    try:
        valores = {
            'energia_potencial': energia_potencial,
            'massa': massa,
            'altura': altura,
            'gravidade': gravidade
        }
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos")
            
        if energia_potencial is None:
            return {'energia_potencial': massa * gravidade * altura}
        elif massa is None:
            if gravidade == 0 or altura == 0:
                raise ValueError("gravidade e altura não podem ser zero")
            return {'massa': energia_potencial / (gravidade * altura)}
        elif altura is None:
            if massa == 0 or gravidade == 0:
                raise ValueError("massa e gravidade não podem ser zero")
            return {'altura': energia_potencial / (massa * gravidade)}
        else:  # gravidade is None
            if massa == 0 or altura == 0:
                raise ValueError("massa e altura não podem ser zero")
            return {'gravidade': energia_potencial / (massa * altura)}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no cálculo da energia potencial: {str(e)}")
def potencia(
    potencia_media: Optional[float] = None,
    trabalho: Optional[float] = None,
    tempo: Optional[float] = None
) -> Dict[str, float]:
    try:
        valores = {
            'potencia_media': potencia_media,
            'trabalho': trabalho,
            'tempo': tempo
        }
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos")
            
        if potencia_media is None:
            if tempo == 0:
                raise ValueError("tempo não pode ser zero")
            return {'potencia_media': trabalho / tempo}
        elif trabalho is None:
            return {'trabalho': potencia_media * tempo}
        else:  # tempo is None
            if potencia_media == 0:
                raise ValueError("potência não pode ser zero")
            return {'tempo': trabalho / potencia_media}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no cálculo da potência: {str(e)}")
def pressao(
    pressao: Optional[float] = None,
    forca: Optional[float] = None,
    area: Optional[float] = None
) -> Dict[str, float]:
    try:
        valores = {
            'pressao': pressao,
            'forca': forca,
            'area': area
        }
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos")
            
        if pressao is None:
            if area == 0:
                raise ValueError("área não pode ser zero")
            return {'pressao': forca / area}
        elif forca is None:
            return {'forca': pressao * area}
        else:  # area is None
            if pressao == 0:
                raise ValueError("pressão não pode ser zero")
            return {'area': forca / pressao}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no cálculo da pressão: {str(e)}")
def equacao_dos_espelhos_e_lentes(
    distancia_focal: Optional[float] = None,
    distancia_objeto: Optional[float] = None,
    distancia_imagem: Optional[float] = None
) -> Dict[str, float]:
    try:
        valores = {
            'distancia_focal': distancia_focal,
            'distancia_objeto': distancia_objeto,
            'distancia_imagem': distancia_imagem
        }
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos")
            
        if distancia_focal is None:
            if distancia_objeto == 0 or distancia_imagem == 0:
                raise ValueError("Distâncias não podem ser zero")
            return {'distancia_focal': 1 / (1/distancia_objeto + 1/distancia_imagem)}
        elif distancia_objeto is None:
            if distancia_focal == 0 or distancia_imagem == 0:
                raise ValueError("Distâncias não podem ser zero")
            return {'distancia_objeto': 1 / (1/distancia_focal - 1/distancia_imagem)}
        else:  # distancia_imagem is None
            if distancia_focal == 0 or distancia_objeto == 0:
                raise ValueError("Distâncias não podem ser zero")
            return {'distancia_imagem': 1 / (1/distancia_focal - 1/distancia_objeto)}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na equação dos espelhos: {str(e)}")
def formula_do_aumento_da_imagem(
    altura_imagem: Optional[float] = None,
    altura_objeto: Optional[float] = None,
    distancia_objeto: Optional[float] = None,
    distancia_imagem: Optional[float] = None
) -> Dict[str, float]:
    try:
        valores = {
            'altura_imagem': altura_imagem,
            'altura_objeto': altura_objeto,
            'distancia_objeto': distancia_objeto,
            'distancia_imagem': distancia_imagem
        }
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos")
            
        # Cálculo do aumento (A = -p'/p = i/o)
        if altura_imagem is None:
            return {'altura_imagem': (altura_objeto * -distancia_imagem) / distancia_objeto}
        elif altura_objeto is None:
            return {'altura_objeto': (altura_imagem * distancia_objeto) / -distancia_imagem}
        elif distancia_objeto is None:
            return {'distancia_objeto': (altura_imagem * -distancia_imagem) / altura_objeto}
        else:  # distancia_imagem is None
            return {'distancia_imagem': (altura_objeto * distancia_objeto) / -altura_imagem}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no cálculo do aumento: {str(e)}")
def velocidade_onda(
    velocidade: Optional[float] = None,
    frequencia: Optional[float] = None,
    comprimento_onda: Optional[float] = None
) -> Dict[str, float]:
    try:
        valores = {
            'velocidade': velocidade,
            'frequencia': frequencia,
            'comprimento_onda': comprimento_onda
        }
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos")
            
        if velocidade is None:
            return {'velocidade': frequencia * comprimento_onda}
        elif frequencia is None:
            if comprimento_onda == 0:
                raise ValueError("Comprimento de onda não pode ser zero")
            return {'frequencia': velocidade / comprimento_onda}
        else:  # comprimento_onda is None
            if frequencia == 0:
                raise ValueError("Frequência não pode ser zero")
            return {'comprimento_onda': velocidade / frequencia}
            
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no cálculo da velocidade da onda: {str(e)}")

def empuxo(empuxo: Optional[float] = None,
           densidade: Optional[float] = None,
           volume: Optional[float] = None,
           gravidade: Optional[float] = None) -> Dict[str, float]:
    try:
        valores = {
            'empuxo': empuxo,
            'densidade': densidade,
            'volume': volume,
            'gravidade': gravidade
        }
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos")
        
        if empuxo is None:
            if any(v is None for v in [densidade, volume, gravidade]):
                raise ValueError("Valores insuficientes para calcular empuxo")
            return {'empuxo': densidade * volume * gravidade}
        
        elif densidade is None:
            if any(v is None for v in [volume, gravidade]):
                raise ValueError("Valores insuficientes para calcular densidade")
            if volume == 0 or gravidade == 0:
                raise ValueError("Volume e gravidade não podem ser zero")
            return {'densidade': empuxo / (volume * gravidade)}
        
        elif volume is None:
            if any(v is None for v in [densidade, gravidade]):
                raise ValueError("Valores insuficientes para calcular volume")
            if densidade == 0 or gravidade == 0:
                raise ValueError("Densidade e gravidade não podem ser zero")
            return {'volume': empuxo / (densidade * gravidade)}
        
        else:  # gravidade is None
            if any(v is None for v in [densidade, volume]):
                raise ValueError("Valores insuficientes para calcular gravidade")
            if densidade == 0 or volume == 0:
                raise ValueError("Densidade e volume não podem ser zero")
            return {'gravidade': empuxo / (densidade * volume)}
    
    except (TypeError, ValueError, ZeroDivisionError) as e:
        raise ValueError(f"Erro ao calcular empuxo: {str(e)}")


def dilatacao_linear(dilatacao_linear: Optional[float] = None,
                     comprimento_final: Optional[float] = None,
                     comprimento_inicial: Optional[float] = None,
                     coeficiente: Optional[float] = None,
                     variacao_de_temperatura: Optional[float] = None) -> Dict[str, float]:
    try:
        valores = {
            'dilatacao_linear': dilatacao_linear,
            'comprimento_final': comprimento_final,
            'comprimento_inicial': comprimento_inicial,
            'coeficiente': coeficiente,
            'variacao_de_temperatura': variacao_de_temperatura
        }
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente quatro valores devem ser fornecidos")
        
        if dilatacao_linear is None:
            # ΔL = L0 * α * ΔT
            required = ['comprimento_inicial', 'coeficiente', 'variacao_de_temperatura']
            if any(valores[k] is None for k in required):
                raise ValueError("Valores insuficientes para calcular dilatação linear")
            L0 = comprimento_inicial
            α = coeficiente
            ΔT = variacao_de_temperatura
            return {'dilatacao_linear': L0 * α * ΔT}
        
        elif comprimento_final is None:
            # L = L0 * (1 + αΔT)
            required = ['comprimento_inicial', 'coeficiente', 'variacao_de_temperatura']
            if any(valores[k] is None for k in required):
                raise ValueError("Valores insuficientes para calcular comprimento final")
            L0 = comprimento_inicial
            α = coeficiente
            ΔT = variacao_de_temperatura
            return {'comprimento_final': L0 * (1 + α * ΔT)}
        
        elif comprimento_inicial is None:
            # L0 pode ser calculado de duas formas
            if dilatacao_linear is not None and coeficiente is not None and variacao_de_temperatura is not None:
                # L0 = ΔL / (αΔT)
                ΔL = dilatacao_linear
                α = coeficiente
                ΔT = variacao_de_temperatura
                if α == 0 or ΔT == 0:
                    raise ValueError("Coeficiente ou variação de temperatura não podem ser zero")
                return {'comprimento_inicial': ΔL / (α * ΔT)}
            elif comprimento_final is not None and coeficiente is not None and variacao_de_temperatura is not None:
                # L0 = L / (1 + αΔT)
                L = comprimento_final
                α = coeficiente
                ΔT = variacao_de_temperatura
                denominator = 1 + α * ΔT
                if denominator == 0:
                    raise ValueError("Denominador não pode ser zero")
                return {'comprimento_inicial': L / denominator}
            else:
                raise ValueError("Combinação inválida de parâmetros")
        
        elif coeficiente is None:
            # α = ΔL / (L0 * ΔT)
            required = ['dilatacao_linear', 'comprimento_inicial', 'variacao_de_temperatura']
            if any(valores[k] is None for k in required):
                raise ValueError("Valores insuficientes para calcular coeficiente")
            ΔL = dilatacao_linear
            L0 = comprimento_inicial
            ΔT = variacao_de_temperatura
            if L0 == 0 or ΔT == 0:
                raise ValueError("Comprimento inicial ou variação de temperatura não podem ser zero")
            return {'coeficiente': ΔL / (L0 * ΔT)}
        
        else:  # ΔT is None
            # ΔT = ΔL / (L0 * α)
            required = ['dilatacao_linear', 'comprimento_inicial', 'coeficiente']
            if any(valores[k] is None for k in required):
                raise ValueError("Valores insuficientes para calcular variação de temperatura")
            ΔL = dilatacao_linear
            L0 = comprimento_inicial
            α = coeficiente
            if L0 == 0 or α == 0:
                raise ValueError("Comprimento inicial ou coeficiente não podem ser zero")
            return {'variacao_de_temperatura': ΔL / (L0 * α)}
    
    except (TypeError, ValueError, ZeroDivisionError) as e:
        raise ValueError(f"Erro ao calcular dilatação linear: {str(e)}")