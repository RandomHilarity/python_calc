from tkinter import *

equation = ""

def Calculator():
    #set up window and button frame
    window = Tk()

    Grid.rowconfigure(window, 0, weight=1)
    Grid.columnconfigure(window, 0, weight=1)

    frame = Frame(window)
    frame.grid(row=0, column=0, sticky=N+S+E+W)

    window.title("Calculator")
    window.resizable(0,0)

    #display variable and font    
    display_font = ('Arial', 12)
    display = StringVar()
        
    #output display
    screen = Entry(frame, textvariable=display, state="disabled", font=display_font, justify="right")
    screen.grid(row=0, column=0, columnspan=4, padx=(0), pady=4)
    screen.config(disabledbackground="white")    
    
    #button functions
    def click(char):
        global equation
        equation = equation + str(char)
        display.set(equation)
        screen.config(disabledforeground="black", disabledbackground="white")
    
    def clear():
        global equation
        equation = ""
        display.set(equation)
        screen.config(disabledforeground="black", disabledbackground="white")

    def delete():
        global equation
        if equation:
            equation = equation[:-1]
            display.set(equation)
            screen.config(disabledforeground="black", disabledbackground="white")
        else:
            pass

    def equal(display):
        global equation
        try:
            output = str(eval(equation))
            display.set(output)
            equation = output
        except:
            screen.config(disabledforeground="white", disabledbackground="red")
    
    #button creation
    b1 = Button(frame, text="1", height=2, bg="black", fg="white", command=lambda: click(1))
    b2 = Button(frame, text="2", height=2, bg="black", fg="white", command=lambda: click(2))
    b3 = Button(frame, text="3", height=2, bg="black", fg="white", command=lambda: click(3))
    b4 = Button(frame, text="4", height=2, bg="black", fg="white", command=lambda: click(4))
    b5 = Button(frame, text="5", height=2, bg="black", fg="white", command=lambda: click(5))
    b6 = Button(frame, text="6", height=2, bg="black", fg="white", command=lambda: click(6))
    b7 = Button(frame, text="7", height=2, bg="black", fg="white", command=lambda: click(7))
    b8 = Button(frame, text="8", height=2, bg="black", fg="white", command=lambda: click(8))
    b9 = Button(frame, text="9", height=2, bg="black", fg="white", command=lambda: click(9))
    b0 = Button(frame, text="0", height=2, bg="black", fg="white", command=lambda: click(0))
    b_dec = Button(frame, text=".", height=2, bg="black", fg="white", command=lambda: click("."))
    b_del = Button(frame, text="Del", height=2, bg="orange", fg="white", command=lambda: delete())
    b_clear = Button(frame, text="Clr", height=2, bg="orange", fg="white", command=lambda: clear())
    b_minus = Button(frame, text="-",  height=2, bg="red", fg="white", command=lambda: click("-"))
    b_plus = Button(frame, text="+", height=2, bg="red", fg="white", command=lambda: click("+"))
    b_divide = Button(frame, text="/", height=2, bg="red", fg="white", command=lambda: click("/"))
    b_multiply = Button(frame, text="*", height=2, bg="red", fg="white", command=lambda: click("*"))
    b_equals = Button(frame, text="=", height=2, bg="orange", fg="white", command=lambda: equal(display))

    #button placement
    b_clear.grid(row=2, column=0, columnspan=2, sticky=N+S+E+W)
    b_del.grid(row=2, column=2, columnspan=2, sticky=N+S+E+W)
    b7.grid(row=3, column=0, sticky=N+S+E+W)
    b8.grid(row=3, column=1, sticky=N+S+E+W)
    b9.grid(row=3, column=2, sticky=N+S+E+W)
    b_plus.grid(row=3, column=3, sticky=N+S+E+W)
    b4.grid(row=4, column=0, sticky=N+S+E+W)
    b5.grid(row=4, column=1, sticky=N+S+E+W)
    b6.grid(row=4, column=2, sticky=N+S+E+W)
    b_minus.grid(row=4, column=3, sticky=N+S+E+W)
    b1.grid(row=5, column=0, sticky=N+S+E+W)
    b2.grid(row=5, column=1, sticky=N+S+E+W)
    b3.grid(row=5, column=2, sticky=N+S+E+W)
    b_divide.grid(row=5, column=3, sticky=N+S+E+W)
    b0.grid(row=6, column=0, columnspan=2, sticky=N+S+E+W)
    b_dec.grid(row=6, column=2, sticky=N+S+E+W)
    b_multiply.grid(row=6, column=3, sticky=N+S+E+W)
    b_equals.grid(row=7, columnspan=4, sticky=N+S+E+W)
    
    window.mainloop()

if __name__ == "__main__":
    Calculator()