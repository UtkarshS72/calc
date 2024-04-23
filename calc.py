import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '1', '2', '3', '/',
    '4', '5', '6', '*',
    '7', '8', '9', '-',
    '.', '0', '%', '+',
    '(', 'C', ')', '='
]

row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, height=2, command=calculate).grid(row=row, column=col)
    elif button == 'C':
        tk.Button(root, text=button, width=5, height=2, command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, width=5, height=2, command=lambda value=button: button_click(value)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
