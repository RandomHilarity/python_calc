from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

window = Tk()
gui = Calculator(window)
window.mainloop()