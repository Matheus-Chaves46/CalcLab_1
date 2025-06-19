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
            'Produtos Notaveis',
            'Formula do Delta',
            'Formula de Bhaskara',
            'Função do 1 Grau',
            'Função do 2 Grau',
            'Vertice da Parabola',
            'Função Exponencial',
            'Função Logaritmica',
            'Pa Termo Geral',
            'Pa Soma dos Termos',
            'Pg Termo Geral',
            'Pg Soma dos Termos Finitos',
            'Pg Soma Infinita',
            'Relacoes Fundamentais',
            'Lei dos Senos',
            'Lei dos Cossenos',
            'Area do Triangulo',
            'Area do Circulo',
            'Volume do Cubo',
            'Volume da Esfera',
            'Volume do Cilindro',
            'Fatorial',
            'Permutacao Simples',
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
            if operacao == "Formula do Delta":
                self.criar_campos(['delta', 'b' , 'a', 'c'])
            elif operacao == "Formula de Bhaskara":
                self.criar_campos(['x', 'b', 'delta', 'a'])
            elif operacao == "Funcao do 1 Grau":
                self.criar_campos(['fx', 'ax', 'b'])
            elif operacao == "Funcao do 2 Grau":
                self.criar_campos(['fx', 'ax2', 'bx', 'c'])
            elif operacao == "Vertice da Parabola":
                self.criar_campos(['vertice_da_parabola', 'b', 'a'])
            elif operacao == "Funcao Exponencial":
                self.criar_campos(['fx', 'a', 'b', 'x'])
            elif operacao == "Funcao Logaritmica":
                self.criar_campos(['fx', 'b', 'x'])
            elif operacao == "Pa Termo Geral":
               self.criar_campos(['termo_geral', 'primeiro_termo','termo_em_sequencia', 'razao_da_pa'])
            elif operacao == "Pa Soma dos Termos":
                self.criar_campos(['soma_dos_termos', 'termos_somados', 'primeiro_termo', 'ultimo_termo'])
            elif operacao == "Pg Termo Geral":
                self.criar_campos(['termo_geral', 'primeiro_termo', 'razao_da_pg', 'termo_em_sequencia'])
            elif operacao == "Pg Soma dos Termos Finitos":
                self.criar_campos(['soma_dos_termos', 'primeiro_termo', 'razao_da_pg', 'termos_somados'])
            elif operacao == "Pg Soma Infinita":
                self.criar_campos(['soma_infinita', 'primeiro_termo', 'razao_da_pg'])
            elif operacao == "Relacoes Fundamentais":
                self.criar_campos(['#', '#', '#', '#']) #! REVISAR VARIÁVEIS 
            elif operacao == "Lei dos Senos": 
                self.criar_campos(['a', 'a_', 'b', 'b_', 'c', 'c_'])
            elif operacao == "Lei dos Cossenos":
                self.criar_campos(['a', 'a_', 'b', 'c'])
            elif operacao == "Area do Triangulo":
                self.criar_campos(['area_do_triangulo', 'base', 'altura'])
            elif operacao == "Area do Circulo":
                self.criar_campos(['area_do_circulo', 'raio'])
            elif operacao == "Volume do Cubo":
                self.criar_campos(['volume_do_cubo', 'aresta'])
            elif operacao == "Volume da Esfera":
                self.criar_campos(['volume_da_esfera', 'raio'])
            elif operacao == "Volume do Cilindro":
                self.criar_campos(['volume_do_cilindro', 'raio', 'altura'])
            elif operacao == "Fatorial":
                self.criar_campos(['n_fatorial', 'n'])
            elif operacao == "Permutacao Simples":
               self.criar_campos(['pn', 'n!'])
            elif operacao == "Combinacao Simples":
                self.criar_campos(['cnk #', 'n!', 'n', 'k']) # ! VERIFICAR VARIÁVEI)
            elif operacao == "Probabilidade":
                self.criar_campos(['probabilidade', 'casos_favoraveis', 'casos_possiveis'])
            elif operacao == "Determinante da Matriz":
                self.criar_campos(['#', '#', '#', '#']) # ! VERIFICAR VARIÁVEIS
            elif operacao == "Multiplicacao de Matriz":
                self.criar_campos(['#', '#', '#', '#']) # ! VERIFICAR VARIÁVEIS
            elif operacao == "Limite":
                self.criar_campos(['limite_fx', 'l'])
            elif operacao == "Derivada de Funcao Potencia":
                self.criar_campos(['f_x', 'n', 'x'])
    
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
                
                if tipo == "Produtos Notaveis":
                    resultado, unidades = (valores.get('a'), valores.get('b'), valores.get('c')) # !
                elif tipo == "Formula do Delta":
                    resultado, unidades = (valores.get('delta'), valores.get('b'), valores.get('a'), valores.get('c'))
                elif tipo == "Formula de Bashkara":
                    resultado, unidades = (valores.get('x'), valores.get('b'), valores.get('delta'), valores.get('a'))
                elif tipo == "Funcao do 1 Grau":
                    resultado, unidades = (valores.get('fx'), valores.get('ax'), valores.get('b'))
                elif operacao == "Funcao do 2 Grau":
                        resultado, unidades = (valores.get('fx'), valores.get('ax2'), valores.get('bx'), valores.get('c'))
                elif operacao == "Vertice de Parabola":
                    resultado, unidades = (valores.get('vertice_da_parabola'), valores.get('b'), valores.get('a'))
                elif operacao == "Funcao Exponencial":
                    resultado, unidades = (valores.get('fx'), valores.get('a'), valores.get('b'), valores.get('x'))
                elif operacao == "Funcao Logaritmica":
                    resultado, unidades = (valores.get('fx'), valores.get('b'), valores.get('x'))
                elif operacao == "Pa Termo Geral":
                    resultado, unidades = (valores.get('termo_geral'), valores.get('primeiro_termo'), valores.get('termo_em_sequencia'), valores.get('razao_da_pa'))
                elif operacao == "Pa Soma dos Termos":
                    resultado, unidades = (valores.get('soma_dos_termos'), valores.get('termos_somados'), valores.get('primeiro_termo'), valores.get('ultimo_termo'))
                elif operacao == "Pg Soma dos Termos Finitos":
                    resultado, unidades = (valores.get('soma_dos_termos'), valores.get('primeiro_termo'), valores.get('razao_da_pg'), valores.get('termos_somados'))
                elif operacao == "Pg Soma Infinita":
                    resultado, unidades = (valores.get('soma_infinita'), valores.get('primeiro_termo'), valores.get('razao_da_pg'))
                elif operacao == "Relacoes Fundamentais": #! REVISAR VARIÁVEIS
                    resultado, unidades = (valores.get('#'), valores.get('#'), valores.get('#'), valores.get('#'))
                elif operacao == "Lei dos Senos":
                    resultado, unidades = (valores.get('a'), valores.get('a_'), valores.get('b'), valores.get('b_'), valores.get('c'), valores.get('c_'))
                elif operacao == "Lei dos Cossenos":
                    resultado, unidades = (valores.get('a'), valores.get('a_'), valores.get('b'), valores.get('c'))
                elif operacao == "Area do Triangulo":
                    resultado, unidades = (valores.get('area_do_triangulo'), valores.get('base'), valores.get('altura'))
                elif operacao == "Area do Circulo":
                    resultado, unidades = (valores.get('area_do_circulo'), valores.get('raio'))
                elif operacao == "Volume do Cubo":
                    resultado, unidades = (valores.get('volume_do_cubo'), valores.get('aresta'))
                elif operacao == "Volume da Esfera":
                    resultado, unidades = (valores.get('volume_da_esfera'), valores.get('raio'))
                elif operacao == "Volume do Cilindro":
                    resultado, unidades = (valores.get('volume_do_cilindro'), valores.get('raio'), valores.get('altura'))
                elif operacao == "Fatorial":
                    resultado, unidades = (valores.get('n!'), valores.get('n'))
                elif operacao == "Permutacao Simples":
                    resultado, unidades = (valores.get('pn'), valores.get('n!'))
                elif operacao == "Combinacao Simples":
                    resultado, unidades = (valores.get('#'), valores.get('#'), valores.get('#'), valores.get('#')) # ! VERIFICAR VARIÁVEIS
                elif operacao == "Probabilidade":
                    resultado, unidades = (valores.get('probabilidade'), valores.get('casos_favoraveis'), valores.get('casos_possiveis'))
                elif operacao == "Determinante da Matriz":
                    resultado, unidades = (valores.get('#'), valores.get('#'), valores.get('#'), valores.get('#')) # ! VERIFICAR VARIÁVEIS
                elif operacao == "Multiplicacao de Matriz":
                   resultado, unidades = (valores.get('#'), valores.get('#'), valores.get('#'), valores.get('#')) # ! VERIFICAR VARIÁVEIS
                elif operacao == "Limite":
                    resultado, unidades = (valores.get('limite_fx'), valores.get('l'))
                elif operacao == "Derivada de Funcao Potencia":
                    resultado, unidades = (valores.get('f_x'), valores.get('n'), valores.get('x'))
            
            self.resultado.config(text=f"Resultado: {resultado}")
            
        except ValueError as e:
            self.resultado.config(text=f"Erro: {str(e)}")
        except Exception as e:
            self.resultado.config(text=f"Erro: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraMatematica(root)
    root.mainloop()

