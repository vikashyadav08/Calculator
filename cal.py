import tkinter as tk

# Function to update the expression in the text entry box
def click(button):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + button)

# Function to evaluate the final expression
def evaluate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry box for the expression
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for the calculator
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        tk.Button(root, text=button, width=8, height=2, command=evaluate).grid(row=row, column=col, columnspan=4)
    else:
        tk.Button(root, text=button, width=4, height=2, command=lambda button=button: click(button)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text='C', width=4, height=2, command=clear).grid(row=row, column=0)

# Run the application
root.mainloop()