# Documentação do CalcLab

## Índice

1. [Visão Geral](#visão-geral)
2. [Estrutura do Projeto](#estrutura-do-projeto)
3. [Funcionalidades](#funcionalidades)
4. [Como Personalizar](#como-personalizar)
5. [Configuração e Instalação](#configuração-e-instalação)
6. [Manutenção](#manutenção)

## Visão Geral

O CalcLab é uma aplicação web desenvolvida em Flask para realizar cálculos científicos nas áreas de Física, Química e Matemática. O site oferece uma interface intuitiva e responsiva, com suporte a modo escuro e feedback visual para os usuários.

## Estrutura do Projeto

```
CalcLab/
├── app.py                 # Arquivo principal da aplicação
├── config.py             # Configurações do site
├── requirements.txt      # Dependências do projeto
├── static/
│   ├── css/
│   │   └── style.css    # Estilos do site
│   └── js/
│       └── main.js      # JavaScript principal
├── templates/
│   ├── base.html        # Template base
│   ├── index.html       # Página inicial
│   ├── fisica.html      # Calculadora de Física
│   ├── quimica.html     # Calculadora de Química
│   ├── matematica.html  # Calculadora de Matemática
│   ├── sobre.html       # Página Sobre
│   └── contato.html     # Página de Contato
└── calc_fisica.py       # Funções de cálculo de Física
```

## Funcionalidades

### 1. Calculadora de Física

- Velocidade Média  
- Movimento Uniforme  
- Movimento Uniformemente Variado  
- Equação de Torricelli  
- Princípio Fundamental da Dinâmica  
- Força Peso  
- Força de Atrito  
- Trabalho da Força Constante  
- Energia Cinética  
- Energia Potencial  
- Potência Média  
- Pressão  
- Pressão Hidrostática  
- Empuxo  
- Dilatação Linear  
- Equação Fundamental da Calorimetria  
- Primeira Lei da Termodinâmica  
- Equação dos Espelhos e Lentes  
- Fórmula do Aumento da Imagem  
- Velocidade de uma Onda  
- Lei de Ohm  


### 2. Calculadora de Química

- Pureza
- Rendimento
- Gases
- Balanceamento
- Excesso
- Massa dos Reagentes ou dos Produtos
- Quantidade de Reagente Necessário
- Tabela Periódica
- Pilha de Daniels
- Termoquímica
 - Equilíbrio Iônico


### 3. Calculadora de Matemática

- Produtos Notáveis
- Fórmula do Delta
- Fórmula de Bhaskara
- Função do 1º Grau
- Função do 2º Grau
- Vértice da Parábola
- Função Exponencial
- Função Logarítmica
- PA: Termo Geral
- PA: Soma dos Termos
- PG: Termo Geral
- PG: Soma dos Termos Finito
- PG: Soma Infinita
- Trigonometria: Relações Fundamentais
- Lei dos Cossenos
- Área do Triângulo
- Área do Círculo
- Volume do Cubo
- Volume da Esfera
- Volume do Cilindro
- Fatorial
- Permutação Simples
- Combinação Simples
- Probabilidade
- Determinante da Matriz
- Multiplicação de Matriz
- Limite
- Derivada de Função Potência


## Como Personalizar

### 1. Configurações Gerais (config.py)

```python
# Informações básicas do site
SITE_NAME = "CalcLab"
SITE_DESCRIPTION = "Sua descrição aqui"

# Informações de contato
CONTACT_EMAIL = "suporte.calclab@gmail.com"
CONTACT_PHONE = "(38) 98824-8721"
CONTACT_ADDRESS = "Seu endereço"

# Redes sociais
SOCIAL_MEDIA = {
    "facebook": "https://facebook.com/seusite",
    "instagram": "https://instagram.com/seusite",
    "twitter": "https://twitter.com/seusite"
}

# Informações da empresa
ABOUT = {
    "title": "Sobre o CalcLab",
    "description": "Sua descrição aqui",
    "team": [
        {
            "name": "Nome do Membro",
            "role": "Cargo",
            "bio": "Biografia curta"
        }
    ]
}
```

### 2. Personalizar Visual (static/css/style.css)

- Cores do tema
- Fontes
- Espaçamentos
- Responsividade
- Modo escuro

### 3. Adicionar Novos Cálculos

1. Criar função de cálculo em `calc_fisica.py`, `calc_quimica.py` ou `calc_matematica.py`
2. Adicionar interface no template correspondente
3. Registrar rota em `app.py`

Exemplo de nova função de cálculo:

```python
def nova_funcao(variavel, param1=None, param2=None):
    try:
        if variavel == 'resultado':
            return param1 * param2
        else:
            raise ValueError("Parâmetros inválidos")
    except Exception as e:
        raise ValueError(f"Erro: {str(e)}")
```

### 4. Personalizar Templates

- Editar `templates/base.html` para mudar o layout base
- Modificar templates individuais para cada página
- Adicionar novos elementos HTML/Bootstrap
- Personalizar mensagens e textos

## Configuração e Instalação

### 1. Requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- Navegador web moderno

### 2. Instalação

1. Criar ambiente virtual:

```bash
python -m venv venv
```

2. Ativar ambiente virtual:

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instalar dependências:

```bash
pip install -r requirements.txt
```

### 3. Executar o Projeto

```bash
python app.py
```

Acesse http://localhost:5000 no navegador

## Manutenção

### 1. Backup

- Fazer backup regular do banco de dados
- Manter cópia dos arquivos de configuração
- Versionar código no Git

### 2. Atualizações

- Manter dependências atualizadas
- Verificar compatibilidade
- Testar após atualizações

### 3. Monitoramento

- Verificar logs de erro
- Monitorar desempenho
- Acompanhar feedback dos usuários

### 4. Segurança

- Manter senhas seguras
- Atualizar certificados SSL
- Validar entradas de usuário
- Proteger contra injeção SQL

## Suporte

Para suporte técnico ou dúvidas:

- Email: suporte@calclab.com
- Telefone: (00) 0000-0000
- Site: www.calclab.com/suporte

Agora você tem uma documentação completa do projeto e um arquivo de configuração abrangente. A documentação em documentacao.md explica:

1. A estrutura do projeto
2. Todas as funcionalidades disponíveis
3. Como personalizar cada aspecto do site
4. Como instalar e configurar o ambiente
5. Como fazer manutenção
   O arquivo config.py permite personalizar:
6. Informações básicas do site (nome, descrição, etc.)
7. Informações de contato
8. Links de redes sociais
9. Informações da equipe
10. Configurações de email
11. Configurações de segurança
12. Configurações de tema (cores, fontes, etc.)
13. Lista de calculadoras disponíveis
14. E muito mais
    Para editar qualquer aspecto do site:
15. Informações Básicas:
    • Abra config.py
    • Edite as variáveis em SITE_NAME, SITE_DESCRIPTION, etc.
16. Contatos e Redes Sociais:
    • Em config.py, encontre as seções CONTACT e SOCIAL_MEDIA
    • Atualize com suas informações
17. Aparência:
    • Em config.py, seção THEME
    • Altere cores, fontes e outros aspectos visuais
18. Calculadoras:
    • Em config.py, seção CALCULADORAS
    • Adicione ou remova cálculos conforme necessário
19. Equipe:
    • Em config.py, seção ABOUT["team"]
    • Adicione ou edite membros da equipe
20. Templates:
    • Edite os arquivos HTML em templates/
    • Use Bootstrap para layout responsivo
21. Estilos:
    • Edite static/css/style.css
    • Personalize cores, espaçamentos, etc.
22. Funcionalidades:
    • Edite os arquivos Python correspondentes
    • Adicione novas funções de cálculo
    • Atualize rotas em app.py
    Lembre-se de sempre:
23. Fazer backup antes de editar
24. Testar as mudanças localmente
25. Verificar se as unidades de medida estão corretas
26. Manter a consistência visual
27. Documentar alterações importantes
    Quer que eu explique mais algum aspecto específico ou ajude com alguma personalização?
