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
            "Velocidade Media",
            "Movimento Uniforme",
            "Movimento Uniformemente Variado",
            "Equacao de Torricelli",
            "Principio Fundamental da Dinamica",
            "Forca Peso",
            "Forca de Atrito",
            "Trabalho da Forca Constante",
            "Energia Cinetica",
            "Energia Potencial",
            "Potencia Media",
            "Pressao",
            "Pressao Hidrostatica",
            "Empuxo",
            "Dilatacao Linear",
            "Equacao Fundamental da Calorimetria",
            "Primeira Lei da Termodinamica",
            "Equacao dos Espelhos e Lentes",
            "Aumento da Imagem",
            "Velocidade de uma Onda",
            "Lei de Ohm",
            "Potencia Eletrica ou Energia Eletrica",
            "Forca entre Cargas Eletricas (Lei de Coulomb)",
            "Energia Potencial Elastica",
            "Energia Mecanica"
        ])
        self.operacao.grid(row=0, column=0, columnspan=2, pady=5)
        self.operacao.set("Velocidade Media")
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
        
        if operacao == "Velocidade Media":
            self.criar_campos(['velocidade_media', 'deslocamento', 'tempo'])
            self.formula.config(text="Fórmula: v = Δs/Δt")
        elif operacao == "Movimento Uniforme":
            self.criar_campos(['movimento_uniforme', 'posicao_final', 'posicao_inicial', 'tempo', 'velocidade'])
            self.formula.config(text="Fórmula: S = S₀ + v·t")
        elif operacao == "Movimento Uniformemente Variado":
            self.criar_campos(['movimento_uniformemente_variado', 'posicao_final', 'posicao_inicial', 'tempo', 'velocidade_inicial', 'aceleracao'])
            self.formula.config(text="Fórmula: S = S₀ + v₀·t + (a·t²)/2")
        elif operacao == "Equacao de Torricelli":
            self.criar_campos(['equacao_torricelli', 'velocidade_final', 'velocidade_inicial', 'aceleracao', 'deslocamento'])
            self.formula.config(text="Fórmula: v² = v₀² + 2·a·ΔS")
        elif operacao == "Principio Fundamental da Dinamica":
            self.criar_campos(['principio_fundamental_da_dinamica', 'forca', 'massa', 'aceleracao'])
            self.formula.config(text="Fórmula: F = m·a")
        elif operacao == "Forca Peso":
            self.criar_campos(['forca_peso', 'massa', 'gravidade'])
            self.formula.config(text="Fórmula: P = m·g")
        elif operacao == "Forca de Atrito":
            self.criar_campos(['forca_atrito', 'coeficiente', 'normal'])
            self.formula.config(text="Fórmula: Fₐ = μ·N")
        elif operacao == "Trabalho da Forca Constante":
            self.criar_campos(['forca', 'deslocamento', 'angulo', 'trabalho'])
            self.formula.config(text="Fórmula: τ = F·d·cos(θ)")
        elif operacao == "Energia Cinetica":
            self.criar_campos(['energia_cinetica', 'massa', 'velocidade'])
            self.formula.config(text="Fórmula: Eₖ = (m·v²)/2")
        elif operacao == "Energia Potencial":
            self.criar_campos(['energia_potencial', 'massa', 'altura', 'gravidade'])
            self.formula.config(text="Fórmula: Eₚ = m·g·h")
        elif operacao == "Potencia Media":
            self.criar_campos(['potencia_media', 'trabalho', 'tempo'])
            self.formula.config(text="Fórmula: P = τ/Δt")
        elif operacao == "Pressao":
            self.criar_campos(['pressao', 'forca', 'area'])
            self.formula.config(text="Fórmula: p = F/A")
        elif operacao == "Pressao Hidrostatica":
            self.criar_campos(['pressao_hidrostatica', 'densidade', 'altura', 'gravidade'])
            self.formula.config(text="Fórmula: p = ρ·g·h")
        elif operacao == "Empuxo":
            self.criar_campos(['empuxo', 'densidade', 'volume', 'gravidade'])
            self.formula.config(text="Fórmula: E = ρ·V·g")
        elif operacao == "Dilatacao Linear":
            self.criar_campos(['dilatacao_linear', 'coeficiente_dilatacao', 'comprimento_inicial', 'variacao_de_temperatura'])
            self.formula.config(text="Fórmula: L = L₀·(1 + α·ΔT)")
        elif operacao == "Equacao Fundamental da Calorimetria":
            self.criar_campos(['calor', 'massa', 'calor_especifico', 'variacao_temperatura'])
            self.formula.config(text="Fórmula: Q = m·c·ΔT")
        elif operacao == "Primeira Lei da Termodinamica":
            self.criar_campos(['variacao_interna', 'trabalho', 'calor'])
            self.formula.config(text="Fórmula: ΔU = Q - τ")
        elif operacao == "Equacao dos Espelhos e Lentes":
            self.criar_campos(['distancia_focal', 'distancia_objeto', 'distancia_imagem'])
            self.formula.config(text="Fórmula: 1/f = 1/p + 1/p'")
        elif operacao == "Aumento da Imagem":
            self.criar_campos(['aumento_da_imagem', 'distancia_objeto', 'distancia_imagem'])
            self.formula.config(text="Fórmula: A = -i/o")
        elif operacao == "Velocidade de uma Onda":
            self.criar_campos(['velocidade_onda', 'frequencia', 'comprimento_onda'])
            self.formula.config(text="Fórmula: v = λ·f")
        elif operacao == "Lei de Ohm":
            self.criar_campos(['resistencia', 'corrente', 'tensao'])
            self.formula.config(text="Fórmula: R = U/i")
        elif operacao == "Potencia Eletrica ou Energia Eletrica":
            self.criar_campos(['potencia_eletrica', 'tensao', 'corrente'])
            self.formula.config(text="Fórmula: P = U·i")
        elif operacao == "Forca entre Cargas Eletricas (Lei de Coulomb)":
            self.criar_campos(['forca_coulomb', 'constante', 'carga1', 'carga2', 'distancia'])
            self.formula.config(text="Fórmula: F = k·|q₁·q₂|/r²")
        elif operacao == "Energia Potencial Elastica":
            self.criar_campos(['energia_potencial_elastica', 'constante_elastica', 'deformacao'])
            self.formula.config(text="Fórmula: Eₚ = (k·x²)/2")
        elif operacao == "Energia Mecanica":
            self.criar_campos(['energia_mecanica', 'energia_cinetica', 'energia_potencial'])
            self.formula.config(text="Fórmula: Eₘ = Eₖ + Eₚ")
    
    def criar_campos(self, campos):
        for i, campo in enumerate(campos):
            ttk.Label(self.campos_frame, text=campo.replace('_', ' ').title()).grid(row=i, column=0, padx=5, pady=2)
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
            
            if operacao == "Velocidade Media":
                resultado, unidades = velocidade_media(valores.get('velocidade_media'), valores.get('deslocamento'), valores.get('tempo'))
            elif operacao == "Movimento Uniforme":
                resultado, unidades = movimento_uniforme(valores.get('posicao_final'), valores.get('posicao_inicial'), valores.get('tempo'), valores.get('velocidade'))
            elif operacao == "Movimento Uniformemente Variado":
                resultado, unidades = movimento_uniformemente_variado(valores.get('posicao_final'), valores.get('posicao_inicial'), valores.get('tempo'), valores.get('velocidade_inicial'), valores.get('aceleracao'))
            elif operacao == "Equacao de Torricelli":
                resultado, unidades = equacao_torricelli(valores.get('velocidade_final'), valores.get('velocidade_inicial'), valores.get('aceleracao'), valores.get('deslocamento'))
            elif operacao == "Principio Fundamental da Dinamica":
                resultado, unidades = principio_fundamental_dinamica(valores.get('forca'), valores.get('massa'), valores.get('aceleracao'))
            elif operacao == "Forca Peso":
                resultado, unidades = forca_peso(valores.get('forca_peso'), valores.get('massa'), valores.get('gravidade'))
            elif operacao == "Forca de Atrito":
                resultado, unidades = forca_atrito(valores.get('forca_atrito'), valores.get('coeficiente'), valores.get('normal'))
            elif operacao == "Trabalho da Forca Constante":
                resultado, unidades = trabalho_forca_constante(valores.get('trabalho'), valores.get('forca'), valores.get('deslocamento'), valores.get('angulo'))
            elif operacao == "Energia Cinetica":
                resultado, unidades = energia_cinetica(valores.get('energia_cinetica'), valores.get('massa'), valores.get('velocidade'))
            elif operacao == "Energia Potencial":
                resultado, unidades = energia_potencial(valores.get('energia_potencial'), valores.get('massa'), valores.get('altura'), valores.get('gravidade'))
            elif operacao == "Potencia Media":
                resultado, unidades = potencia(valores.get('potencia_media'), valores.get('trabalho'), valores.get('tempo'))
            elif operacao == "Pressao":
                resultado, unidades = pressao(valores.get('pressao'), valores.get('forca'), valores.get('area'))
            elif operacao == "Pressao Hidrostatica":
                resultado, unidades = pressao_hidrostatica(valores.get('pressao_hidrostatica'), valores.get('densidade'), valores.get('altura'), valores.get('gravidade'))
            elif operacao == "Empuxo":
                resultado, unidades = empuxo(valores.get('empuxo'), valores.get('densidade'), valores.get('volume'), valores.get('gravidade'))
            elif operacao == "Dilatacao Linear":
                resultado, unidades = dilatacao_linear(valores.get('coeficiente_dilatacao'), valores.get('comprimento_inicial'), valores.get('dilatacao_linear'), valores.get('variacao_de_temperatura'))
            elif operacao == "Equacao Fundamental da Calorimetria":
                resultado, unidades = equacao_fundamental_calorimetria(valores.get('calor'), valores.get('massa'), valores.get('calor_especifico'), valores.get('variacao_temperatura'))
            elif operacao == "Primeira Lei da Termodinamica":
                resultado, unidades = primeira_lei_termodinamica(valores.get('variacao_interna'), valores.get('trabalho'), valores.get('calor'))
            elif operacao == "Equacao dos Espelhos e Lentes":
                resultado, unidades = equacao_dos_espelhos_e_lentes(valores.get('distancia_focal'), valores.get('distancia_objeto'), valores.get('distancia_imagem'))
            elif operacao == "Aumento da Imagem":
                resultado, unidades = aumento_da_imagem(valores.get('aumento_da_imagem'), valores.get('distancia_objeto_a'), valores.get('distancia_imagem_a'))
            elif operacao == "Velocidade de uma Onda":
                resultado, unidades = velocidade_onda(valores.get('velocidade_onda'), valores.get('frequencia'), valores.get('comprimento_onda'))
            elif operacao == "Lei de Ohm":
                resultado, unidades = lei_ohm(valores.get('resistencia'), valores.get('corrente'), valores.get('tensao'))
            elif operacao == "Potencia Eletrica ou Energia Eletrica":
                resultado, unidades = potencia_eletrica(valores.get('potencia_eletrica'), valores.get('tensao'), valores.get('corrente'))
            elif operacao == "Forca entre Cargas Eletricas (Lei de Coulomb)":
                resultado, unidades = forca_entre_cargas_eletricas(valores.get('forca_coulomb'), valores.get('carga1'), valores.get('carga2'), valores.get('distancia'))
            elif operacao == "Energia Potencial Elastica":
                resultado, unidades = energia_potencial_elastica(valores.get('energia_potencial_elastica'), valores.get('constante_elastica'), valores.get('deformacao'))
            elif operacao == "Energia Mecanica":
                resultado, unidades = energia_mecanica(valores.get('energia_mecanica'), valores.get('energia_cinetica'), valores.get('energia_potencial'))
            
            # Formatar o resultado com a unidade
            resultado_formatado = ""
            for variavel, valor in resultado.items():
                unidade = unidades[variavel]
                resultado_formatado += f"{variavel.replace('_', ' ').title()}: {valor:.10f} {unidade}\n"
            
            self.resultado.config(text=resultado_formatado.strip())
            
        except ValueError as e:
            self.resultado.config(text=f"Erro: {str(e)}")
        except Exception as e:
            self.resultado.config(text=f"Erro: {str(e)}")