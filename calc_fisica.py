from typing import Dict, List, Union, Optional, Tuple
import math
def velocidade_media(deslocamento: Optional[float] = None, 
                  tempo: Optional[float] = None, 
                  velocidade_media: Optional[float] = None) -> Dict[str, str]:
    try:
        valores = {'deslocamento': deslocamento, 'tempo': tempo, 'velocidade_media': velocidade_media}
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
            
        if deslocamento is None:
            if tempo is None or velocidade_media is None:
                raise ValueError("Tempo e velocidade média devem ser fornecidos para calcular o deslocamento.")
            deslocamento = velocidade_media * tempo
            return {'deslocamento': f"{deslocamento:.2f} m"}
        elif tempo is None:
            if deslocamento is None or velocidade_media is None:
                raise ValueError("Deslocamento e velocidade média devem ser fornecidos para calcular o tempo.")
            if velocidade_media == 0:
                raise ValueError("Velocidade média não pode ser zero para calcular o tempo.")
            tempo = deslocamento / velocidade_media
            return {'tempo': f"{tempo:.2f} s"}
        else:  # velocidade_media is None
            if deslocamento is None or tempo is None:
                raise ValueError("Deslocamento e tempo devem ser fornecidos para calcular a velocidade média.")
            if tempo == 0:
                raise ValueError("Tempo não pode ser zero para calcular a velocidade média.")
            velocidade_media = deslocamento / tempo
            return {'velocidade_media': f"{velocidade_media:.2f} m/s"}
            
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular velocidade média: {str(e)}")

def movimento_uniforme(posicao_final: Optional[float] = None,
                    posicao_inicial: Optional[float] = None,
                    velocidade: Optional[float] = None,
                    tempo: Optional[float] = None) -> Dict[str, str]:
    try:
        valores = {
            'posicao_final': posicao_final,
            'posicao_inicial': posicao_inicial,
            'velocidade': velocidade,
            'tempo': tempo
        }
        none_count = sum(1 for v in valores.values() if v is None)
        
        if none_count != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")
            
        if posicao_final is None:
            posicao_final = posicao_inicial + velocidade * tempo
            return {'posicao_final': f"{posicao_final:.2f} m"}
        elif posicao_inicial is None:
            posicao_inicial = posicao_final - velocidade * tempo
            return {'posicao_inicial': f"{posicao_inicial:.2f} m"}
        elif velocidade is None:
            if tempo == 0:
                raise ValueError("Tempo não pode ser zero para calcular a velocidade.")
            velocidade = (posicao_final - posicao_inicial) / tempo
            return {'velocidade': f"{velocidade:.2f} m/s"}
        else:  # tempo is None
            if velocidade == 0:
                raise ValueError("Velocidade não pode ser zero para calcular o tempo.")
            tempo = (posicao_final - posicao_inicial) / velocidade
            return {'tempo': f"{tempo:.2f} s"}
            
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro ao calcular movimento uniforme: {str(e)}")

