"""
Configurações do CalcLab.
"""

import os
from datetime import timedelta

# Configurações básicas
SITE_NAME = "CalcLab"
SITE_DESCRIPTION = "Calculadora científica online para Matemática, Física e Química"
SITE_URL = "http://localhost:5000"

# Configurações do Flask
# SECRET_KEY = os.urandom(24) # Removido para evitar que a chave mude a cada reinício
PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

# Configurações de email
MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True').lower() == 'true'
MAIL_USERNAME = os.getenv('MAIL_USERNAME', '')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', '')
MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', '')

# Configurações de logging
LOG_LEVEL = "INFO"
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = "app.log"

# Configurações de cache
CACHE_TYPE = 'SimpleCache'
CACHE_DEFAULT_TIMEOUT = 300

# Configurações de segurança
SESSION_COOKIE_SECURE = True
REMEMBER_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
REMEMBER_COOKIE_HTTPONLY = True

# Configurações de upload
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
UPLOAD_FOLDER = os.path.join('static', 'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Configurações de API
API_RATE_LIMIT = '100 per minute'
API_RATE_LIMIT_STORAGE_URL = 'memory://'

# Configurações de banco de dados
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///calclab.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configurações de tema
THEME = {
    'PRIMARY_COLOR': '#ff1744',  # Azul mais vibrante
    'SECONDARY_COLOR': '#455a64',  # Cinza azulado
    'FONT_FAMILY': "'Poppins', sans-serif",  # Fonte mais moderna
    'DARK_MODE': False,
    'ACCENT_COLOR': '#00c853',  # Verde para destaques
    'ERROR_COLOR': '#ff1744',  # Vermelho para erros
    'SUCCESS_COLOR': '#00c853',  # Verde para sucesso
    'WARNING_COLOR': '#ffc400',  # Amarelo para avisos
    'INFO_COLOR': '#ff1744',  # Azul claro para informações
    'BORDER_RADIUS': '8px',  # Bordas mais arredondadas
    'SHADOW': '0 4px 6px rgba(0, 0, 0, 0.1)'  # Sombra suave
}

# Configurações de contato
CONTACT = {
    'email': os.getenv('CONTACT_EMAIL', 'contato@calclab.com'),
    'phone': os.getenv('CONTACT_PHONE', '+55 38 98824-8721'),
    'whatsapp': os.getenv('CONTACT_WHATSAPP', '+55 3 98824-8721'),
    'telegram': os.getenv('CONTACT_TELEGRAM', '@calclab')
}

# Configurações de redes sociais
SOCIAL_MEDIA = {
    'facebook': os.getenv('FACEBOOK_URL', 'https://facebook.com/calclab'),
    'twitter': os.getenv('TWITTER_URL', 'https://twitter.com/calclab'),
    'instagram': os.getenv('INSTAGRAM_URL', 'https://instagram.com/calclab'),
    'linkedin': os.getenv('LINKEDIN_URL', 'https://linkedin.com/company/calclab'),
    'github': os.getenv('GITHUB_URL', 'https://github.com/calclab')
}

# Configurações de calculadoras
CALCULATORS = {
    'matematica': {
        'title': 'Calculadora de Matemática',
        'description': 'Realize cálculos matemáticos complexos',
        'icon': 'square-root-alt',
        'categories': {
            'algebra': {
                'title': '🧠 Álgebra',
                'description': 'Cálculos envolvendo expressões e equações algébricas.',
                'calculations': {
                    'produtos_notaveis': {
                        'title': 'Produtos Notáveis',
                        'description': 'Aplica identidades algébricas clássicas.',
                        'variables': ['a', 'b', 'c']
                    },
                    'formula_delta': {
                        'title': 'Fórmula do Delta',
                        'description': 'Determina o valor de Δ em equações quadráticas.',
                        'variables': ['a', 'b']
                    },
                    'formula_bhaskara': {
                        'title': 'Fórmula de Bhaskara',
                        'description': 'Resolve equações do 2º grau.',
                        'variables': ['a1', 'b1', 'c1', 'a2', 'b2', 'c2']
                    },
                    'funcao_1_grau': {
                        'title': 'Função do 1º Grau',
                        'description': 'Análise de função linear',
                        'variables': ['a1', 'b1', 'c1', 'a2', 'b2', 'c2']
                    },
                    'funcao_2_grau': {
                        'title': 'Função do 2º Grau',
                        'description': 'Análise de parábolas.',
                        'variables': ['a1', 'b1', 'c1', 'a2', 'b2', 'c2']
                    },
                    'vertice_parabola': {
                        'title': 'Vértice da Parábola',
                        'description': 'Encontra o ponto de máximo ou mínimo.',
                        'variables': ['a1', 'b1', 'c1', 'a2', 'b2', 'c2']
                    },
                    'funcao_exponencial': {
                        'title': 'Função Exponencial',
                        'description': 'Comportamento de crescimento e decaimento.',
                        'variables': ['a1', 'b1', 'c1', 'a2', 'b2', 'c2']
                    },
                    'funcao_logaritmica': {
                        'title': 'Função Logarítmica',
                        'description': 'Operações com logaritmos.',
                        'variables': ['a1', 'b1', 'c1', 'a2', 'b2', 'c2']
                    }
                }
            },
            'funcoes_progressoes': {
                'title': '📈 Funções e Progressões',
                'description': 'Cálculos com sequências numéricas',
                'calculations': {
                    'pa_termo_geral': {
                        'title': 'PA: Termo Geral',
                        'description': 'Encontra um termo específico na PA.',
                        'variables': []
                    },
                    'pa_soma_termos': {
                        'title': 'PA: Soma dos Termos',
                        'description': 'Soma de uma sequência aritmética.',
                        'variables': ['a1', 'q', 'n']
                    },
                    'pg_termo_geral': {
                        'title': 'PG: Termo Geral',
                        'description': 'Termo específico em uma PG.',
                        'variables': []
                    },
                    'pg_soma_termos_finitos': {
                        'title': 'PG: Soma dos Termos Finitos',
                        'description': 'Soma parcial de uma PG.',
                        'variables': []
                    },
                    'pg_soma_infinita': {
                        'title': 'PG: Soma Infinita',
                        'description': 'Soma de uma PG infinita (convergente).',
                        'variables': []
                    },
                }
            },
            'trigonometria': {
                'title': '📐 Trigonometria',
                'description': 'Cálculos de áreas, volumes e perímetros',
                'calculations': {
                    'relacoes_fundamentais': {
                        'title': 'Relações Fundamentais',
                        'description': 'Seno, Cosseno Tangente.',
                        'variables': ['tipo', 'base', 'altura', 'raio']
                    },
                    'lei_senos': {
                        'title': 'Lei Senos',
                        'description': 'Relação entre lados e senos dos ângulos.',
                        'variables': ['tipo', 'base', 'altura', 'raio']
                    },
                    'lei_cossenos': {
                        'title': 'Lei dos Cossenos',
                        'description': 'Generalização do teorema de Pitágoras.',
                        'variables': ['tipo', 'lado', 'raio']
                    },
                }
            },
            'geometria': {
                'title': '🧮 Geometria',
                'description': 'Cálculos Trigonométricos',
                'calculations': {
                    'area_triangulo': {
                        'title': 'Área do Triângulo',
                        'description': 'Área usando base × altura ou trigonometria.',
                        'variables': []
                    },
                    'area_circulo': {
                        'title': 'Área do Círculo',
                        'description': 'Cálculo usando π × raio².',
                        'variables': []
                    },
                    'volume_cubo': {
                        'title': 'Volume do Cubo',
                        'description': 'Lado³.',
                        'variables': []
                    },
                    'volume_esfera': {
                        'title': 'Volume da Esfera',
                        'description': '4/3πr³',
                        'variables': []
                    },                   
                    'volume_cilindro': {
                        'title': 'Volume do Cilindro',
                        'description': 'π × raio² × altura.',
                        'variables': []
                    },
                }
            },
            'analise_combinatoria_probabilidade': {
                'title': '🔢 Análise Combinatória e Probabilidade',
                'description': 'Cálculos estatísticos',
                'calculations': {
                    'fatorial': {
                        'title': 'Fatorial',
                        'description': 'Produto de todos os inteiros positivos até n.',
                        'variables': ['valores']
                    },
                    'permutacao_simples': {
                        'title': 'Permutação Simples',
                        'description': 'Contagem de ordens possíveis.',
                        'variables': ['valores']
                    },
                    'combinacao_simples': {
                        'title': 'Combinação Simples',
                        'description': 'Contagem de agrupamentos sem ordem.',
                        'variables': ['valores']
                    },
                    'probabilidade': {
                        'title': 'Probabilidade',
                        'description': 'Chance de um evento ocorrer.',
                        'variables': ['valores']
                    }
                }
            },
            'matrizes':{
                'title': '🧊 Matrizes',
                'description': 'Cálculos estatísticos',
                'calculations': {
                    'determinante_matriz': {
                        'title': 'Determinante da Matriz',
                        'description': 'Valor escalar associado à matriz.',
                        'variables': []
                    },
                    'multiplicacao_matriz': {
                        'title': 'Multiplicação de Matriz',
                        'description': 'Produto entre duas matrizes.',
                        'variables': []
                    },
                }
            },
            'calculo_diferencial':{
                'title': '🧮 Cálculo Diferencial',
                'description': 'Cálculos estatísticos',
                'calculations': {
                    'limite': {
                        'title': 'Limite',
                        'description': '',
                        'variables': []
                    },
                    'derivada_funcao_potencia': {
                        'title': 'Derivada de Função Potência',
                        'description': '',
                        'variables': []
                    },
                }
            },
        }
    },
    'fisica': {
        'title': 'Calculadora de Física',
        'description': 'Realize cálculos físicos complexos',
        'icon': 'atom',
        'categories': {
            'cinematica': {
                'title': '🧮 Cinemática',
                'description': 'Cálculos de Movimento',
                'calculations': {
                    'velocidade_media': {
                        'title': 'Velocidade Média',
                        'description': 'Calcula a velocidade média, deslocamento ou tempo.',
                        'variables': ['velocidade_media', 'deslocamento', 'tempo']
                    },
                    'movimento_uniforme': {
                        'title': 'Movimento Uniforme',
                        'description': 'Calcula posição final/inicial, velocidade ou tempo em movimento uniforme.',
                        'variables': ['posicao_final', 'posicao_inicial', 'velocidade', 'tempo']
                    },
                    'movimento_uniformente_variado': {
                        'title': 'Movimento Uniformemente Variado',
                        'description': 'Calcula posição final/inicial, velocidade inicial, tempo ou aceleração em movimento uniformemente variado.',
                        'variables': ['posicao_final', 'posicao_inicial', 'velocidade_inicial', 'tempo', 'aceleracao']
                    },
                    'equacao_torricelli': {
                        'title': 'Equação de Torricelli',
                        'description': 'Calcula velocidade final/inicial, aceleração ou deslocamento sem usar o tempo.',
                        'variables': ['velocidade_final', 'velocidade_inicial', 'aceleracao', 'deslocamento']
                    }
                }
            },
            'dinamica': {
                'title': '🛠️ Dinâmica',
                'description': 'Cálculos de forças e leis de Newton.',
                'calculations': {
                    'principio_fundamental_dinamica': {
                        'title': 'Princípio Fundamental da Dinâmica',
                        'description': 'Calcula força, massa ou aceleração (F=ma).',
                        'variables': ['forca', 'massa', 'aceleracao']
                    },
                    'forca_peso': {
                        'title': 'Força Peso',
                        'description': 'Calcula força peso, massa ou gravidade (P=mg).',
                        'variables': ['forca_peso', 'massa', 'gravidade']
                    },
                    'forca_atrito': {
                        'title': 'Força de Atrito',
                        'description': 'Calcula força de atrito, coeficiente de atrito ou força normal.',
                        'variables': ['forca_atrito', 'coeficiente', 'normal']
                    }
                }
            },
            'trabalho_e_energia': {
                'title': '⚙️ Trabalho e Energia',
                'description': 'Cálculos relacionados a trabalho, energia e potência.',
                'calculations': {
                    'trabalho_forca_constante': {
                        'title': 'Trabalho de Força Constante',
                        'description': 'Calcula o trabalho realizado por uma força constante.',
                        'variables': ['trabalho', 'forca', 'deslocamento', 'angulo']
                    },
                    'energia_cinetica': {
                        'title': 'Energia Cinética',
                        'description': 'Calcula energia cinética, massa ou velocidade.',
                        'variables': ['energia_cinetica', 'massa', 'velocidade']
                    },
                    'energia_potencial': {
                        'title': 'Energia Potencial Gravitacional',
                        'description': 'Calcula energia potencial gravitacional, massa, altura ou gravidade.',
                        'variables': ['energia_potencial', 'massa', 'altura', 'gravidade']
                    },
                    'potencia': {
                        'title': 'Potência Média',
                        'description': 'Calcula potência média, trabalho ou tempo.',
                        'variables': ['potencia_media', 'trabalho', 'tempo']
                    },
                    'energia_potencial_elastica': {
                        'title': 'Energia Potencial Elástica',
                        'description': 'Calcula energia potencial elástica, constante elástica ou deformação.',
                        'variables': ['energia', 'constante', 'deformacao']
                    },
                    'energia_mecanica': {
                        'title': 'Energia Mecânica',
                        'description': 'Calcula energia mecânica, cinética ou potencial.',
                        'variables': ['energia_mec', 'energia_cinetica', 'energia_potencial']
                    },           
                }
            },
            'hidroestatica': {
                'title': '🌊 Hidrostática',
                'description': 'Cálculos relacionados a fluidos em repouso.',
                'calculations': {
                    'pressao': {
                        'title': 'Pressão',
                        'description': 'Calcula pressão, força ou área.',
                        'variables': ['pressao', 'forca', 'area']
                    },
                    'pressao_hidrostatica': {
                        'title': 'Pressão Hidrostática',
                        'description': 'Calcula pressão hidrostática, densidade, altura ou gravidade.',
                        'variables': ['pressao', 'densidade', 'altura', 'gravidade']
                    },
                    'empuxo': {
                        'title': 'Empuxo',
                        'description': 'Calcula empuxo, densidade, volume ou gravidade.',
                        'variables': ['empuxo', 'densidade', 'volume', 'gravidade']
                    }
                }
            },
            'termologia': {
                'title': '🌡️ Termologia',
                'description': 'Cálculos térmicos e termodinâmicos.',
                'calculations': {
                    'dilatacao_linear': {
                        'title': 'Dilatação Linear',
                        'description': 'Calcula dilatação linear, comprimento final/inicial, coeficiente ou variação de temperatura.',
                        'variables': ['dilatacao_linear', 'comprimento_final', 'comprimento_inicial', 'coeficiente', 'variacao_de_temperatura']
                    },
                    'primeira_lei_termodinamica': {
                        'title': 'Primeira Lei da Termodinâmica',
                        'description': 'Calcula variação da energia interna, calor ou trabalho.',
                        'variables': ['variacao_interna', 'calor', 'trabalho']
                    }
                }
            },
            'optica': {
                'title': '🔍 Óptica',
                'description': 'Cálculos envolvendo espelhos, lentes e fenômenos luminosos.',
                'calculations': {
                    'equacao_dos_espelhos_e_lentes': {
                        'title': 'Equação dos Espelhos e Lentes',
                        'description': 'Calcula distância focal, distância do objeto ou distância da imagem.',
                        'variables': ['distancia_focal', 'distancia_objeto', 'distancia_imagem']
                    },
                    'formula_do_aumento_da_imagem': {
                        'title': 'Fórmula do Aumento da Imagem',
                        'description': 'Calcula altura da imagem/objeto ou distância da imagem/objeto.',
                        'variables': ['altura_imagem', 'altura_objeto', 'distancia_objeto', 'distancia_imagem']
                    }
                }
            },
            'ondulatoria':{
                'title': '📡 Ondulatória',
                'description': 'Cálculos relacionados a ondas.',
                'calculations': {
                    'velocidade_onda': {
                        'title': 'Velocidade de uma Onda',
                        'description': 'Calcula velocidade, frequência ou comprimento de onda.',
                        'variables': ['velocidade', 'frequencia', 'comprimento_onda']
                    }
                }
            },
             'eletricidade':{
                'title': '⚡ Eletricidade',
                'description': 'Cálculos com energia elétrica e circuitos.',
                'calculations': {
                    'lei_ohm': {
                        'title': 'Lei de Ohm',
                        'description': 'Calcula tensão, resistência ou corrente.',
                        'variables': ['tensao', 'resistencia', 'corrente']
                    },
                    'potencia_eletrica': {
                        'title': 'Potência Elétrica',
                        'description': 'Calcula potência, tensão ou corrente elétrica.',
                        'variables': ['potencia', 'tensao', 'corrente']
                    },
                    'forca_entre_cargas_eletricas': {
                        'title': 'Força entre Cargas Elétricas (Lei de Coulomb)',
                        'description': 'Calcula força, constante eletrostática, cargas ou distância.',
                        'variables': ['forca', 'k', 'q1', 'q2', 'd']
                    },
                }
            },
        }
    },
    'quimica': {
        'title': 'Calculadora de Química',
        'description': 'Realize cálculos químicos complexos',
        'icon': 'flask',
        'categories': {
            'estequiometria': {
                'title': '⚗️ Estequiometria',
                'description': 'Cálculos de soluções',
                'calculations': {
                    'pureza': {
                        'title': 'Pureza',
                        'description': 'Calcula concentração em g/L ou mol/L',
                        'variables': ['massa_soluto', 'volume_solucao', 'massa_molar']
                    },
                    'rendimento': {
                        'title': 'Rendimento',
                        'description': 'Calcula concentração após diluição',
                        'variables': ['concentracao_inicial', 'volume_inicial', 'volume_final']
                    },
                    'excesso': {
                        'title': 'Excesso',
                        'description': 'Calcula concentração por titulação',
                        'variables': ['concentracao_titulante', 'volume_titulante', 'volume_analito']
                    },
                    'massa_reagentes_produtos': {
                        'title': 'Excesso',
                        'description': 'Calcula concentração por titulação',
                        'variables': ['concentracao_titulante', 'volume_titulante', 'volume_analito']
                    },
                    'quantidade_reagente_necessario': {
                        'title': 'Quantidade de Reagente Necessário',
                        'description': 'Calcula concentração por titulação',
                        'variables': ['concentracao_titulante', 'volume_titulante', 'volume_analito']
                    },
                    'balanceamento': {
                        'title': 'Balanceamento',
                        'description': 'Calcula concentração por titulação',
                        'variables': ['concentracao_titulante', 'volume_titulante', 'volume_analito']
                    }
                }
            },
            'gases': {
                'title':'💨 Gases',
                'description': 'Cálculos de pH e pOH',
                'calculations': {
                    'gases': {
                        'title': 'Gases',
                        'description': 'Calcula pH de uma solução',
                        'variables': ['concentracao_hidrogenio']
                    },
                }
            },
            'tabela_e_estrutura_atomica': {
                'title': '🔬 Tabela e Estrutura Atômica',
                'description': 'Leis dos gases',
                'calculations': {
                    'tabela_periodica': {
                        'title': 'Tabela Periódica',
                        'description': 'Calcula pressão final (P1V1 = P2V2)',
                        'variables': ['pressao_inicial', 'volume_inicial', 'volume_final']
                    },
                }
            },
            'eletroquimica': {
                'title': '🔋 Eletroquímica',
                'description': 'Cálculos estequiométricos',
                'calculations': {
                    'pilha_daniels': {
                        'title': 'Pilha de Daniels',
                        'description': 'Calcula massa molar',
                        'variables': ['massa', 'quantidade_mols']
                    },
                }
            },
            'termoquimica': {
                'title': '🔥 Termoquímica',
                'description': 'Cálculos estequiométricos',
                'calculations': {
                    'termoquimica': {
                        'title': 'Termoquímica',
                        'description': 'Calcula massa molar',
                        'variables': ['massa', 'quantidade_mols']
                    },
                }
            },
            'equilibrio_quimico': {
                'title': '💧 Equilíbrio Químico',
                'description': 'Cálculos estequiométricos',
                'calculations': {
                    'equilibrio_quimico': {
                        'title': 'Equilíbrio Químico',
                        'description': 'Calcula massa molar',
                        'variables': ['massa', 'quantidade_mols']
                    },
                }
            },
        }
    }
} 

UNIDADES_VARIAVEIS = {
    'velocidade_media': 'm/s',
    'velocidade': 'm/s',
    'deslocamento': 'm',
    'tempo': 's',
    'posicao_final': 'm',
    'posicao_inicial': 'm',
    'velocidade_inicial': 'm/s',
    'velocidade_final': 'm/s',
    'aceleracao': 'm/s²',
    'massa': 'kg',
    'gravidade': 'm/s²',
    'força': 'N',
    'coeficiente': '',
    'normal': 'N',
    'angulo': 'graus',
    'trabalho': 'J',
    'energia': 'J',
    'altura': 'm',
    'potencia': 'W',
    'pressao': 'Pa',
    'forca': 'N',
    'area': 'm²',
    'densidade': 'kg/m³',
    'volume': 'm³',
    'comprimento_final': 'm',
    'comprimento_inicial': 'm',
    'variacao_de_temperatura': '°C',
    'mols': 'mol',
    'R': 'J/mol·K',
    'temperatura': 'K',
    'variacao_interna': 'J',
    'calor': 'J',
    'distancia_focal': 'm',
    'distancia_objeto': 'm',
    'distancia_imagem': 'm',
    'altura_imagem': 'm',
    'altura_objeto': 'm',
    'frequencia': 'Hz',
    'comprimento_onda': 'm',
    'resistencia': 'cΩ',
    'corrente': 'A',
    'tensao': 'V',
    'p': 'W',
    'v': 'V',
    'i': 'A',
    'k': 'N·m²/C²',
    'q1': 'C',
    'q2': 'C',
    'd': 'm',
    'constante': 'N/m',
    'deformacao': 'm',
    'energia_cinetica': 'J',
    'energia_potencial': 'J',
    'massa_soluto': 'g',
    'volume_solucao': 'L',
    'massa_molar': 'g/mol'
}