#CÓDIGO PARA RESOLVER EQUAÇÃO DE 2° GRAU COM INTERFACE GRÁFICA UTILIZANDO TKINTER

import tkinter as tk
from tkinter import messagebox

def calcular_delta(a, b, c):
    return b ** 2 - 4 * a * c

def calcular():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            messagebox.showerror("Erro", 'O valor de "a" deve ser diferente de 0.')
            return

        delta = calcular_delta(a, b, c)

        if delta < 0:
            resultado.set("Não possui raízes reais.")
        else:
            x1 = (-b + delta**0.5) / (2 * a)
            x2 = (-b - delta**0.5) / (2 * a)
            resultado.set(f"Δ = {delta:.2f}\nX₁ = {x1:.2f}\nX₂ = {x2:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Insira apenas números.")

# Criação da interface
janela = tk.Tk()
janela.title("Equação do 2º Grau")

tk.Label(janela, text="Valor de a:").grid(row=0, column=0)
entry_a = tk.Entry(janela)
entry_a.grid(row=0, column=1)

tk.Label(janela, text="Valor de b:").grid(row=1, column=0)
entry_b = tk.Entry(janela)
entry_b.grid(row=1, column=1)

tk.Label(janela, text="Valor de c:").grid(row=2, column=0)
entry_c = tk.Entry(janela)
entry_c.grid(row=2, column=1)

tk.Button(janela, text="Calcular", command=calcular).grid(row=3, column=0, columnspan=2, pady=10)

resultado = tk.StringVar()
tk.Label(janela, textvariable=resultado, fg="blue").grid(row=4, column=0, columnspan=2)

janela.mainloop()