def movimento_uniformemente_variado(
    posicao_final: Optional[float] = None,
    posicao_inicial: Optional[float] = None,
    velocidade_inicial: Optional[float] = None,
    tempo: Optional[float] = None,
    aceleracao: Optional[float] = None
) -> Dict[str, str]:
    
    valores = {
        'posicao_final': posicao_final,
        'posicao_inicial': posicao_inicial,
        'velocidade_inicial': velocidade_inicial,
        'tempo': tempo,
        'aceleracao': aceleracao
    }
    
    none_count = sum(1 for v in valores.values() if v is None)
    if none_count != 1:
        raise ValueError("Exatamente quatro valores devem ser fornecidos para calcular o quinto.")

    try:
        if posicao_final is None:
            posicao_final = posicao_inicial + velocidade_inicial * tempo + (aceleracao * tempo**2)/2
            return {'posicao_final': f"{posicao_final:.2f} m"}
        elif posicao_inicial is None:
            posicao_inicial = posicao_final - velocidade_inicial * tempo - (aceleracao * tempo**2)/2
            return {'posicao_inicial': f"{posicao_inicial:.2f} m"}
        elif velocidade_inicial is None:
            if tempo == 0:
                raise ValueError("Tempo não pode ser zero para calcular a velocidade inicial.")
            velocidade_inicial = (posicao_final - posicao_inicial - (aceleracao * tempo**2)/2) / tempo
            return {'velocidade_inicial': f"{velocidade_inicial:.2f} m/s"}
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
                return {'tempo': f"{tempo:.2f} s"}

            delta = b**2 - 4*a*c
            if delta < 0:
                raise ValueError("Não há solução real para o tempo com os valores fornecidos.")
            
            tempo1 = (-b + math.sqrt(delta))/(2*a)
            tempo2 = (-b - math.sqrt(delta))/(2*a)
            
            # Retorna o tempo positivo, se houver
            if tempo1 >= 0 and tempo2 >= 0:
                return {'tempo': f"{min(tempo1, tempo2):.2f} s"} # Retorna o menor tempo positivo
            elif tempo1 >= 0:
                return {'tempo': f"{tempo1:.2f} s"}
            elif tempo2 >= 0:
                return {'tempo': f"{tempo2:.2f} s"}
            else:
                raise ValueError("Não há tempos positivos válidos com os valores fornecidos.")
        else:
            if tempo == 0:
                raise ValueError("Tempo não pode ser zero para calcular a aceleração.")
            aceleracao = 2*(posicao_final - posicao_inicial - velocidade_inicial * tempo)/tempo**2
            return {'aceleracao': f"{aceleracao:.2f} m/s²"}

    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no MUV: {str(e)}")
def equacao_torricelli(
    velocidade_final: Optional[float] = None,
    velocidade_inicial: Optional[float] = None,
    aceleracao: Optional[float] = None,
    deslocamento: Optional[float] = None) -> Dict[str, str]:
    
    valores = {
        'velocidade_final': velocidade_final,
        'velocidade_inicial': velocidade_inicial,
        'aceleracao': aceleracao,
        'deslocamento': deslocamento
    }
    
    none_count = sum(1 for v in valores.values() if v is None)
    if none_count != 1:
        raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")

    try:
        if velocidade_final is None:
            arg = velocidade_inicial**2 + 2 * aceleracao * deslocamento
            if arg < 0:
                raise ValueError("Não é possível ter velocidade final real com os valores fornecidos (raiz de número negativo).")
            velocidade_final = math.sqrt(arg)
            return {'velocidade_final': f"{velocidade_final:.2f} m/s"}
        elif velocidade_inicial is None:
            arg = velocidade_final**2 - 2 * aceleracao * deslocamento
            if arg < 0:
                raise ValueError("Não é possível ter velocidade inicial real com os valores fornecidos (raiz de número negativo).")
            velocidade_inicial = math.sqrt(arg)
            return {'velocidade_inicial': f"{velocidade_inicial:.2f} m/s"}
        elif aceleracao is None:
            den = (2 * deslocamento)
            if den == 0:
                raise ValueError("Deslocamento não pode ser zero para calcular a aceleração.")
            aceleracao = (velocidade_final**2 - velocidade_inicial**2)/den
            return {'aceleracao': f"{aceleracao:.2f} m/s²"}
        else:
            den = (2 * aceleracao)
            if den == 0:
                raise ValueError("Aceleração não pode ser zero para calcular o deslocamento.")
            deslocamento = (velocidade_final**2 - velocidade_inicial**2)/den
            return {'deslocamento': f"{deslocamento:.2f} m"}

    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Equação de Torricelli: {str(e)}")

def principio_fundamental_dinamica(
    forca: Optional[float] = None,
    massa: Optional[float] = None,
    aceleracao: Optional[float] = None
) -> Dict[str, str]:
    
    valores = {'forca': forca, 'massa': massa, 'aceleracao': aceleracao}
    none_count = sum(1 for v in valores.values() if v is None)
    
    if none_count != 1:
        raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")

    try:
        if forca is None:
            forca = massa * aceleracao
            return {'forca': f"{forca:.2f} N"}
        elif massa is None:
            if aceleracao == 0:
                raise ValueError("Aceleração não pode ser zero para calcular a massa.")
            massa = forca / aceleracao
            return {'massa': f"{massa:.2f} kg"}
        else: # aceleracao is None
            if massa == 0:
                raise ValueError("Massa não pode ser zero para calcular a aceleração.")
            aceleracao = forca / massa
            return {'aceleracao': f"{aceleracao:.2f} m/s²"}

    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro no Princípio Fundamental: {str(e)}")
