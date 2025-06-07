from typing import Dict, List, Optional
import re
import json
import os
from datetime import datetime
import openai
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configuração da API do OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

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

    def generate_ai_response(self, text: str, user_name: Optional[str] = None) -> str:
        """Gera uma resposta usando a API do ChatGPT"""
        try:
            # Análise inicial do texto
            analysis = self.analyze_input(text)
            
            # Prepara o contexto para o ChatGPT
            context = f"""Você é um assistente especializado em física, química e matemática.
            Sua função é ajudar os usuários a escolher a calculadora correta do CalcLab.
            
            Calculadoras disponíveis:
            {json.dumps(self.calculators, indent=2, ensure_ascii=False)}
            
            Análise da pergunta do usuário:
            Palavras-chave encontradas: {', '.join(analysis['keywords'])}
            Calculadoras relevantes: {[calc['name'] for calc in analysis['calculators']]}
            
            Usuário: {text}
            
            Responda de forma amigável e profissional, explicando qual calculadora usar e por quê.
            Se precisar de mais informações, peça gentilmente.
            """

            # Chama a API do ChatGPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": text}
                ],
                temperature=0.7,
                max_tokens=500
            )

            # Processa a resposta
            ai_response = response.choices[0].message.content.strip()
            
            # Personaliza a resposta com o nome do usuário
            if user_name:
                ai_response = f"{user_name}, {ai_response[0].lower()}{ai_response[1:]}"
            
            return ai_response

        except Exception as e:
            print(f"Erro ao gerar resposta: {str(e)}")
            return "Desculpe, tive um problema ao processar sua pergunta. Pode tentar novamente?"

    def generate_response(self, text: str, user_name: Optional[str] = None) -> str:
        """Gera uma resposta baseada na análise do texto"""
        return self.generate_ai_response(text, user_name)

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