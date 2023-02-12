import tkinter as tk
from tkinter import ttk # themed tk

current_operation = "basic" # variable that stores the current operation for the change_operations function

def clear_display():
    number_input.set("")

def add_number(number):
    current = number_input.get()
    number_input.set(str(current) + str(number))

def number_negative_positive(): # inverts the sign of the number
    current = number_input.get()
    if "-" in str(current):
        number_input.set(str(current).replace("-", ""))
    else:
        number_input.set("-" + str(current))

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

def button_exponentiation():
    first_number = float(number_input.get())
    global f_num
    global math
    math = "exponentiation"
    f_num = first_number
    number_input.set("")

def button_radication():
    first_number = float(number_input.get())
    global f_num
    global math
    math = "radication"
    f_num = first_number
    number_input.set("")

def button_equal(): # function that calculates the result as soon as the equal button is pressed
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
    if math == "radication":
        number_input.set(f_num ** (1/second_number))

def change_operations():
    global current_operation
    if current_operation == "basic":
        btn_add.config(text="x^2")
        btn_add.config(command=button_exponentiation)
        current_operation = "exponentiation"
    else:
        btn_add.config(text="+")
        btn_add.config(command=button_add)
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

btn_div = ttk.Button(root, text="-", width=11, command=button_subtract)
btn_div.grid(row=1, column=3, sticky="e")

btn_div = ttk.Button(root, text="+/-", width=5, command=number_negative_positive)
btn_div.grid(row=1, column=4, rowspan=2, sticky="nsew")

# line 2
btn_4 = ttk.Button(root, text="4", width=10, command=lambda: add_number(4))
btn_4.grid(row=2, column=0)

btn_5 = ttk.Button(root, text="5", width=10, command=lambda: add_number(5))
btn_5.grid(row=2, column=1)

btn_6 = ttk.Button(root, text="6", width=10, command=lambda: add_number(6))
btn_6.grid(row=2, column=2)

btn_sub = ttk.Button(root, text="*", width=11, command=button_multiply)
btn_sub.grid(row=2, column=3, sticky="w")

btn_div = ttk.Button(root, text="/", width=11, command=button_divide)
btn_div.grid(row=2, column=3, sticky="e")

# line 3
btn_1 = ttk.Button(root, text="1", width=10, command=lambda: add_number(1))
btn_1.grid(row=3, column=0)

btn_2 = ttk.Button(root, text="2", width=10, command=lambda: add_number(2))
btn_2.grid(row=3, column=1)

btn_3 = ttk.Button(root, text="3", width=10, command=lambda: add_number(3))
btn_3.grid(row=3, column=2)

btn_mul = ttk.Button(root, text="x^y", width=11, command=button_exponentiation)
btn_mul.grid(row=3, column=3, sticky="w")

btn_div = ttk.Button(root, text="√^y", width=11, command=button_radication)
btn_div.grid(row=3, column=3, sticky="e")

btn_div = ttk.Button(root, text="mode", width=5, command=change_operations)
btn_div.grid(row=3, column=4, rowspan=2, sticky="nsew")

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