def forca_peso(
    forca_peso: Optional[float] = None,
    massa: Optional[float] = None,
    gravidade: Optional[float] = None
) -> Dict[str, str]:
    
    valores = {'forca_peso': forca_peso, 'massa': massa, 'gravidade': gravidade}
    none_count = sum(1 for v in valores.values() if v is None)
    
    if none_count != 1:
        raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")

    try:
        if forca_peso is None:
            forca_peso = massa * gravidade
            return {'forca_peso': f"{forca_peso:.2f} N"}
        elif massa is None:
            if gravidade == 0:
                raise ValueError("Gravidade não pode ser zero para calcular a massa.")
            massa = forca_peso / gravidade
            return {'massa': f"{massa:.2f} kg"}
        else: # gravidade is None
            if massa == 0:
                raise ValueError("Massa não pode ser zero para calcular a gravidade.")
            gravidade = forca_peso / massa
            return {'gravidade': f"{gravidade:.2f} m/s²"}

    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Força Peso: {str(e)}")
def forca_atrito(
    forca_atrito: Optional[float] = None,
    coeficiente: Optional[float] = None,
    normal: Optional[float] = None
) -> Dict[str, str]:
    
    valores = {'forca_atrito': forca_atrito, 'coeficiente': coeficiente, 'normal': normal}
    none_count = sum(1 for v in valores.values() if v is None)
    
    if none_count != 1:
        raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")

    try:
        if forca_atrito is None:
            forca_atrito = coeficiente * normal
            return {'forca_atrito': f"{forca_atrito:.2f} N"}
        elif coeficiente is None:
            if normal == 0:
                raise ValueError("Força normal não pode ser zero para calcular o coeficiente.")
            coeficiente = forca_atrito / normal
            return {'coeficiente': f"{coeficiente:.2f} (adimensional)"}
        else: # normal is None
            if coeficiente == 0:
                raise ValueError("Coeficiente não pode ser zero para calcular a força normal.")
            normal = forca_atrito / coeficiente
            return {'normal': f"{normal:.2f} N"}

    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Erro na Força de Atrito: {str(e)}")
