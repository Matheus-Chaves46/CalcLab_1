# CalcLab - Calculadora Científica Online

CalcLab é uma aplicação web que oferece calculadoras científicas para Física, Química e Matemática.

## Funcionalidades

- Calculadoras de Física (velocidade média, movimento uniforme, etc.)
- Calculadoras de Química (tabela periódica, balanceamento de equações, etc.)
- Calculadoras de Matemática (funções, trigonometria, etc.)
- Formulário de contato
- Interface responsiva e moderna

## Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/calclab.git
cd calclab
```

2. Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
   - Copie o arquivo `.env.example` para `.env`
   - Edite o arquivo `.env` com suas configurações:
     - `SECRET_KEY`: Chave secreta para o Flask
     - `MAIL_USERNAME`: Seu e-mail Gmail
     - `MAIL_PASSWORD`: Sua senha de aplicativo do Gmail

## Executando o Projeto

1. Ative o ambiente virtual (se ainda não estiver ativo):

```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Execute o servidor:

```bash
flask run
```

3. Acesse a aplicação em `http://localhost:5000`

## Estrutura do Projeto

```
calclab/
├── app.py              # Aplicação principal
├── config.py           # Configurações do site
├── calc_fisica.py      # Funções de cálculo de física
├── requirements.txt    # Dependências do projeto
├── .env               # Variáveis de ambiente
├── static/            # Arquivos estáticos
│   └── css/
│       └── style.css  # Estilos CSS
└── templates/         # Templates HTML
    ├── base.html      # Template base
    ├── index.html     # Página inicial
    ├── fisica.html    # Página de física
    ├── quimica.html   # Página de química
    ├── matematica.html # Página de matemática
    ├── sobre.html     # Página sobre
    └── contato.html   # Página de contato
```

## Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Contato

Seu Nome - [@seu_twitter](https://twitter.com/seu_twitter) - email@exemplo.com

Link do Projeto: [https://github.com/seu-usuario/calclab](https://github.com/seu-usuario/calclab)
