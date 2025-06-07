from typing import Dict, List, Optional
import re
import json
import os
from datetime import datetime

class CalcLabChatbot:
    def __init__(self):
        self.calculators = {
            'fisica': {
                'velocidade_media': ['velocidade', 'deslocamento', 'tempo'],
                'movimento_uniforme': ['posição', 'velocidade', 'tempo'],
                'movimento_uniformemente_variado': ['posição', 'velocidade', 'aceleração', 'tempo'],
                'forca_peso': ['massa', 'gravidade'],
                'energia_cinetica': ['massa', 'velocidade'],
                'energia_potencial': ['massa', 'altura', 'gravidade'],
                'potencia': ['trabalho', 'tempo'],
                'pressao': ['força', 'área'],
                'lei_ohm': ['tensão', 'corrente', 'resistência']
            },
            'quimica': {
                'concentracao': ['massa', 'volume', 'massa_molar'],
                'ph': ['concentração', 'h+'],
                'diluicao': ['concentração_inicial', 'volume_inicial', 'volume_final'],
                'gases': ['pressão', 'volume', 'temperatura', 'mols']
            },
            'matematica': {
                'equacao_segundo_grau': ['a', 'b', 'c'],
                'trigonometria': ['ângulo', 'cateto', 'hipotenusa'],
                'logaritmo': ['base', 'número'],
                'matriz': ['dimensão', 'elementos']
            }
        }
        
        self.keywords = {
            'velocidade': ['velocidade', 'rapidez', 'movimento', 'deslocamento'],
            'força': ['força', 'peso', 'massa', 'gravidade'],
            'energia': ['energia', 'trabalho', 'potência'],
            'pressão': ['pressão', 'área', 'força'],
            'eletricidade': ['corrente', 'tensão', 'resistência', 'voltagem'],
            'química': ['concentração', 'ph', 'ácido', 'base', 'molar'],
            'matemática': ['equação', 'trigonometria', 'logaritmo', 'matriz']
        }

    def analyze_input(self, text: str) -> Dict:
        """Analisa o texto de entrada e retorna recomendações"""
        text = text.lower()
        
        # Identifica palavras-chave
        found_keywords = []
        for category, words in self.keywords.items():
            for word in words:
                if word in text:
                    found_keywords.append(category)
                    break
        
        # Encontra calculadoras relevantes
        relevant_calculators = []
        for category, calcs in self.calculators.items():
            for calc_name, params in calcs.items():
                if any(keyword in text for keyword in params):
                    relevant_calculators.append({
                        'category': category,
                        'name': calc_name,
                        'params': params
                    })
        
        return {
            'keywords': found_keywords,
            'calculators': relevant_calculators
        }

    def generate_response(self, text: str, user_name: Optional[str] = None) -> str:
        """Gera uma resposta baseada na análise do texto"""
        analysis = self.analyze_input(text)
        
        if not analysis['calculators']:
            return f"{user_name + ', ' if user_name else ''}Desculpe, não consegui identificar qual calculadora você precisa. " \
                   f"Você poderia me dar mais detalhes sobre o problema? Por exemplo, quais valores você tem disponível?"
        
        # Gera resposta personalizada
        response = f"{user_name + ', ' if user_name else ''}Baseado no seu problema, "
        
        if len(analysis['calculators']) == 1:
            calc = analysis['calculators'][0]
            response += f"recomendo usar a calculadora de {calc['name'].replace('_', ' ')}. "
            response += f"Você precisará dos seguintes valores: {', '.join(calc['params'])}. "
        else:
            response += "existem algumas opções que podem ajudar:\n\n"
            for calc in analysis['calculators']:
                response += f"- {calc['name'].replace('_', ' ')}: precisa de {', '.join(calc['params'])}\n"
            response += "\nQual dessas opções melhor se encaixa no seu problema?"
        
        return response

    def save_conversation(self, user_id: str, message: str, response: str):
        """Salva a conversa no histórico"""
        history_file = 'chat_history.json'
        
        # Carrega histórico existente
        if os.path.exists(history_file):
            with open(history_file, 'r', encoding='utf-8') as f:
                history = json.load(f)
        else:
            history = {}
        
        # Adiciona nova conversa
        if user_id not in history:
            history[user_id] = []
        
        history[user_id].append({
            'timestamp': datetime.now().isoformat(),
            'message': message,
            'response': response
        })
        
        # Salva histórico
        with open(history_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)

# Instância global do chatbot
chatbot = CalcLabChatbot() 