def trabalho_forca_constante(
    trabalho: Optional[float] = None,
    forca: Optional[float] = None,
    deslocamento: Optional[float] = None,
    angulo: Optional[float] = None
) -> Dict[str, str]:
    try:
        valores = {'trabalho': trabalho, 'forca': forca, 'deslocamento': deslocamento, 'angulo': angulo}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")
        
        if trabalho is None:
            trabalho = forca * deslocamento * math.cos(math.radians(angulo))
            return {'trabalho': f"{trabalho:.2f} J"}
        elif forca is None:
            den = (deslocamento * math.cos(math.radians(angulo)))
            if den == 0:
                raise ValueError("Denominador não pode ser zero para calcular a força.")
            forca = trabalho / den
            return {'forca': f"{forca:.2f} N"}
        elif deslocamento is None:
            den = (forca * math.cos(math.radians(angulo)))
            if den == 0:
                raise ValueError("Denominador não pode ser zero para calcular o deslocamento.")
            deslocamento = trabalho / den
            return {'deslocamento': f"{deslocamento:.2f} m"}
        else: # angulo is None
            den = (forca * deslocamento)
            if den == 0:
                raise ValueError("Denominador não pode ser zero para calcular o ângulo.")
            cos_angulo = trabalho / den
            if not -1 <= cos_angulo <= 1:
                raise ValueError("Não é possível calcular o ângulo real com os valores fornecidos.")
            angulo = math.degrees(math.acos(cos_angulo))
            return {'angulo': f"{angulo:.2f} °"}
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro no cálculo do Trabalho de Força Constante: {str(e)}")
def energia_cinetica(
    energia_cinetica: Optional[float] = None,
    massa: Optional[float] = None,
    velocidade: Optional[float] = None
) -> Dict[str, str]:
    try:
        valores = {'energia_cinetica': energia_cinetica, 'massa': massa, 'velocidade': velocidade}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
        
        if energia_cinetica is None:
            energia_cinetica = (massa * velocidade**2) / 2
            return {'energia_cinetica': f"{energia_cinetica:.2f} J"}
        elif massa is None:
            den = (velocidade**2)
            if den == 0:
                raise ValueError("Velocidade não pode ser zero para calcular a massa.")
            massa = (2 * energia_cinetica) / den
            return {'massa': f"{massa:.2f} kg"}
        else: # velocidade is None
            arg = (2 * energia_cinetica) / massa
            if arg < 0:
                raise ValueError("Não é possível ter velocidade real com os valores fornecidos (raiz de número negativo).")
            velocidade = math.sqrt(arg)
            return {'velocidade': f"{velocidade:.2f} m/s"}
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro no cálculo da Energia Cinética: {str(e)}")
def pressao_hidrostatica(
    pressao: Optional[float] = None,
    densidade: Optional[float] = None,
    gravidade: Optional[float] = None,
    altura: Optional[float] = None
) -> Dict[str, str]:
    try:
        valores = {'pressao': pressao, 'densidade': densidade, 'gravidade': gravidade, 'altura': altura}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")

        if pressao is None:
            pressao = densidade * gravidade * altura
            return {'pressao': f"{pressao:.2f} Pa"}
        elif densidade is None:
            den = (gravidade * altura)
            if den == 0:
                raise ValueError("Gravidade ou altura não podem ser zero para calcular a densidade.")
            densidade = pressao / den
            return {'densidade': f"{densidade:.2f} kg/m³"}
        elif gravidade is None:
            den = (densidade * altura)
            if den == 0:
                raise ValueError("Densidade ou altura não podem ser zero para calcular a gravidade.")
            gravidade = pressao / den
            return {'gravidade': f"{gravidade:.2f} m/s²"}
        else: # altura is None
            den = (densidade * gravidade)
            if den == 0:
                raise ValueError("Densidade ou gravidade não podem ser zero para calcular a altura.")
            altura = pressao / den
            return {'altura': f"{altura:.2f} m"}
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro no cálculo da Pressão Hidrostática: {str(e)}")
def primeira_lei_termodinamica(
    variacao_interna: Optional[float] = None,
    calor: Optional[float] = None,
    trabalho: Optional[float] = None
) -> Dict[str, str]:
    try:
        valores = {'variacao_interna': variacao_interna, 'calor': calor, 'trabalho': trabalho}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")

        if variacao_interna is None:
            variacao_interna = calor - trabalho
            return {'variacao_interna': f"{variacao_interna:.2f} J"}
        elif calor is None:
            calor = variacao_interna + trabalho
            return {'calor': f"{calor:.2f} J"}
        else: # trabalho is None
            trabalho = calor - variacao_interna
            return {'trabalho': f"{trabalho:.2f} J"}
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
def potencia_eletrica(potencia: Optional[float] = None, 
                      tensao: Optional[float] = None, 
                      corrente: Optional[float] = None) -> Dict[str, str]:
    try:
        valores = {'potencia': potencia, 'tensao': tensao, 'corrente': corrente}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")

        if potencia is None:
            potencia = tensao * corrente
            return {'potencia': f"{potencia:.2f} W"}
        elif tensao is None:
            if corrente == 0:
                raise ValueError("Corrente não pode ser zero para calcular a tensão.")
            tensao = potencia / corrente
            return {'tensao': f"{tensao:.2f} V"}
        else: # corrente is None
            if tensao == 0:
                raise ValueError("Tensão não pode ser zero para calcular a corrente.")
            corrente = potencia / tensao
            return {'corrente': f"{corrente:.2f} A"}
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro na Potência Elétrica: {str(e)}")
def forca_entre_cargas_eletricas(forca: Optional[float] = None,
                                 k: Optional[float] = None,
                                 q1: Optional[float] = None,
                                 q2: Optional[float] = None,
                                 d: Optional[float] = None) -> Dict[str, str]:
    try:
        valores = {'forca': forca, 'k': k, 'q1': q1, 'q2': q2, 'd': d}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente quatro valores devem ser fornecidos para calcular o quinto.")

        # Constante eletrostática do vácuo k = 8.99 x 10^9 N·m²/C²
        k_val = k if k is not None else 8.99e9 # Usar k fornecido ou padrão

        if forca is None:
            if d == 0:
                raise ValueError("Distância não pode ser zero para calcular a força.")
            forca = k_val * abs(q1 * q2) / (d**2)
            return {'forca': f"{forca:.2e} N"}
        elif k is None:
            if q1 == 0 or q2 == 0:
                raise ValueError("As cargas elétricas não podem ser zero para calcular a constante k.")
            k = forca * (d**2) / (q1 * q2)
            return {'k': f"{k:.2e} N·m²/C²"}
        elif q1 is None:
            if k_val == 0 or d == 0 or q2 == 0:
                raise ValueError("Constante k, distância ou carga q2 não podem ser zero para calcular a carga q1.")
            q1 = forca * (d**2) / (k_val * q2)
            return {'q1': f"{q1:.2e} C"}
        elif q2 is None:
            if k_val == 0 or d == 0 or q1 == 0:
                raise ValueError("Constante k, distância ou carga q1 não podem ser zero para calcular a carga q2.")
            q2 = forca * (d**2) / (k_val * q1)
            return {'q2': f"{q2:.2e} C"}
        else: # d is None
            if k_val == 0 or q1 == 0 or q2 == 0 or forca == 0:
                raise ValueError("Constante k, cargas ou força não podem ser zero para calcular a distância.")
            arg = (k_val * abs(q1 * q2)) / forca
            if arg < 0:
                raise ValueError("Não é possível ter distância real com os valores fornecidos (raiz de número negativo).")
            d = math.sqrt(arg)
            return {'d': f"{d:.2f} m"}
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro no cálculo da Força entre Cargas Elétricas: {str(e)}")
def energia_potencial_elastica(energia: Optional[float] = None,
                               constante: Optional[float] = None,
                               deformacao: Optional[float] = None) -> Dict[str, str]:
    try:
        valores = {'energia': energia, 'constante': constante, 'deformacao': deformacao}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
        
        if energia is None:
            energia = (constante * deformacao**2) / 2
            return {'energia': f"{energia:.2f} J"}
        elif constante is None:
            den = (deformacao**2)
            if den == 0:
                raise ValueError("Deformação não pode ser zero para calcular a constante elástica.")
            constante = (2 * energia) / den
            return {'constante': f"{constante:.2f} N/m"}
        else: # deformacao is None
            if constante == 0:
                raise ValueError("Constante elástica não pode ser zero para calcular a deformação.")
            arg = (2 * energia) / constante
            if arg < 0:
                raise ValueError("Não é possível ter deformação real com os valores fornecidos (raiz de número negativo).")
            deformacao = math.sqrt(arg)
            return {'deformacao': f"{deformacao:.2f} m"}
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro no cálculo da Energia Potencial Elástica: {str(e)}")
def energia_mecanica(energia_mec: Optional[float] = None,
                     energia_cinetica: Optional[float] = None,
                     energia_potencial: Optional[float] = None) -> Dict[str, str]:
    try:
        valores = {'energia_mec': energia_mec, 'energia_cinetica': energia_cinetica, 'energia_potencial': energia_potencial}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")
        
        if energia_mec is None:
            energia_mec = energia_cinetica + energia_potencial
            return {'energia_mec': f"{energia_mec:.2f} J"}
        elif energia_cinetica is None:
            energia_cinetica = energia_mec - energia_potencial
            return {'energia_cinetica': f"{energia_cinetica:.2f} J"}
        else: # energia_potencial is None
            energia_potencial = energia_mec - energia_cinetica
            return {'energia_potencial': f"{energia_potencial:.2f} J"}
    except (TypeError, ValueError) as e:
        raise ValueError(f"Erro no cálculo da Energia Mecânica: {str(e)}")
