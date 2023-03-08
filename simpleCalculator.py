import tkinter as tk
from tkinter import ttk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.expression = ""

        # Create display label
        self.display_label = ttk.Label(master, text="", font=("Arial", 32))
        self.display_label.grid(row=0, column=0, columnspan=4, pady=5)

        # Create buttons
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button("C", 5, 0)

        # Set up event bindings for buttons
        self.master.bind("<Key>", self.key_press)
        self.master.bind("<Return>", self.evaluate)
        self.master.bind("<BackSpace>", self.delete)

    def create_button(self, text, row, column):
        button = ttk.Button(self.master, text=text, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5, ipadx=10, ipady=10)

    def button_click(self, text):
        if text == "C":
            self.expression = ""
            self.display_label.configure(text="")
        elif text == "=":
            self.evaluate(None)
        else:
            self.expression += text
            self.display_label.configure(text=self.expression)

    def key_press(self, event):
        if event.char.isdigit() or event.char in ["+", "-", "*", "/", ".", "%"]:
            self.expression += event.char
            self.display_label.configure(text=self.expression)
        elif event.char == "\r":
            self.evaluate(None)
        elif event.char == "\x08":
            self.delete(None)

    def delete(self, event):
        self.expression = self.expression[:-1]
        self.display_label.configure(text=self.expression)

    def evaluate(self, event):
        try:
            self.expression = str(eval(self.expression))
            self.display_label.configure(text=self.expression)
        except:
            self.display_label.configure(text="Error")
            self.expression = ""
            

root = tk.Tk()
app = Calculator(root)

# Automatically resize window to fit all buttons
root.update()
width = root.winfo_width()
height = root.winfo_height()
root.minsize(width, height)

root.mainloop()
