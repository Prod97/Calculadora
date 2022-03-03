import tkinter as tk
from tkinter import ttk


class Frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root, bg="#8c8c8c")
        self.grid()
        self.texto_pantalla = tk.StringVar()
        self.ventana()
        self.operadores = ""

        
    def clean_window(self):
        if self.texto_pantalla:
            self.operadores = ""
            self.texto_pantalla.set("0")

    def click(self, number):
        self.operadores += str(number)
        self.texto_pantalla.set(self.operadores)

    def Resultados(self):
        try:
            result = str(eval(self.operadores))
        except ZeroDivisionError:
            self.texto_pantalla.set("Error!")
        except SyntaxError:
            self.texto_pantalla.set("Agregue numero")
        else:
            return self.texto_pantalla.set(result)

    def ventana(self):
        tk.Entry(self, font=("Space mono", 25),
                 justify="right", bg="#65727c", fg="white", textvariable=self.texto_pantalla).grid(column=0, row=0, columnspan=4, sticky="we")

        # Operadores
        tk.Button(self, text="(", width=13, cursor="hand2",
                  relief="flat", fg="white", bg="#ff9800", bd=5, font=13,
                  activebackground="#ffc340", command=lambda:self.click("(")).grid(column=0, row=1)

        tk.Button(self, text=")", width=13, cursor="hand2",
                  relief="flat", fg="white", bg="#ff9800", bd=5, font=13,
                  activebackground="#ffc340", command=lambda:self.click(")")).grid(column=1, row=1)

        tk.Button(self, text="%", width=13, cursor="hand2",
                  relief="flat", fg="white", bg="#ff9800", bd=5, font=13,
                  activebackground="#ffc340", command=lambda:self.click("%")).grid(column=2, row=1)

        tk.Button(self, text="AC", width=13, cursor="hand2",
                  relief="flat", fg="white", bg="#ff9800", font=13, bd=5,
                  activebackground="#ffc340", command=self.clean_window).grid(column=3, row=1)

        tk.Button(self, text="/", width=13, cursor="hand2",
                  relief="flat", fg="white", bg="#ff9800", bd=5, font=13,
                  activebackground="#ffc340", command=lambda:self.click("/")).grid(column=3, row=2)

        tk.Button(self, text="x", width=13, cursor="hand2",
                  relief="flat", fg="white", bg="#ff9800", bd=5, font=13,
                  activebackground="#ffc340", command=lambda:self.click("*")).grid(column=3, row=3)

        tk.Button(self, text="-", width=13, cursor="hand2",
                  relief="flat", fg="white", bg="#ff9800", bd=5, font=13,
                  activebackground="#ffc340", command=lambda:self.click("-")).grid(column=3, row=4)

        tk.Button(self, text="+", width=13, cursor="hand2",
                  relief="flat", fg="white", bg="#ff9800", bd=5, font=13,
                  activebackground="#ffc340", command=lambda: self.click("+")).grid(column=3, row=5)

        # Numbers

        tk.Button(self, text="7", font=13, width=13, bd=5, relief="flat", cursor="hand2",
                  command=lambda:self.click(7)).grid(column=0, row=2)
        tk.Button(self, text="8", font=13, width=13, bd=5, relief="flat", cursor="hand2",
                  command=lambda:self.click(8)).grid(column=1, row=2)
        tk.Button(self, text="9", font=13, width=13, bd=5, relief="flat", cursor="hand2",
                  command=lambda:self.click(9)).grid(column=2, row=2)
        tk.Button(self, text="6", font=13, width=13, bd=5, relief="flat", cursor="hand2",
                  command=lambda:self.click(6)).grid(column=0, row=3)
        tk.Button(self, text="5", font=13, width=13, bd=5, relief="flat", cursor="hand2",
                  command=lambda:self.click(5)).grid(column=1, row=3)
        tk.Button(self, text="4", font=13, width=13, bd=5, relief="flat", cursor="hand2",
                  command=lambda:self.click(4)).grid(column=2, row=3)
        tk.Button(self, text="3", font=13, width=13, bd=5, relief="flat", cursor="hand2",
                  command=lambda:self.click(3)).grid(column=0, row=4)
        tk.Button(self, text="2", font=13, width=13, bd=5, relief="flat", cursor="hand2",
                  command=lambda:self.click(2)).grid(column=1, row=4)
        tk.Button(self, text="1", font=13, width=13, bd=5, relief="flat", cursor="hand2",
                  command=lambda:self.click(1)).grid(column=2, row=4)
        tk.Button(self, text="0", font=13, width=13, bd=5, relief="flat", cursor="hand2",
                  command=lambda:self.click(0)).grid(column=0, row=5)
        tk.Button(self, text=".", font=13, width=13, bd=5, relief="flat", cursor="hand2",
                  command=lambda:self.click(".")).grid(column=1, row=5)
        tk.Button(self, text="=", font=13, width=13, bd=5, relief="flat", cursor="hand2",
                  background="#1e91ed", fg="white", command=self.Resultados).grid(column=2, row=5)
