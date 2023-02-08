import tkinter as tk
import math

def clear_display():
    number_input.set("")

def add_number(number):
    current = number_input.get()
    number_input.set(str(current) + str(number))

def button_add():
    first_number = float(number_input.get())
    global f_num
    global math
    math = "addition"
    f_num = first_number
    number_input.set("")

def button_subtract():
    first_number = float(number_input.get())
    global f_num
    global math
    math = "subtraction"
    f_num = first_number
    number_input.set("")

def button_multiply():
    first_number = float(number_input.get())
    global f_num
    global math
    math = "multiplication"
    f_num = first_number
    number_input.set("")

def button_divide():
    first_number = float(number_input.get())
    global f_num
    global math
    math = "division"
    f_num = first_number
    number_input.set("")

def exponentiation():
    first_number = float(number_input.get())
    global f_num
    global math
    math = "exponentiation"
    f_num = first_number
    number_input.set("")

def button_equal():
    second_number = float(number_input.get())
    number_input.set("")
    if math == "addition":
        number_input.set(f_num + second_number)
    if math == "subtraction":
        number_input.set(f_num - second_number)
    if math == "multiplication":
        number_input.set(f_num * second_number)
    if math == "division":
        number_input.set(f_num / second_number)
    if math == "exponentiation":
        number_input.set(f_num ** second_number)

root = tk.Tk()
root.title("Calculadora")

# evitar que o usuário ajuste o tamanho da janela
root.resizable(False, False)

# display
number_input = tk.StringVar()
display = tk.Entry(root, font=("Helvetica", 14), width=40, borderwidth=5, justify="right", bg="white", fg="black", textvariable=number_input, state="readonly")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=7)

# linha 1
btn_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: add_number(7))
btn_7.grid(row=1, column=0)

btn_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: add_number(8))
btn_8.grid(row=1, column=1)

btn_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: add_number(9))
btn_9.grid(row=1, column=2)

btn_add = tk.Button(root, text="+", padx=39, pady=20, command=button_add)
btn_add.grid(row=1, column=3)

# linha 2
btn_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: add_number(4))
btn_4.grid(row=2, column=0)

btn_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: add_number(5))
btn_5.grid(row=2, column=1)

btn_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: add_number(6))
btn_6.grid(row=2, column=2)

btn_sub = tk.Button(root, text="-", padx=41, pady=20, command=button_subtract)
btn_sub.grid(row=2, column=3)

# linha 3
btn_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: add_number(1))
btn_1.grid(row=3, column=0)

btn_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: add_number(2))
btn_2.grid(row=3, column=1)

btn_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: add_number(3))
btn_3.grid(row=3, column=2)

btn_mul = tk.Button(root, text="*", padx=41, pady=20, command=button_multiply)
btn_mul.grid(row=3, column=3)

# linha 4
btn_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=clear_display)
btn_clear.grid(row=4, column=0, columnspan=2)

btn_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: add_number(0))
btn_0.grid(row=4, column=2)

btn_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal)
btn_equal.grid(row=4, column=3)

root.mainloop()
