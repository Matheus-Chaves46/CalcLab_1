"""
Interface da calculadora física.
"""

import tkinter as tk
from tkinter import ttk
from calc_fisica import *

class CalculadoraFisica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Física")
        
        # Frame principal
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Combobox para seleção de operação
        self.operacao = ttk.Combobox(self.frame, values=[
            "Velocidade Média",
            "Movimento Uniforme",
            "Movimento Uniformemente Variado",
            "Equação de Torricelli",
            "Princípio Fundamental da Dinâmica",
            "Força Peso",
            "Força de Atrito",
            "Trabalho da Força Constante",
            "Energia Cinética",
            "Energia Potencial",
            "Potência Média",
            "Pressão",
            "Pressão Hidrostática",
            "Empuxo",
            "Dilatação Linear",
            "Equação Fundamental da Calorimetria",
            "Primeira Lei da Termodinâmica",
            "Equação dos Espelhos e Lentes",
            "Fórmula do Aumento da Imagem",
            "Velocidade de uma Onda",
            "Lei de Ohm",
            "Potência Elétrica ou Energia Elétrica",
            "Força entre Cargas Elétricas (Lei de Coulomb)",
            "Energia Potencial Elástica",
            "Energia Mecânica"
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
        
        if operacao == "Velocidade Média":
            self.criar_campos(['velocidade_media', 'deslocamento', 'tempo'])
        elif operacao == "Movimento Uniforme":
            self.criar_campos(['movimento_uniforme', 'posicao_final', 'posicao_inicial', 'tempo', 'velocidade'])
            
        elif operacao == "Movimento Uniformemente Variado":
            self.criar_campos(['movimento_uniformemente_variado', 'posicao_final', 'posicao_inicial', 'tempo', 'velocidade_inicial', 'aceleracao'])
            
        elif operacao == "Equação de Torricelli":
            self.criar_campos(['equacao_torricelli', 'velocidade_final', 'velocidade_inicial', 'aceleracao', 'deslocamento'])
            
        elif operacao == "Princípio Fundamental da Dinâmica":
            self.criar_campos(['princípio_fundamental_da_dinâmica', 'força', 'massa', 'aceleração'])
            
        elif operacao == "Força Peso":
            self.criar_campos(['força_peso', 'massa', 'gravidade'])
            
        elif operacao == "Força de Atrito":
            self.criar_campos(['força_atrito', 'coeficiente', 'normal'])
            
        elif operacao == "Trabalho da Força Constante":
            self.criar_campos(['força', 'deslocamento', 'angulo', 'trabalho'])
            
        elif operacao == "Energia Cinética":
            self.criar_campos(['energia', 'massa', 'velocidade'])
            
        elif operacao == "Energia Potencial":
            self.criar_campos(['energia', 'massa', 'altura', 'gravidade'])
            
        elif operacao == "Potência":
            self.criar_campos(['potencia', 'trabalho', 'tempo'])
            
        elif operacao == "Pressão":
            self.criar_campos(['pressao', 'forca', 'area'])
            
        elif operacao == "Pressão Hidrostática":
            self.criar_campos(['pressao', 'densidade', 'altura', 'gravidade'])
            
        elif operacao == "Empuxo":
            self.criar_campos(['empuxo', 'densidade', 'volume', 'gravidade'])
            
        elif operacao == "Dilatação Linear":
            self.criar_campos(['comprimento_final', 'comprimento_inicial', 'coeficiente', 'variacao_de_temperatura'])
            
        elif operacao == "Energia Interna":
            self.criar_campos(['energia', 'mols', 'R', 'temperatura'])
            
        elif operacao == "Primeira Lei da Termodinâmica":
            self.criar_campos(['variacao_interna', 'trabalho', 'calor'])
            
        elif operacao == "Equação dos Espelhos e Lentes":
            self.criar_campos(['distancia_focal', 'distancia_objeto', 'distancia_imagem'])
            
        elif operacao == "Formula do Aumento da Imagem":
            self.criar_campos(['altura_imagem', 'altura_objeto', 'distancia_objeto', 'distancia_imagem'])
            
        elif operacao == "Velocidade de uma Onda":
            self.criar_campos(['velocidade', 'frequencia', 'comprimento_onda'])
            
        elif operacao == "Lei de Ohm":
            self.criar_campos(['resistencia', 'corrente', 'tensao'])
            
        elif operacao == "Potência Elétrica ou Energia Elétrica":
            self.criar_campos(['p', 'v', 'i'])
            
        elif operacao == "Força entre Cargas Elétricas (Lei de Coulomb)":
            self.criar_campos(['forca', 'k', 'q1', 'q2', 'd'])
            
        elif operacao == "Energia Potencial Elástica":
            self.criar_campos(['energia', 'constante', 'deformacao'])
        
        elif operacao == "Energia Mecânica":
            self.criar_campos(['energia', 'energia_cinetica', 'energia_potencial']) 

            
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
                valores[campo] = float(entrada.get())
            
            if operacao == "Velocidade Média":
                resultado = velocidade_media(valores['velocidade_media'], valores['deslocamento'], valores['tempo'])
            elif operacao == "Movimento Uniforme":
                resultado = movimento_uniforme(valores['posicao_final'], valores['posicao_inicial'], valores['tempo'], valores['velocidade'])
            elif operacao == "Movimento Uniformemente Variado":
                resultado = movimento_uniformemente_variado(valores['posicao_final'], valores['posicao_inicial'], valores['tempo'], valores['velocidade_inicial'], valores['aceleracao'])
            elif operacao == "Equação de Torricelli":
                resultado = equacao_torricelli(valores['velocidade_final'], valores['velocidade_inicial'], valores['aceleracao'], valores['deslocamento'])
            elif operacao == "Princípio Fundamental da Dinâmica":
                resultado = principio_fundamental_dinamica(valores['força'], valores['massa'], valores['aceleração'])
            elif operacao == "Força Peso":
                resultado = forca_peso(valores['forca_peso'], valores['massa'], valores['gravidade'])
            elif operacao == "Força de Atrito":
                resultado = forca_atrito(valores['forca_atrito'], valores['coeficiente'], valores['normal'])
            elif operacao == "Trabalho da Força Constante":
                resultado = trabalho_forca_constante(valores['trabalho'], valores['forca'], valores['deslocamento'], valores['angulo'])
            elif operacao == "Energia Cinética":
                resultado = energia_cinetica(valores['energia_cinetica'], valores['massa'], valores['velocidade'])
            elif operacao == "Energia Potencial":
                resultado = energia_potencial(valores['energia_potencial'], valores['massa'], valores['altura'], valores['gravidade'])
            elif operacao == "Potência":
                resultado = potencia(valores['potencia'], valores['trabalho'], valores['tempo'])
            elif operacao == "Pressão":
                resultado = pressao(valores['pressao'], valores['forca'], valores['area'])
            elif operacao == "Pressão Hidrostática":
                resultado = pressao_hidrostatica(valores['pressao_hidrostatica'], valores['densidade'], valores['altura'], valores['gravidade'])
            elif operacao == "Empuxo":
                resultado = empuxo(valores['empuxo'], valores['densidade'], valores['volume'], valores['gravidade'])
            elif operacao == "Dilatação Linear":
                resultado = dilatacao_linear(valores['comprimento_final'], valores['comprimento_inicial'], valores['coeficiente'], valores['variacao_de_temperatura'])
            elif operacao == "Energia Interna":
                resultado = primeira_lei_termodinamica(valores['variacao_interna'], valores['trabalho'], valores['calor'])
            elif operacao == "Equação dos Espelhos e Lentes":
                resultado = equacao_dos_espelhos_e_lentes(valores['distancia_focal'], valores['distancia_objeto'], valores['distancia_imagem'])
            elif operacao == "Formula do Aumento da Imagem":
                resultado = formula_do_aumento_da_imagem(valores['altura_imagem'], valores['altura_objeto'], valores['distancia_objeto'], valores['distancia_imagem'])
            elif operacao == "Velocidade de uma Onda":
                resultado = velocidade_onda(valores['velocidade_onda'], valores['frequencia'], valores['comprimento_onda'])
            elif operacao == "Lei de Ohm":
                resultado = lei_ohm(valores['lei_ohm'], valores['resistencia'], valores['corrente'], valores['tensao'])
            elif operacao == "Potência Elétrica ou Energia Elétrica":
                resultado = potencia_eletrica(valores['potencia_eletrica'], valores['p'], valores['v'], valores['i'])
            elif operacao == "Força entre Cargas Elétricas (Lei de Coulomb)":
                resultado = forca_entre_cargas_eletricas(valores['forca_entre_cargas_eletricas'], valores['k'], valores['q1'], valores['q2'], valores['d'])
            elif operacao == "Energia Potencial Elástica":
                resultado = energia_potencial_elastica(valores['energia_potencial_elastica'], valores['constante'], valores['deformacao'])
            elif operacao == "Energia Mecânica":
                resultado = energia_mecanica(valores['energia_mecanica'], valores['energia_cinetica'], valores['energia_potencial'])
            
            self.resultado.config(text=f"Resultado: {resultado}")
            
        except ValueError as e:
            self.resultado.config(text=f"Erro: {str(e)}")
        except Exception as e:
            self.resultado.config(text=f"Erro: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraFisica(root)
    root.mainloop()