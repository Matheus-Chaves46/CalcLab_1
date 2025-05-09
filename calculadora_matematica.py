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
            "Função Quadrática",
            "Equação Linear",
            "Sistema Linear",
            "Progressão Aritmética",
            "Progressão Geométrica",
            "Área",
            "Volume",
            "Perímetro",
            "Teorema de Pitágoras",
            "Trigonometria",
            "Média",
            "Mediana",
            "Moda",
            "Desvio Padrão"
        ])
        self.operacao.grid(row=0, column=0, columnspan=2, pady=5)
        self.operacao.bind('<<ComboboxSelected>>', self.atualizar_campos)
        
        # Frame para campos de entrada
        self.campos_frame = ttk.Frame(self.frame)
        self.campos_frame.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Campos de entrada
        self.entradas = {}
        
        # Botão de cálculo
        self.calcular_btn = ttk.Button(self.frame, text="Calcular", command=self.calcular)
        self.calcular_btn.grid(row=2, column=0, columnspan=2, pady=5)
        
        # Label para resultado
        self.resultado = ttk.Label(self.frame, text="")
        self.resultado.grid(row=3, column=0, columnspan=2, pady=5)
    
    def atualizar_campos(self, event=None):
        # Limpar campos existentes
        for widget in self.campos_frame.winfo_children():
            widget.destroy()
        self.entradas.clear()
        
        operacao = self.operacao.get()
        
        if operacao == "Função Quadrática":
            self.criar_campos(['a', 'b', 'c', 'x'])
        elif operacao == "Equação Linear":
            self.criar_campos(['a', 'b', 'x'])
        elif operacao == "Sistema Linear":
            self.criar_campos(['a1', 'b1', 'c1', 'a2', 'b2', 'c2'])
        elif operacao == "Progressão Aritmética":
            self.criar_campos(['a1', 'r', 'n'])
        elif operacao == "Progressão Geométrica":
            self.criar_campos(['a1', 'q', 'n'])
        elif operacao == "Área":
            self.criar_campos(['tipo', 'lado', 'base', 'altura', 'raio'])
        elif operacao == "Volume":
            self.criar_campos(['tipo', 'lado', 'base', 'altura', 'profundidade', 'raio'])
        elif operacao == "Perímetro":
            self.criar_campos(['tipo', 'lado', 'base', 'altura', 'raio', 'lado1', 'lado2', 'lado3'])
        elif operacao == "Teorema de Pitágoras":
            self.criar_campos(['a', 'b', 'c'])
        elif operacao == "Trigonometria":
            self.criar_campos(['angulo', 'hipotenusa', 'cateto_oposto', 'cateto_adjacente'])
        elif operacao == "Média":
            self.criar_campos(['valores'])
        elif operacao == "Mediana":
            self.criar_campos(['valores'])
        elif operacao == "Moda":
            self.criar_campos(['valores'])
        elif operacao == "Desvio Padrão":
            self.criar_campos(['valores'])
    
    def criar_campos(self, campos):
        for i, campo in enumerate(campos):
            ttk.Label(self.campos_frame, text=campo).grid(row=i, column=0, padx=5, pady=2)
            self.entradas[campo] = ttk.Entry(self.campos_frame)
            self.entradas[campo].grid(row=i, column=1, padx=5, pady=2)
    
    def calcular(self):
        try:
            operacao = self.operacao.get()
            valores = {}
            
            for campo, entrada in self.entradas.items():
                if campo == 'valores':
                    valores[campo] = [float(x) for x in entrada.get().split(',')]
                else:
                    valores[campo] = float(entrada.get())
            
            if operacao == "Função Quadrática":
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

