"""

@Author: Pranta Sarker
Institute: North East University Bangladesh
Language: Python
Version: 3.x
Platfrom: Pycharm Community Version

"""
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("330x480")  # Ensures space for all buttons
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry Display
        entry = tk.Entry(self.root, textvariable=self.input_text, font=('Arial', 24),
                         bd=10, relief='ridge', justify='right')
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        # Buttons Grid
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                button = tk.Button(self.root, text=btn_text, font=('Arial', 18),
                                   padx=20, pady=20, width=2,
                                   command=lambda ch=btn_text: self.on_button_click(ch))
                button.grid(row=i+1, column=j, padx=5, pady=5, sticky='nsew')

        # 🔴 CLEAR Button (Row 5, full width)
        clear_btn = tk.Button(self.root, text="C", font=('Arial', 16, 'bold'),
                              bg='red', fg='white', command=self.clear)
        clear_btn.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        # Make buttons expand nicely if resizing is allowed
        for i in range(6):
            self.root.rowconfigure(i, weight=1)
        for j in range(4):
            self.root.columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result  # enable chaining
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Cannot divide by zero!")
            self.clear()
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear()

    def clear(self):
        self.expression = ""
        self.input_text.set("")


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

