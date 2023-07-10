import tkinter as tk
from tkinter import ttk # themed tk
import math as mt

current_operation = "basic" # variable that stores the current operation for the change_operations function

def clear_display():
    number_input.set("")

def add_number(number):
    current = number_input.get()
    number_input.set(str(current) + str(number))

def number_negative_positive(): # inverts the sign of the number
    current = number_input.get()
    if "-" in str(current):
        number_input.set((str(current).replace("-", "")))
    else:
        number_input.set(("-" + str(current)))

def button_add():
    if number_input.get() == "" or number_input.get() == "-" or number_input.get() == "." or number_input.get() == "-.":
        return None
    else:
        first_number = float(number_input.get())
        global f_num
        global math
        math = "addition"
        f_num = first_number
        number_input.set(str(f_num) + " + ")

def button_subtract():
    if number_input.get() == "" or number_input.get() == "-" or number_input.get() == "." or number_input.get() == "-.":
        return None
    else:
        first_number = float(number_input.get())
        global f_num
        global math
        math = "subtraction"
        f_num = first_number
        number_input.set(str(f_num) + " - ")

def button_multiply():
    if number_input.get() == "" or number_input.get() == "-" or number_input.get() == "." or number_input.get() == "-.":
        return None
    else:
        first_number = float(number_input.get())
        global f_num
        global math
        math = "multiplication"
        f_num = first_number
        number_input.set(str(f_num) + " * ")

def button_divide():
    if number_input.get() == "" or number_input.get() == "-" or number_input.get() == "." or number_input.get() == "-.":
        return None
    else:
        first_number = float(number_input.get())
        global f_num
        global math
        math = "division"
        f_num = first_number
        number_input.set(str(f_num) + " / ")

def button_exponentiation():
    if number_input.get() == "" or number_input.get() == "-" or number_input.get() == "." or number_input.get() == "-.":
        return None
    else:
        first_number = float(number_input.get())
        global f_num
        global math
        math = "exponentiation"
        f_num = first_number
        number_input.set(str(f_num) + " ^ ")

def button_radication():
    if number_input.get() == "" or number_input.get() == "-" or number_input.get() == "." or number_input.get() == "-.":
        return None
    else:
        first_number = float(number_input.get())
        global f_num
        global math
        math = "radication"
        f_num = first_number
        number_input.set(str(f_num) + " √ ")

def button_percent():
    if number_input.get() == "" or number_input.get() == "-" or number_input.get() == "." or number_input.get() == "-.":
        return None
    else:
        first_number = float(number_input.get())
        global f_num
        global math
        math = "percent"
        f_num = first_number
        number_input.set(str(f_num) + " % ")

def button_fraction():
    if number_input.get() == "" or number_input.get() == "-" or number_input.get() == "." or number_input.get() == "-.":
        return None
    else:
        first_number = float(number_input.get())
        global f_num
        global math
        math = "fraction"
        f_num = first_number
        number_input.set(1 / f_num)

def button_factorial():
    if number_input.get() == "" or number_input.get() == "-" or number_input.get() == "." or number_input.get() == "-.":
        return None
    else:
        first_number = float(number_input.get())
        global f_num
        global math
        math = "factorial"
        f_num = first_number
        number_input.set(1)
        if f_num < 0:
            number_input.set("Não existe fatorial de número negativo")
        else:
            for i in range(1, int(f_num) + 1):
                number_input.set(float(number_input.get()) * i)
            if float(number_input.get()) > 1231344554367656:
                number_input.set(format(float(number_input.get()), ".2e"))

def button_log():
    if number_input.get() == "" or number_input.get() == "-" or number_input.get() == "." or number_input.get() == "-.":
        return None
    else:
        first_number = float(number_input.get())
        global f_num
        global math
        math = "log"
        f_num = first_number
        if f_num < 0:
            number_input.set("O resultado é um número complexo")
        else:
            number_input.set(mt.log(f_num, 10))

def button_equal():
    input_text = number_input.get()
    if input_text == "":
        return None
    split_text = input_text.split(" ")
    if not split_text[0].strip().isdigit() and len(split_text) == 1:
        number_input.set("Insira apenas operandos numéricos")
        return None
    elif len(split_text) < 3 or split_text[2] == "":
        number_input.set("Insira um segundo operando")
        return None
    elif not split_text[2].strip().isdigit() or split_text[0].strip().isdigit():
        number_input.set("Insira apenas operandos numéricos")
        return None
    second_number = float(split_text[2])
    number_input.set(calculate(f_num, second_number, math))

