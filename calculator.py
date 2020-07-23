from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("300x400")
        master.resizable(0,0)

        #output display
        self.screen = Text(master, state="disabled", width=35, height=3)
        self.screen.grid(row=0, column=0, columnspan=4, padx=6, pady=4)
        self.screen.configure(state="normal")
        
        self.display = ""

if __name__ == "__main__":
    window = Tk()
    gui = Calculator(window)
    window.mainloop()