def energia_potencial(
    energia_potencial: Optional[float] = None,
    massa: Optional[float] = None,
    altura: Optional[float] = None,
    gravidade: Optional[float] = None
) -> Dict[str, str]:
    try:
        valores = {'energia_potencial': energia_potencial, 'massa': massa, 'altura': altura, 'gravidade': gravidade}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")

        if energia_potencial is None:
            energia_potencial = massa * gravidade * altura
            return {'energia_potencial': f"{energia_potencial:.2f} J"}
        elif massa is None:
            den = (gravidade * altura)
            if den == 0:
                raise ValueError("Gravidade ou altura não podem ser zero para calcular a massa.")
            massa = energia_potencial / den
            return {'massa': f"{massa:.2f} kg"}
        elif altura is None:
            den = (massa * gravidade)
            if den == 0:
                raise ValueError("Massa ou gravidade não podem ser zero para calcular a altura.")
            altura = energia_potencial / den
            return {'altura': f"{altura:.2f} m"}
        else: # gravidade is None
            den = (massa * altura)
            if den == 0:
                raise ValueError("Massa ou altura não podem ser zero para calcular a gravidade.")
            gravidade = energia_potencial / den
            return {'gravidade': f"{gravidade:.2f} m/s²"}
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro no cálculo da Energia Potencial Gravitacional: {str(e)}")
def potencia(
    potencia_media: Optional[float] = None,
    trabalho: Optional[float] = None,
    tempo: Optional[float] = None
) -> Dict[str, str]:
    try:
        valores = {'potencia_media': potencia_media, 'trabalho': trabalho, 'tempo': tempo}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")

        if potencia_media is None:
            if tempo == 0: 
                raise ValueError("Tempo não pode ser zero para calcular a potência.")
            potencia_media = trabalho / tempo
            return {'potencia_media': f"{potencia_media:.2f} W"}
        elif trabalho is None:
            trabalho = potencia_media * tempo
            return {'trabalho': f"{trabalho:.2f} J"}
        else: # tempo is None
            if potencia_media == 0:
                raise ValueError("Potência média não pode ser zero para calcular o tempo.")
            tempo = trabalho / potencia_media
            return {'tempo': f"{tempo:.2f} s"}
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro no cálculo da Potência: {str(e)}")
def pressao(
    pressao: Optional[float] = None,
    forca: Optional[float] = None,
    area: Optional[float] = None
) -> Dict[str, str]:
    try:
        valores = {'pressao': pressao, 'forca': forca, 'area': area}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente dois valores devem ser fornecidos para calcular o terceiro.")

        if pressao is None:
            if area == 0:
                raise ValueError("Área não pode ser zero para calcular a pressão.")
            pressao = forca / area
            return {'pressao': f"{pressao:.2f} Pa"}
        elif forca is None:
            forca = pressao * area
            return {'forca': f"{forca:.2f} N"}
        else: # area is None
            if pressao == 0:
                raise ValueError("Pressão não pode ser zero para calcular a área.")
            area = forca / pressao
            return {'area': f"{area:.2f} m²"}
    except (TypeError, ZeroDivisionError, ValueError) as e:
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
def empuxo(empuxo: Optional[float] = None,
           densidade: Optional[float] = None,
           volume: Optional[float] = None,
           gravidade: Optional[float] = None) -> Dict[str, str]:
    try:
        valores = {'empuxo': empuxo, 'densidade': densidade, 'volume': volume, 'gravidade': gravidade}
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente três valores devem ser fornecidos para calcular o quarto.")

        if empuxo is None:
            empuxo = densidade * volume * gravidade
            return {'empuxo': f"{empuxo:.2f} N"}
        elif densidade is None:
            den = (volume * gravidade)
            if den == 0:
                raise ValueError("Volume ou gravidade não podem ser zero para calcular a densidade.")
            densidade = empuxo / den
            return {'densidade': f"{densidade:.2f} kg/m³"}
        elif volume is None:
            den = (densidade * gravidade)
            if den == 0:
                raise ValueError("Densidade ou gravidade não podem ser zero para calcular o volume.")
            volume = empuxo / den
            return {'volume': f"{volume:.2f} m³"}
        else: # gravidade is None
            den = (densidade * volume)
            if den == 0:
                raise ValueError("Densidade ou volume não podem ser zero para calcular a gravidade.")
            gravidade = empuxo / den
            return {'gravidade': f"{gravidade:.2f} m/s²"}
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro no cálculo do Empuxo: {str(e)}")
def dilatacao_linear(dilatacao_linear: Optional[float] = None,
                     comprimento_final: Optional[float] = None,
                     comprimento_inicial: Optional[float] = None,
                     coeficiente: Optional[float] = None,
                     variacao_de_temperatura: Optional[float] = None) -> Dict[str, str]:
    try:
        valores = {
            'dilatacao_linear': dilatacao_linear,
            'comprimento_final': comprimento_final,
            'comprimento_inicial': comprimento_inicial,
            'coeficiente': coeficiente,
            'variacao_de_temperatura': variacao_de_temperatura
        }
        if sum(1 for v in valores.values() if v is None) != 1:
            raise ValueError("Exatamente quatro valores devem ser fornecidos para calcular o quinto.")

        # Caso 1: Dilatação linear é o que precisa ser calculado
        if dilatacao_linear is None:
            if comprimento_inicial is None or coeficiente is None or variacao_de_temperatura is None:
                raise ValueError("Comprimento inicial, coeficiente e variação de temperatura devem ser fornecidos para calcular a dilatação linear.")
            dilatacao_linear = comprimento_inicial * coeficiente * variacao_de_temperatura
            return {'dilatacao_linear': f"{dilatacao_linear:.2e} m"}

        # Caso 2: Comprimento final é o que precisa ser calculado (Delta L = Lf - Li)
        elif comprimento_final is None:
            if comprimento_inicial is None or coeficiente is None or variacao_de_temperatura is None:
                raise ValueError("Comprimento inicial, coeficiente e variação de temperatura devem ser fornecidos para calcular o comprimento final.")
            # Se dilatacao_linear não foi fornecida, calcule primeiro
            if dilatacao_linear is None:
                dilatacao_linear_calc = comprimento_inicial * coeficiente * variacao_de_temperatura
            else:
                dilatacao_linear_calc = dilatacao_linear
            comprimento_final = comprimento_inicial + dilatacao_linear_calc
            return {'comprimento_final': f"{comprimento_final:.2f} m"}
        
        # Caso 3: Comprimento inicial é o que precisa ser calculado (Delta L = Lf - Li)
        elif comprimento_inicial is None:
            if comprimento_final is None or coeficiente is None or variacao_de_temperatura is None:
                raise ValueError("Comprimento final, coeficiente e variação de temperatura devem ser fornecidos para calcular o comprimento inicial.")
            # Se dilatacao_linear não foi fornecida, calcule primeiro
            if dilatacao_linear is None:
                dilatacao_linear_calc = comprimento_final - (comprimento_final * coeficiente * variacao_de_temperatura)
            else:
                dilatacao_linear_calc = dilatacao_linear
            comprimento_inicial = comprimento_final - dilatacao_linear_calc
            return {'comprimento_inicial': f"{comprimento_inicial:.2f} m"}

        # Casos para as outras variáveis (coeficiente, variacao_de_temperatura)
        elif coeficiente is None:
            den = (comprimento_inicial * variacao_de_temperatura)
            if den == 0:
                raise ValueError("Comprimento inicial ou variação de temperatura não podem ser zero para calcular o coeficiente.")
            coeficiente = dilatacao_linear / den
            return {'coeficiente': f"{coeficiente:.2e} /°C"}
        else: # variacao_de_temperatura is None
            den = (comprimento_inicial * coeficiente)
            if den == 0:
                raise ValueError("Comprimento inicial ou coeficiente não podem ser zero para calcular a variação de temperatura.")
            variacao_de_temperatura = dilatacao_linear / den
            return {'variacao_de_temperatura': f"{variacao_de_temperatura:.2f} °C"}

    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise ValueError(f"Erro no cálculo da Dilatação Linear: {str(e)}")