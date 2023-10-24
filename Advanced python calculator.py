import tkinter as tk
import math


def evaluate_expression():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def clear():
    entry.delete(0, tk.END)


def add_to_input(char):
    entry.insert(tk.END, char)


root = tk.Tk()
root.title("Advanced Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'sqrt', 'x^2', 'C', '(', ')'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=10, height=2, command=evaluate_expression).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(root, text=button, width=10, height=2, command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, width=5, height=2, command=lambda b=button: add_to_input(b)).grid(row=row_val,
                                                                                                       column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
