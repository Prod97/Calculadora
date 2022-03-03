import tkinter as tk
from frame import Frame


class Program:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora ")
        self.root.resizable(False, False)
        self.frm = Frame(self.root)

        self.root.mainloop()
if __name__ == '__main__':
    application = Program()