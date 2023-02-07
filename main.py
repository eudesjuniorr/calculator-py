import tkinter as tk

# graphic interface

# window
janela = tk.Tk()
janela.title("Calculadora")

# inputs
num1_entry = tk.Entry(janela)
num1_entry.grid(row=0, column=1)
num1_label = tk.Label(janela, text="Número 1")
num1_label.grid(row=0, column=0, sticky="E")

num2_entry = tk.Entry(janela)
num2_entry.grid(row=1, column=1)
num2_label = tk.Label(janela, text="Número 2")
num2_label.grid(row=1, column=0, sticky="E")

# outputs
resultado_label = tk.Label(janela, text="Resultado")
resultado_label.grid(row=2, column=0, sticky="E")

# buttons
botao_soma = tk.Button(janela, text="+", command=lambda: soma(num1_entry, num2_entry, resultado_label))
botao_soma.grid(row=0, column=2)

botao_subtracao = tk.Button(janela, text="-", command=lambda: subtracao(num1_entry, num2_entry, resultado_label))
botao_subtracao.grid(row=1, column=2)

botao_multiplicacao = tk.Button(janela, text="*", command=lambda: multiplicacao(num1_entry, num2_entry, resultado_label))
botao_multiplicacao.grid(row=0, column=3, padx=10)

botao_divisao = tk.Button(janela, text="/", command=lambda: divisao(num1_entry, num2_entry, resultado_label))
botao_divisao.grid(row=1, column=3, padx=10)

botao_radiciacao = tk.Button(janela, text="^", command=lambda: radiciacao(num1_entry, num2_entry, resultado_label))
botao_radiciacao.grid(row=2, column=2, padx=10)

# centralize the widgets
janela.columnconfigure(0, weight=3)
janela.columnconfigure(1, weight=3)
janela.columnconfigure(2, weight=3)
janela.rowconfigure(0, weight=3)
janela.rowconfigure(1, weight=3)
janela.rowconfigure(2, weight=3)
janela.rowconfigure(3, weight=3)

# definir tamanho inicial da janela
janela.geometry("300x250")

# evitar que o usuário ajuste o tamanho da janela
janela.resizable(False, False)

# functions
def soma(num1_entry, num2_entry, resultado_label):
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())
    resultado = num1 + num2
    resultado_label.config(text=resultado)
    
def subtracao(num1_entry, num2_entry, resultado_label):
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())
    resultado = num1 - num2
    resultado_label.config(text=resultado)
    
def multiplicacao(num1_entry, num2_entry, resultado_label):
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())
    resultado = num1 * num2
    resultado_label.config(text=resultado)

def divisao(num1_entry, num2_entry, resultado_label):
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())
    resultado = num1 / num2
    resultado_label.config(text=resultado)

def radiciacao(num1_entry, num2_entry, resultado_label):
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())
    resultado = num1 ** num2
    resultado_label.config(text=resultado)

# executável
janela.mainloop()
