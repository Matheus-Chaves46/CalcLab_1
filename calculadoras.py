"""
Interface principal das calculadoras.
"""

import tkinter as tk
from tkinter import ttk
from calculadora_matematica import CalculadoraMatematica
from calculadora_quimica import CalculadoraQuimica
from calculadora_fisica import CalculadoraFisica

class Calculadoras:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadoras")
        
        # Frame principal
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Botões para cada calculadora
        ttk.Button(self.frame, text="Calculadora Matemática",
                  command=self.abrir_calculadora_matematica).grid(row=0, column=0, pady=5)
        
        ttk.Button(self.frame, text="Calculadora Química",
                  command=self.abrir_calculadora_quimica).grid(row=1, column=0, pady=5)
        
        ttk.Button(self.frame, text="Calculadora Física",
                  command=self.abrir_calculadora_fisica).grid(row=2, column=0, pady=5)
    
    def abrir_calculadora_matematica(self):
        janela = tk.Toplevel(self.root)
        CalculadoraMatematica(janela)
    
    def abrir_calculadora_quimica(self):
        janela = tk.Toplevel(self.root)
        CalculadoraQuimica(janela)
    
    def abrir_calculadora_fisica(self):
        janela = tk.Toplevel(self.root)
        CalculadoraFisica(janela)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadoras(root)
    root.mainloop()
