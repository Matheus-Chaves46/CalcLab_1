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
            'Pureza',
            'Rendimento',
            'Excesso',
            'Quantidade de Reagentes Necessario',
            'Balanceamento',
            'Gases',
            'Tabela Periodica',
            'Pilha de Daniels',
            'Termoquimica',
            'Equilíbrio Quimico'
        ])
        self.operacao.grid(row=0, column=0, columnspan=2, pady=5)
        self.operacao.set("Pureza")
        self.operacao.bind('<<ComboboxSelected>>', self.atualizar_campos)
        self.atualizar_campos()
        
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
        
        # Label para fórmula
        self.formula = ttk.Label(self.frame, text="")
        self.formula.grid(row=4, column=0, columnspan=2, pady=5)
    
    def atualizar_campos(self, event=None):
        # Limpar campos existentes
        for widget in self.campos_frame.winfo_children():
            widget.destroy()
        self.entradas.clear()
        
        operacao = self.operacao.get()
        
        if operacao == "Pureza":
            self.criar_campos(['pureza', 'massa_da_substancia_pura', 'massa_da_substancia_amostra'])
            self.formula.config(text="Fórmula:")
        elif operacao == "Rendimento":
            self.criar_campos(['rendimento', 'rendimento_real', 'rendimento_teorico'])
            self.formula.config(text="Fórmula:")
        elif operacao == "Excesso":
            self.criar_campos(['equacao_reagentes', 'equacao_produtos', 'massa_disponivel'])
            self.formula.config(text="Fórmula:")
        elif operacao == "Quantidade Reagente Necessario":
            self.criar_campos(['equacao_reagentes', 'equacao_produtos', 'massa_dos_produtos_desejada'])
            self.formula.config(text="Fórmula:")
        elif operacao == "Balanceamento":
            self.criar_campos(['equacao_reagentes', 'equacao_produtos'])
            self.formula.config(text="Fórmula:")
        elif operacao == "Gases":
            self.criar_campos(['pressao', 'volume', 'numero_mols', 'temperatura'])
            self.formula.config(text="Fórmula:")
        elif operacao == "Tabela Periodica":
            self.criar_campos(['elemento'])
            self.formula.config(text="Fórmula:")
        elif operacao == "Pilha de Daniels":
            self.criar_campos(['equacao_reagentes', 'equacao_produtos', 'concentracao_dos_produtos', 'concentracao_dos_reagentes'])
            self.formula.config(text="Fórmula:")
        elif operacao == "Termoquimica":
            self.criar_campos(['delta_h', 'entalpia_dos_produtos', 'entalpia_dos_reagentes'])
            self.formula.config(text="Fórmula:")
        elif operacao == "Equilibrio Quimico":
            self.criar_campos(['acido_ou_base', 'constante_de_equilibrio', 'concentracao_incial'])
            self.formula.config(text="Fórmula:")
    
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
                valor = entrada.get()
                if valor:  # Só adiciona se o campo não estiver vazio
                    valores[campo] = float(valor)
            
            if operacao == "Pureza":
                resultado, unidades = pureza(valores.get('pureza'), valores.get('massa_da_substancia_pura'), valores.get('massa_da_substancia_amostra'))
            elif operacao == "Rendimento":
                resultado, unidades = rendimento(valores.get('rendimento'), valores.get('rendimento_real'), valores.get('rendimento_teorico'))
            elif operacao == "Excesso":
                resultado, unidades = excesso(valores.get('excesso'), valores.get('quantidade_incial_reagentes'), valores.get('quantidade_reagentes_reagidos'))
            elif operacao == "Quantidade de Reagentes Necessario":
                resultado, unidades = quantidade_de_reagentes_necessario(valores.get('equacao_reagentes'), valores.get('equacao_produtos'), valores.get('massa_dos_produtos_desejada'))
            elif operacao == "Balanceamento":
                resultado, unidades = balanceamento(valores.get('equacao_reagentes'), valores.get('equacao_produtos'))
            elif operacao == "Gases":
                resultado, unidades = gases(valores.get('pressao'), valores.get('volume'), valores.get('numero_de_mols'), valores.get('temperatura'))
            elif operacao == "Tabela Periodica":
                resultado, unidades = tabela_periodica(valores.get('elemento'))
            elif operacao == "Pilha de Daniels":
                resultado, unidades = pilha_de_daniels(valores.get('equacao_reagentes'), valores.get('equacao_produtos'), valores.get('concentracao_dos_produtos'), valores.get('concentracao_dos_reagentes'))
            elif operacao == "Termoquimica":
                resultado, unidades = termoquimica(valores.get('delta_h'), valores.get('entalpia_dos_produtos'), valores.get('entalpia_dos_reagentes'))
            elif operacao == "Equilibrio Quimico":
                resultado, unidades = equilibrio_ionico(valores.get('acido_ou_base'), valores.get('constante_de_equilibrio'), valores.get('concentracao_inicial'))
            
            # Formatar o resultado com a unidade
            resultado_formatado = ""
            for variavel, valor in resultado.items():
                unidade = unidades[variavel]
                resultado_formatado += f"{variavel.replace('_', ' ').title()}: {valor:.10f} {unidade}\n"
                
            self.resultado.config(text=f"Resultado: {resultado}")
            
        except ValueError as e:
            self.resultado.config(text=f"Erro: {str(e)}")
        except Exception as e:
            self.resultado.config(text=f"Erro: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraQuimica(root)
    root.mainloop()