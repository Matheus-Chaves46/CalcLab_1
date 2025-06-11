"""
Interface da calculadora matemática.
"""

import tkinter as tk
from tkinter import ttk
from calc_matematica import *

class CalculadoraMatematica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Matemática")
        
        # Frame principal
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Combobox para seleção de operação
        self.operacao = ttk.Combobox(self.frame, values=[
            'Produtos Notáveis',
            'Formula do Delta',
            'Formula de Bhaskara',
            'Função do 1° Grau',
            'Função do 2° Grau',
            'Vertice da Parabola',
            'Função Exponencial',
            'Função Logaritmica',
            'PA: Termo Geral',
            'PA: Soma dos Termos',
            'PG: Termo Geral',
            'PG: Soma dos Termos Finitos',
            'PG: Soma Infinita',
            'Relacoes Fundamentais',
            'Lei dos Senos',
            'Lei dos Cossenos',
            'Area do Triangulo',
            'Area do Circulo',
            'Volume do Cubo',
            'Volume da Esfera',
            'Volume do Cilindro',
            'Fatorial',
            'Permutação Simples',
            'Combinacao Simples',
            'Probabilidade',
            'Determinante da Matriz',
            'Multiplicação de Matriz',
            'Limite',
            'Derivada de Funcao Potencia'
        ])
        self.operacao.grid(row=0, column=0, columnspan=2, pady=5)
        self.operacao.set("Produtos Notáveis")
        self.operacao.bind('<<ComboboxSelected>>', self.atualizar_campos)
        
        # Frame para campos de entrada
        self.campos_frame = ttk.Frame(self.frame)
        self.campos_frame.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Campos de entrada
        self.entradas = {}
        
        # Variáveis para produtos notáveis
        self.tipo_produto = tk.StringVar()
        self.var_a = tk.BooleanVar()
        self.var_b = tk.BooleanVar()
        
        # Botão de cálculo
        self.calcular_btn = ttk.Button(self.frame, text="Calcular", command=self.calcular)
        self.calcular_btn.grid(row=2, column=0, columnspan=2, pady=5)
        
        # Label para resultado
        self.resultado = ttk.Label(self.frame, text="")
        self.resultado.grid(row=3, column=0, columnspan=2, pady=5)
        
        # Label para fórmula
        self.formula = ttk.Label(self.frame, text="")
        self.formula.grid(row=4, column=0, columnspan=2, pady=5)
        
        # Inicializar campos
        self.atualizar_campos()
    
    def atualizar_campos(self, event=None):
        # Limpar campos existentes
        for widget in self.campos_frame.winfo_children():
            widget.destroy()
        self.entradas.clear()
        self.formula.config(text="")
        
        operacao = self.operacao.get()
        
        if operacao == "Produtos Notáveis":
            # Frame para radio buttons
            radio_frame = ttk.LabelFrame(self.campos_frame, text="Selecione o tipo de produto notável")
            radio_frame.grid(row=0, column=0, columnspan=2, pady=5, padx=5, sticky="ew")
            
            # Radio buttons
            ttk.Radiobutton(radio_frame, text="Quadrado da soma [(a+b)² = a² + 2ab + b²]",
                           variable=self.tipo_produto, value="quadrado_soma",
                           command=self.atualizar_checkboxes).grid(row=0, column=0, sticky="w", padx=5, pady=2)
            
            ttk.Radiobutton(radio_frame, text="Quadrado da diferença [(a-b)² = a² - 2ab + b²]",
                           variable=self.tipo_produto, value="quadrado_diferenca",
                           command=self.atualizar_checkboxes).grid(row=1, column=0, sticky="w", padx=5, pady=2)
            
            ttk.Radiobutton(radio_frame, text="Diferença dos quadrados [a²-b² = (a+b)(a-b)]",
                           variable=self.tipo_produto, value="diferenca_quadrados",
                           command=self.atualizar_checkboxes).grid(row=2, column=0, sticky="w", padx=5, pady=2)
            
            # Frame para checkboxes
            self.checkbox_frame = ttk.LabelFrame(self.campos_frame, text="Selecione a variável que você tem")
            self.checkbox_frame.grid(row=1, column=0, columnspan=2, pady=5, padx=5, sticky="ew")
            
            # Checkboxes (agora mutuamente exclusivos)
            ttk.Checkbutton(self.checkbox_frame, text="Valor de a",
                           variable=self.var_a,
                           command=self.on_var_a).grid(row=0, column=0, sticky="w", padx=5, pady=2)
            
            ttk.Checkbutton(self.checkbox_frame, text="Valor de b",
                           variable=self.var_b,
                           command=self.on_var_b).grid(row=1, column=0, sticky="w", padx=5, pady=2)
            
            # Frame para entrada
            self.entrada_frame = ttk.Frame(self.campos_frame)
            self.entrada_frame.grid(row=2, column=0, columnspan=2, pady=5, padx=5, sticky="ew")
            self.atualizar_campo_entrada()
        else:
            # Demais operações
            if operacao == "Função Quadrática":
                self.criar_campos(['a', 'b', 'c', 'x'])
                self.formula.config(text="Fórmula: f(x) = ax² + bx + c")
            elif operacao == "Equação Linear":
                self.criar_campos(['a', 'b', 'x'])
                self.formula.config(text="Fórmula: ax + b = 0")
            elif operacao == "Sistema Linear":
                self.criar_campos(['a1', 'b1', 'c1', 'a2', 'b2', 'c2'])
                self.formula.config(text="Fórmula: a₁x + b₁y = c₁\na₂x + b₂y = c₂")
            elif operacao == "Progressão Aritmética":
                self.criar_campos(['a1', 'r', 'n'])
                self.formula.config(text="Fórmula: aₙ = a₁ + (n-1)r")
            elif operacao == "Progressão Geométrica":
                self.criar_campos(['a1', 'q', 'n'])
                self.formula.config(text="Fórmula: aₙ = a₁ · qⁿ⁻¹")
            elif operacao == "Área":
                self.criar_campos(['tipo', 'lado', 'base', 'altura', 'raio'])
                self.formula.config(text="Fórmula: Varia de acordo com a forma geométrica")
            elif operacao == "Volume":
                self.criar_campos(['tipo', 'lado', 'base', 'altura', 'profundidade', 'raio'])
                self.formula.config(text="Fórmula: Varia de acordo com a forma geométrica")
            elif operacao == "Perímetro":
                self.criar_campos(['tipo', 'lado', 'base', 'altura', 'raio', 'lado1', 'lado2', 'lado3'])
                self.formula.config(text="Fórmula: Varia de acordo com a forma geométrica")
            elif operacao == "Teorema de Pitágoras":
                self.criar_campos(['a', 'b', 'c'])
                self.formula.config(text="Fórmula: a² + b² = c²")
            elif operacao == "Trigonometria":
                self.criar_campos(['angulo', 'hipotenusa', 'cateto_oposto', 'cateto_adjacente'])
                self.formula.config(text="Fórmula: Sen(θ) = CO/H, Cos(θ) = CA/H, Tan(θ) = CO/CA")
            elif operacao == "Média":
                self.criar_campos(['valores'])
                self.formula.config(text="Fórmula: Σx / n")
            elif operacao == "Mediana":
                self.criar_campos(['valores'])
                self.formula.config(text="Fórmula: Valor do meio em um conjunto ordenado")
            elif operacao == "Moda":
                self.criar_campos(['valores'])
                self.formula.config(text="Fórmula: Valor mais frequente em um conjunto")
            elif operacao == "Desvio Padrão":
                self.criar_campos(['valores'])
                self.formula.config(text="Fórmula: σ = √[Σ(xᵢ - μ)² / N]")
    
    def criar_campos(self, campos):
        for i, campo in enumerate(campos):
            ttk.Label(self.campos_frame, text=campo).grid(row=i, column=0, padx=5, pady=2)
            self.entradas[campo] = ttk.Entry(self.campos_frame)
            self.entradas[campo].grid(row=i, column=1, padx=5, pady=2)
    
    def atualizar_checkboxes(self):
        # Limpar checkboxes quando mudar o tipo de produto
        self.var_a.set(False)
        self.var_b.set(False)
        self.atualizar_campo_entrada()

    def on_var_a(self):
        if self.var_a.get():
            self.var_b.set(False)
        self.atualizar_campo_entrada()

    def on_var_b(self):
        if self.var_b.get():
            self.var_a.set(False)
        self.atualizar_campo_entrada()

    def atualizar_campo_entrada(self):
        # Limpar frame de entrada
        for widget in self.entrada_frame.winfo_children():
            widget.destroy()
        # Só permite um checkbox selecionado por vez
        if self.var_a.get() and not self.var_b.get():
            ttk.Label(self.entrada_frame, text="Digite o valor de b:").grid(row=0, column=0, padx=5, pady=2)
            self.entradas['b'] = ttk.Entry(self.entrada_frame)
            self.entradas['b'].grid(row=0, column=1, padx=5, pady=2)
        elif not self.var_a.get() and self.var_b.get():
            ttk.Label(self.entrada_frame, text="Digite o valor de a:").grid(row=0, column=0, padx=5, pady=2)
            self.entradas['a'] = ttk.Entry(self.entrada_frame)
            self.entradas['a'].grid(row=0, column=1, padx=5, pady=2)
    
    def calcular(self):
        try:
            operacao = self.operacao.get()
            valores = {}
            
            if operacao == "Produtos Notáveis":
                tipo = self.tipo_produto.get()
                if not tipo:
                    raise ValueError("Selecione um tipo de produto notável")
                
                if not (self.var_a.get() or self.var_b.get()):
                    raise ValueError("Selecione pelo menos uma variável")
                
                for campo, entrada in self.entradas.items():
                    valores[campo] = float(entrada.get())
                
                if tipo == "quadrado_soma":
                    resultado = quadrado_soma(valores['a'], valores['b'])
                    self.formula.config(text="Fórmula: (a+b)² = a² + 2ab + b²")
                elif tipo == "quadrado_diferenca":
                    resultado = quadrado_diferenca(valores['a'], valores['b'])
                    self.formula.config(text="Fórmula: (a-b)² = a² - 2ab + b²")
                elif tipo == "diferenca_quadrados":
                    resultado = diferenca_quadrados(valores['a'], valores['b'])
                    self.formula.config(text="Fórmula: a²-b² = (a+b)(a-b)")
                
            elif operacao == "Função Quadrática":
                for campo, entrada in self.entradas.items():
                    valores[campo] = float(entrada.get())
                resultado = funcao_quadratica(valores['a'], valores['b'], valores['c'], valores['x'])
            elif operacao == "Equação Linear":
                resultado = equacao_linear(valores['a'], valores['b'], valores['x'])
            elif operacao == "Sistema Linear":
                resultado = sistema_linear(valores['a1'], valores['b1'], valores['c1'],
                                         valores['a2'], valores['b2'], valores['c2'])
            elif operacao == "Progressão Aritmética":
                resultado = progressao_aritmetica(valores['a1'], valores['r'], valores['n'])
            elif operacao == "Progressão Geométrica":
                resultado = progressao_geometrica(valores['a1'], valores['q'], valores['n'])
            elif operacao == "Área":
                resultado = area(valores['tipo'], **{k: v for k, v in valores.items() if k != 'tipo'})
            elif operacao == "Volume":
                resultado = volume(valores['tipo'], **{k: v for k, v in valores.items() if k != 'tipo'})
            elif operacao == "Perímetro":
                resultado = perimetro(valores['tipo'], **{k: v for k, v in valores.items() if k != 'tipo'})
            elif operacao == "Teorema de Pitágoras":
                resultado = teorema_pitagoras(valores['a'], valores['b'], valores['c'])
            elif operacao == "Trigonometria":
                resultado = trigonometria(valores['angulo'], valores['hipotenusa'],
                                        valores['cateto_oposto'], valores['cateto_adjacente'])
            elif operacao == "Média":
                resultado = media(valores['valores'])
            elif operacao == "Mediana":
                resultado = mediana(valores['valores'])
            elif operacao == "Moda":
                resultado = moda(valores['valores'])
            elif operacao == "Desvio Padrão":
                resultado = desvio_padrao(valores['valores'])
            
            self.resultado.config(text=f"Resultado: {resultado}")
            
        except ValueError as e:
            self.resultado.config(text=f"Erro: {str(e)}")
        except Exception as e:
            self.resultado.config(text=f"Erro: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraMatematica(root)
    root.mainloop()

