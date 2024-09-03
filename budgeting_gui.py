import tkinter as tk
from tkinter import messagebox

# Function to calculate the balance
def calculate_balance():
    try:
        income = float(income_entry.get())
        expenses = float(expenses_entry.get())
        balance = income - expenses
        result_label.config(text=f"Balance: ${balance:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for income and expenses.")

# Function to reset the entries
def reset():
    income_entry.delete(0, tk.END)
    expenses_entry.delete(0, tk.END)
    result_label.config(text="Balance: $0.00")

# Initialize the main window
root = tk.Tk()
root.title("Budgeting App")

# Create and place the income label and entry
income_label = tk.Label(root, text="Income:")
income_label.grid(row=0, column=0, padx=10, pady=10)

income_entry = tk.Entry(root)
income_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the expenses label and entry
expenses_label = tk.Label(root, text="Expenses:")
expenses_label.grid(row=1, column=0, padx=10, pady=10)

expenses_entry = tk.Entry(root)
expenses_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_balance)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create and place the result label
result_label = tk.Label(root, text="Balance: $0.00")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create and place the reset button
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
