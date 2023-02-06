import tkinter as tk

# graphic interface

# window
janela = tk.Tk()
janela.title("Calculadora")

# inputs
num1_entry = tk.Entry(janela)
num1_entry.grid(row=0, column=0, padx=10, pady=10)

num2_entry = tk.Entry(janela)
num2_entry.grid(row=1, column=0, padx=10, pady=10)

# outputs
resultado_label = tk.Label(janela, text="Resultado")
resultado_label.grid(row=2, column=0, padx=10, pady=10)

# buttons
botao_soma = tk.Button(janela, text="+", command=lambda: soma(num1_entry, num2_entry, resultado_label))
botao_soma.grid(row=0, column=1)

botao_subtracao = tk.Button(janela, text="-", command=lambda: subtracao(num1_entry, num2_entry, resultado_label))
botao_subtracao.grid(row=0, column=2)

botao_multiplicacao = tk.Button(janela, text="*", command=lambda: multiplicacao(num1_entry, num2_entry, resultado_label))
botao_multiplicacao.grid(row=1, column=1)

botao_divisao = tk.Button(janela, text="/", command=lambda: divisao(num1_entry, num2_entry, resultado_label))
botao_divisao.grid(row=1, column=2)

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
    
# executável
janela.mainloop()