def calculate(f_num, second_number, math): # function that calculates the result
    if math == "addition":
        result = (f_num + second_number)
        return result
    if math == "subtraction":
        result = (f_num - second_number)
        return result
    if math == "multiplication":
        result = (f_num * second_number)
        return result
    if math == "division":
        result = (f_num / second_number)
        return result
    if math == "exponentiation":
        result = (f_num ** second_number)
        return result
    if math == "radication":
        result = (f_num ** (1/second_number))
        return result
    if math == "percent":
        result = (second_number * f_num / 100)
        return result

def change_operations():
    global current_operation
    if current_operation == "basic":
        btn_add.config(text="%")
        btn_add.config(command=button_percent)
        btn_sub.config(text="1/x")
        btn_sub.config(command=button_fraction)
        btn_mult.config(text="n!")
        btn_mult.config(command=button_factorial)
        btn_div.config(text="log10")
        btn_div.config(command=button_log)
        current_operation = "button"
    else:
        btn_add.config(text="+")
        btn_add.config(command=button_add)
        btn_sub.config(text="-")
        btn_sub.config(command=button_subtract)
        btn_mult.config(text="x")
        btn_mult.config(command=button_multiply)
        btn_div.config(text="/")
        btn_div.config(command=button_divide)
        current_operation = "basic"

root = tk.Tk()
root.title("Calculadora")

# style of the window
style = ttk.Style()
style.theme_use("vista")

# make the window not resizable
root.resizable(False, False)

# display
number_input = tk.StringVar()
display = ttk.Entry(root, font=("Helvetica", 14), width=35, justify="right", textvariable=number_input, state="readonly")
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipady=7)

# line 1
btn_7 = ttk.Button(root, text="7", width=10, command=lambda: add_number(7))
btn_7.grid(row=1, column=0)

btn_8 = ttk.Button(root, text="8", width=10, command=lambda: add_number(8))
btn_8.grid(row=1, column=1)

btn_9 = ttk.Button(root, text="9", width=10, command=lambda: add_number(9))
btn_9.grid(row=1, column=2)

btn_add = ttk.Button(root, text="+", width=11, command=button_add)
btn_add.grid(row=1, column=3, sticky="w")

btn_sub = ttk.Button(root, text="-", width=11, command=button_subtract)
btn_sub.grid(row=1, column=3, sticky="e")

btn_nnp = ttk.Button(root, text="+/-", width=5, command=number_negative_positive)
btn_nnp.grid(row=1, column=4, rowspan=2, sticky="nsew")

# line 2
btn_4 = ttk.Button(root, text="4", width=10, command=lambda: add_number(4))
btn_4.grid(row=2, column=0)

btn_5 = ttk.Button(root, text="5", width=10, command=lambda: add_number(5))
btn_5.grid(row=2, column=1)

btn_6 = ttk.Button(root, text="6", width=10, command=lambda: add_number(6))
btn_6.grid(row=2, column=2)

btn_mult = ttk.Button(root, text="*", width=11, command=button_multiply)
btn_mult.grid(row=2, column=3, sticky="w")

btn_div = ttk.Button(root, text="/", width=11, command=button_divide)
btn_div.grid(row=2, column=3, sticky="e")

# line 3
btn_1 = ttk.Button(root, text="1", width=10, command=lambda: add_number(1))
btn_1.grid(row=3, column=0)

btn_2 = ttk.Button(root, text="2", width=10, command=lambda: add_number(2))
btn_2.grid(row=3, column=1)

btn_3 = ttk.Button(root, text="3", width=10, command=lambda: add_number(3))
btn_3.grid(row=3, column=2)

btn_exp = ttk.Button(root, text="x^y", width=11, command=button_exponentiation)
btn_exp.grid(row=3, column=3, sticky="w")

btn_rad = ttk.Button(root, text="√^y", width=11, command=button_radication)
btn_rad.grid(row=3, column=3, sticky="e")

btn_co = ttk.Button(root, text="mode", width=5, command=change_operations)
btn_co.grid(row=3, column=4, rowspan=2, sticky="nsew")

# line 4
btn_clear = ttk.Button(root, text="Clear", width=10, command=clear_display)
btn_clear.grid(row=4, column=0, columnspan=1)

btn_0 = ttk.Button(root, text="0", width=10, command=lambda: add_number(0))
btn_0.grid(row=4, column=1)

btn_clear = ttk.Button(root, text=".", width=10, command=lambda: add_number("."))
btn_clear.grid(row=4, column=2)

btn_equal = ttk.Button(root, text="=", width=24, command=button_equal)
btn_equal.grid(row=4, column=3)

root.mainloop()
