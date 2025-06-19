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
    'email': os.getenv('CONTACT_EMAIL', 'suporte.calclab@gmail.com'),
    'phone': os.getenv('CONTACT_PHONE', '+55 38 98824-8721'),
    'whatsapp': os.getenv('CONTACT_WHATSAPP', '+55 38 98824-8721'),
    'telegram': os.getenv('CONTACT_TELEGRAM', '@calclab')
}

# Configurações de redes sociais
SOCIAL_MEDIA = {
    'facebook': os.getenv('FACEBOOK_URL', 'https://facebook.com/calclab'),
    'twitter': os.getenv('TWITTER_URL', 'https://twitter.com/calclab'),
    'instagram': os.getenv('INSTAGRAM_URL', 'https://instagram.com/calclab_'),
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
                    'formula_do_delta': {
                        'title': 'Fórmula do Delta [Δ = b² - 4ac]',
                        'description': 'Determina o valor de Δ em equações quadráticas.',
                        'variables': ['delta', 'b' , 'a', 'c']
                    },
                    'formula_de_bhaskara': {
                        'title': 'Fórmula de Bhaskara [x = -b±√Δ/2a]',
                        'description': 'Resolve equações do 2º grau.',
                        'variables': ['x', 'b', 'delta', 'a']
                    },
                    'funcao_do_1_grau': {
                        'title': 'Função do 1º Grau [f(x) = ax + b]',
                        'description': 'Análise de função linear',
                        'variables': ['fx', 'ax', 'b']
                    },
                    'funcao_do_2_grau': {
                        'title': 'Função do 2º Grau [f(x) = ax² + bx + c]',
                        'description': 'Análise de parábolas.',
                        'variables': ['fx', 'ax2', 'bx', 'c']
                    },
                    'vertice_parabola': {
                        'title': 'Vértice de Parábola [Vp = -b/2a]',
                        'description': 'Encontra o ponto de máximo ou mínimo.',
                        'variables': ['vertice_da_parabola', 'b', 'a']
                    },
                    'funcao_exponencial': {
                        'title': 'Função Exponencial [f(x) a.b^x]',
                        'description': 'Comportamento de crescimento e decaimento.',
                        'variables': ['fx', 'a', 'b', 'x']
                    },
                    'funcao_logaritmica': {
                        'title': 'Função Logarítmica [f(x) = logb(x)]',
                        'description': 'Operações com logaritmos.',
                        'variables': ['fx', 'b', 'x']
                    }
                }
            },
            'funcoes_progressoes': {
                'title': '📈 Funções e Progressões',
                'description': 'Cálculos com sequências numéricas',
                'calculations': {
                    'pa_termo_geral': {
                        'title': 'PA: Termo Geral [an = a1 + (n-1)r]',
                        'description': 'Encontra um termo específico na PA.',
                        'variables': ['termo_geral', 'primeiro_termo', 'termo_em_sequencia', 'razao_da_pa']
                    },
                    'pa_soma_termos': {
                        'title': 'PA: Soma dos Termos [Sn = n(a1 + an)/2]',
                        'description': 'Soma de uma sequência aritmética.',
                        'variables': ['soma_dos_termos', 'termos_somados', 'primeiro_termo', 'ultimo_termo']
                    },
                    'pg_termo_geral': {
                        'title': 'PG: Termo Geral [an = a1.q^(n-1)]',
                        'description': 'Termo específico em uma PG.',
                        'variables': ['termo_geral', 'primeiro_termo', 'razao_da_pg', 'termo_em_sequencia']
                    },
                    'pg_soma_termos_finitos': {
                        'title': 'PG: Soma dos Termos Finitos [Sn = a1 . (q^n - 1)/(q - 1)]',
                        'description': 'Soma parcial de uma PG.',
                        'variables': ['soma_dos_termos', 'primeiro_termo', 'razao_da_pg', 'termos_somados']
                    },
                    'pg_soma_infinita': {
                        'title': 'PG: Soma Infinita [S = a1/(1-q)]',
                        'description': 'Soma de uma PG infinita (convergente).',
                        'variables': ['soma_infinita', 'primeiro_termo', 'razao_da_pg']
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
                        'variables': ['#', '#', '#', '#'] #! REVISAR VARIÁVEIS
                    },
                    'lei_dos_senos': {
                        'title': 'Lei Senos [a/sen(a_) = b/sen(b_) = c/sen(c_)]',
                        'description': 'Relação entre lados e senos dos ângulos.',
                    'variables': ['a', 'a_', 'b', 'b_', 'c', 'c_']
                    },
                    'lei_dos_cossenos': {
                        'title': 'Lei dos Cossenos [a² = b² + c² - 2bc.cos(a_)]',
                        'description': 'Generalização do teorema de Pitágoras.',
                        'variables': ['a', 'a_', 'b', 'c']
                    },
                }
            },
            'geometria': {
                'title': '🧮 Geometria',
                'description': 'Cálculos Trigonométricos',
                'calculations': {
                    'area_do_triangulo': {
                        'title': 'Área do Triângulo [A = b.h/2]',
                        'description': 'Área usando base × altura ou trigonometria.',
                        'variables': ['area_do_triangulo', 'base', 'altura']
                    },
                    'area_do_circulo': {
                        'title': 'Área do Círculo [A = π.r²]',
                        'description': 'Cálculo usando π × raio².',
                        'variables': ['area_do_circulo', 'raio']
                    },
                    'volume_do_cubo': {
                        'title': 'Volume do Cubo [V = a³]',
                        'description': 'Lado³.',
                        'variables': ['volume_do_cubo', 'aresta']
                    },
                    'volume_da_esfera': {
                        'title': 'Volume da Esfera [V = 4/3πr³]',
                        'description': '4/3πr³',
                        'variables': ['volume_da_esfera', 'raio']
                    },                   
                    'volume_do_cilindro': {
                        'title': 'Volume do Cilindro [V = π.r².h]',
                        'description': 'π × raio² × altura.',
                        'variables': ['volume_do_cilindro', 'raio', 'altura']
                    },
                }
            },
            'analise_combinatoria_probabilidade': {
                'title': '🔢 Análise Combinatória e Probabilidade',
                'description': 'Cálculos estatísticos',
                'calculations': {
                    'fatorial': {
                        'title': 'Fatorial [n! = n.(n-1).(n-2)...1]',
                        'description': 'Produto de todos os inteiros positivos até n.',
                        'variables': ['n!', 'n']
                    },
                    'permutacao_simples': {
                        'title': 'Permutação Simples [P(n) = n!]',
                        'description': 'Contagem de ordens possíveis.',
                        'variables': ['pn', 'n!']
                    },
                    'combinacao_simples': {
                        'title': 'Combinação Simples [C(n,k) = n!/k!(n-k)!]',
                        'description': 'Contagem de agrupamentos sem ordem.',
                        'variables': ['cnk #', 'n!', 'n', 'k'] # ! VERIFICAR VARIÁVEIS
                    },
                    'probabilidade': {
                        'title': 'Probabilidade [P = favoráveis/possíveis]',
                        'description': 'Chance de um evento ocorrer.',
                        'variables': ['probabilidade', 'casos_favoraveis', 'casos_possiveis']
                    }
                }
            },
            'matrizes':{
                'title': '🧊 Matrizes',
                'description': 'Cálculos estatísticos',
                'calculations': {
                    'determinante_da_matriz': {
                        'title': 'Determinante da Matriz',
                        'description': 'Valor escalar associado à matriz.',
                        'variables': ['#', '#', '#', '#'] # ! VERIFICAR VARIÁVEIS
                    },
                    'multiplicacao_de_matriz': {
                        'title': 'Multiplicação de Matriz [Cij = n∑k=1 Aik.Bkj]',
                        'description': 'Produto entre duas matrizes.',
                        'variables': ['#', '#', '#', '#'] # ! VERIFICAR VARIÁVEIS
                    },
                }
            },
            'calculo_diferencial':{
                'title': '🧮 Cálculo Diferencial',
                'description': 'Cálculos estatísticos',
                'calculations': {
                    'limite': {
                        'title': 'Limite [lim f(x) = L]',
                        'description': '',
                        'variables': ['limite_fx', 'l']
                    },
                    'derivada_de_funcao_potencia': {
                        'title': 'Derivada de Função Potência [f"(x) = n.x^(n-1)]',
                        'description': '',
                        'variables': ['f"x', 'n', 'x']
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
                        'title': 'Velocidade Média vm = [Δs/Δt]',
                        'description': 'Calcula a velocidade média, deslocamento ou tempo.',
                        'variables': ['velocidade_media', 'deslocamento', 'tempo']
                    },
                    'movimento_uniforme': {
                        'title': 'Movimento Uniforme [s = s0 + v.t]',
                        'description': 'Calcula posição final/inicial, velocidade ou tempo em movimento uniforme.',
                        'variables': ['posicao_final', 'posicao_inicial', 'velocidade', 'tempo']
                    },
                    'movimento_uniformemente_variado': {
                        'title': 'Movimento Uniformemente Variado [s = s0 + v0.t + a.t²/2]',
                        'description': 'Calcula posição final/inicial, velocidade inicial, tempo ou aceleração em movimento uniformemente variado.',
                        'variables': ['posicao_final', 'posicao_inicial', 'velocidade_inicial', 'tempo', 'aceleracao']
                    },
                    'equacao_torricelli': {
                        'title': 'Equação de Torricelli [v² = v0² + 2.a.Δs]',
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
                        'title': 'Princípio Fundamental da Dinâmica [F = m.a]',
                        'description': 'Calcula força, massa ou aceleração (F=ma).',
                        'variables': ['forca', 'massa', 'aceleracao']
                    },
                    'forca_peso': {
                        'title': 'Força Peso [P = m.g]',
                        'description': 'Calcula força peso, massa ou gravidade (P=mg).',
                        'variables': ['forca_peso', 'massa', 'gravidade']
                    },
                    'forca_atrito': {
                        'title': 'Força de Atrito [Fat = μ.N]',
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
                        'title': 'Trabalho de Força Constante [ω = F.d.cosθ]',
                        'description': 'Calcula o trabalho realizado por uma força constante.',
                        'variables': ['trabalho', 'forca', 'deslocamento', 'angulo']
                    },
                    'energia_cinetica': {
                        'title': 'Energia Cinética [Ec = m.v²/2]',
                        'description': 'Calcula energia cinética, massa ou velocidade.',
                        'variables': ['energia_cinetica', 'massa', 'velocidade']
                    },
                    'energia_potencial': {
                        'title': 'Energia Potencial Gravitacional [Ep = m.g.h]',
                        'description': 'Calcula energia potencial gravitacional, massa, altura ou gravidade.',
                        'variables': ['energia_potencial', 'massa', 'altura', 'gravidade']
                    },
                    'potencia': {
                        'title': 'Potência Média [P = ω/Δt]',
                        'description': 'Calcula potência média, trabalho ou tempo.',
                        'variables': ['potencia_media', 'trabalho', 'tempo']
                    },
                    'energia_potencial_elastica': {
                        'title': 'Energia Potencial Elástica [Epe = k.x²/2]',
                        'description': 'Calcula energia potencial elástica, constante elástica ou deformação.',
                        'variables': ['energia_potencial_elastica', 'constante_elastica', 'deformacao']
                    },
                    'energia_mecanica': {
                        'title': 'Energia Mecânica [Em = Ec + Ep]',
                        'description': 'Calcula energia mecânica, cinética ou potencial.',
                        'variables': ['energia_mecanica', 'energia_cinetica', 'energia_potencial']
                    },           
                }
            },
            'hidroestatica': {
                'title': '🌊 Hidrostática',
                'description': 'Cálculos relacionados a fluidos em repouso.',
                'calculations': {
                    'pressao': {
                        'title': 'Pressão [P = F/A]',
                        'description': 'Calcula pressão, força ou área.',
                        'variables': ['pressao', 'forca', 'area']
                    },
                    'pressao_hidrostatica': {
                        'title': 'Pressão Hidrostática [P = ρ.g.h]',
                        'description': 'Calcula pressão hidrostática, densidade, altura ou gravidade.',
                        'variables': ['pressao_hidrostatica', 'densidade', 'altura', 'gravidade']
                    },
                    'empuxo': {
                        'title': 'Empuxo [E = ρ.g.V]',
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
                        'title': 'Dilatação Linear [ΔL = L0.α.ΔT]',
                        'description': 'Calcula dilatação linear, comprimento final/inicial, coeficiente ou variação de temperatura.',
                        'variables': ['dilatacao_linear', 'coeficiente_dilatacao', 'comprimento_inicial', 'variacao_de_temperatura']
                    },
                    'primeira_lei_termodinamica': {
                        'title': 'Primeira Lei da Termodinâmica [ΔU = Q - W]',
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
                        'title': 'Equação dos Espelhos e Lentes [1/f = 1/p + 1/p"]',
                        'description': 'Calcula distância focal, distância do objeto ou distância da imagem.',
                        'variables': ['distancia_focal', 'distancia_objeto', 'distancia_imagem']
                    },
                    'aumento_da_imagem': {
                        'title': 'Aumento da Imagem [A = -i/o]',
                        'description': 'Calcula o aumento por meio da distância da imagem do objeto.',
                        'variables': ['aumento_da_imagem', 'distancia_objeto', 'distancia_imagem']
                    }
                }
            },
            'ondulatoria':{
                'title': '📡 Ondulatória',
                'description': 'Cálculos relacionados a ondas.',
                'calculations': {
                    'velocidade_onda': {
                        'title': 'Velocidade de uma Onda [v = λ.f]',
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
                        'title': 'Lei de Ohm [U = R.I]',
                        'description': 'Calcula tensão, resistência ou corrente.',
                        'variables': ['tensao', 'resistencia', 'corrente']
                    },
                    'potencia_eletrica': {
                        'title': 'Potência Elétrica [P = U.I]',
                        'description': 'Calcula potência, tensão ou corrente elétrica.',
                        'variables': ['potencia', 'tensao', 'corrente']
                    },
                    'forca_entre_cargas_eletricas': {
                        'title': 'Força entre Cargas Elétricas (Lei de Coulomb) [F = k.q1.q2/r²] k = 9x10⁹',
                        'description': 'Calcula força, constante eletrostática, cargas ou distância.',
                        'variables': ['forca_de_coloumb', 'carga_1', 'carga_2', 'distancia']
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
                        'title': 'Pureza [massa da subs pura/massa da subs amotra . 100]',
                        'description': 'Calcula concentração em g/L ou mol/L',
                        'variables': ['pureza', 'massa_da_substancia_pura', 'massa_da_substancia_amostra']
                    },
                    'rendimento': {
                        'title': 'Rendimento [rendimento real / rendimento teorico . 100]',
                        'description': 'Calcula concentração após diluição',
                        'variables': ['rendimento', 'rendimento_real', 'rendimento_teorico']
                    },
                    'excesso': {
                        'title': 'Excesso ',
                        'description': 'Calcula concentração por titulação',
                        'variables': ['equacao_reagentes', 'equacao_produtos', 'massa_disponivel']
                    },
                    'quantidade_de_reagentes_necessario': {
                        'title': 'Quantidade de Reagente Necessário',
                        'description': 'Calcula concentração por titulação',
                        'variables': ['equacao_reagentes', 'equacao_produtos', 'massa_dos_produtos_desejada']
                    },
                    'massa_dos_reagentes_ou_dos_produtos': {
                        'title': 'Massa dos Reagentes ',
                        'description': 'Calcula a massa dos reagentes ou dos produtos da reação',
                        'variables': ['composto_quimico']
                    },
                    'balanceamento': {
                        'title': 'Balanceamento',
                        'description': 'Calcula concentração por titulação',
                        'variables': ['equacao_reagentes', 'equacao_produtos']
                    }
                }
            },
            'gases': {
                'title':'💨 Gases',
                'description': 'Cálculos de pH e pOH',
                'calculations': {
                    'gases': {
                        'title': 'Gases [P.V = n.R.T]',
                        'description': 'Calcula pH de uma solução',
                        'variables': ['pressao', 'volume', 'numero_de_mols', 'temperatura']
                    },
                }
            },
            'tabela_periodica': {
                'title': '🔬 Tabela e Estrutura Atômica',
                'description': 'Tabela periódica',
                'calculations': {
                    'tabela_periodica': {
                        'title': 'Tabela Periódica',
                        'description': 'Mostra as informações de um determinado elemento químico.',
                        'variables': ['elemento']
                    },
                }
            },
            'pilha_de_daniels': {
                'title': '🔋 Eletroquímica',
                'description': 'Cálculos estequiométricos',
                'calculations': {
                    'pilha_daniels': {
                        'title': 'Pilha de Daniels',
                        'description': 'Calcula massa molar',
                        'variables': ['equacao_reagentes', 'equacao_produtos', 'concentracao_dos_produtos', 'concentracao_dos_reagentes']
                    },
                }
            },
            'termoquimica': {
                'title': '🔥 Termoquímica',
                'description': 'Cálculos estequiométricos',
                'calculations': {
                    'termoquimica': {
                        'title': 'Termoquímica ΔH = H produtos - H reagentes',
                        'description': 'Calcula massa molar',
                        'variables': ['delta_h', 'entalpia_dos_produtos', 'entalpia_dos_reagentes']
                    },
                }
            },
            'equilibrio_ionico': {
                'title': '💧 Equilíbrio Iônico',
                'description': 'Cálculos estequiométricos',
                'calculations': {
                    'equilibrio_quimico': {
                        'title': 'Equilíbrio Iônico',
                        'description': 'Calcula massa molar',
                        'variables': ['acido_ou_base', 'constante_de_equilibrio', 'concentracao_incial']
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
    'resistencia': 'Ω',
    'corrente': 'A',
    'tensao': 'V',
    'p': 'W',
    'v': 'V',
    'i': 'A',
    'k': 'N·m²/C²',
    'q1': 'C',
    'q2': 'C',
    'r': 'm',
    'constante': 'N/m',
    'deformacao': 'm',
    'energia_cinetica': 'J',
    'energia_potencial': 'J',
    'massa_soluto': 'g',
    'volume_solucao': 'L',
    'massa_molar': 'g/mol',
    "pureza": "%", 
    "massa_da_substancia_pura": "g", 
    "massa_da_substancia_amostra": "g",  
    "rendimento": "%", 
    "rendimento_real": "g", 
    "rendimento_teorico": "g", 
    "pressao": "atm", 
    "volume": "L",
    "numero_de_mols": "mol", 
    "constante_R": "atm·L/(mol·K)",  
    "temperatura": "K",  
    "delta_h": "kJ/mol",  
    "entalpia_dos_produtos": "kJ/mol",  
    "entalpia_dos_reagentes": "kJ/mol"
}