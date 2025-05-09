"""
Interface da calculadora química.
"""

import tkinter as tk
from tkinter import ttk
from calc_quimica import *

class CalculadoraQuimica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Química")
        
        # Frame principal
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Combobox para seleção de operação
        self.operacao = ttk.Combobox(self.frame, values=[
            "Massa Molar",
            "Concentração Molar",
            "pH",
            "pOH",
            "Constante de Equilíbrio",
            "Energia Livre de Gibbs",
            "Lei de Henry",
            "Razão Molar",
            "Rendimento Teórico",
            "Pressão Osmótica"
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
        
        if operacao == "Massa Molar":
            self.criar_campos(['formula'])
        elif operacao == "Concentração Molar":
            self.criar_campos(['mols', 'volume'])
        elif operacao == "pH":
            self.criar_campos(['concentracao_h'])
        elif operacao == "pOH":
            self.criar_campos(['concentracao_oh'])
        elif operacao == "Constante de Equilíbrio":
            self.criar_campos(['produtos', 'reagentes'])
        elif operacao == "Energia Livre de Gibbs":
            self.criar_campos(['entalpia', 'entropia', 'temperatura'])
        elif operacao == "Lei de Henry":
            self.criar_campos(['pressao', 'constante_henry'])
        elif operacao == "Razão Molar":
            self.criar_campos(['mols_reagente', 'mols_produto'])
        elif operacao == "Rendimento Teórico":
            self.criar_campos(['mols_obtidos', 'mols_esperados'])
        elif operacao == "Pressão Osmótica":
            self.criar_campos(['concentracao', 'temperatura'])
    
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
                if campo in ['produtos', 'reagentes']:
                    # Converter string de dicionário para dicionário
                    valores[campo] = eval(entrada.get())
                else:
                    valores[campo] = float(entrada.get())
            
            if operacao == "Massa Molar":
                resultado = massa_molar(valores['formula'])
            elif operacao == "Concentração Molar":
                resultado = concentracao_molar(valores['mols'], valores['volume'])
            elif operacao == "pH":
                resultado = ph(valores['concentracao_h'])
            elif operacao == "pOH":
                resultado = poh(valores['concentracao_oh'])
            elif operacao == "Constante de Equilíbrio":
                resultado = constante_equilibrio(valores['produtos'], valores['reagentes'])
            elif operacao == "Energia Livre de Gibbs":
                resultado = energia_livre_gibbs(valores['entalpia'], valores['entropia'], valores['temperatura'])
            elif operacao == "Lei de Henry":
                resultado = lei_henry(valores['pressao'], valores['constante_henry'])
            elif operacao == "Razão Molar":
                resultado = razao_molar(valores['mols_reagente'], valores['mols_produto'])
            elif operacao == "Rendimento Teórico":
                resultado = rendimento_teorico(valores['mols_obtidos'], valores['mols_esperados'])
            elif operacao == "Pressão Osmótica":
                resultado = pressao_osmotica(valores['concentracao'], valores['temperatura'])
            
            self.resultado.config(text=f"Resultado: {resultado}")
            
        except ValueError as e:
            self.resultado.config(text=f"Erro: {str(e)}")
        except Exception as e:
            self.resultado.config(text=f"Erro: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraQuimica(root)
    root.mainloop()