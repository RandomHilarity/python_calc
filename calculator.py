from tkinter import *

def Calculator():
    #set up window and button frame
    window = Tk()

    Grid.rowconfigure(window, 0, weight=1)
    Grid.columnconfigure(window, 0, weight=1)

    frame = Frame(window)
    frame.grid(row=0, column=0, sticky=N+S+E+W)

    window.title("Calculator")
    window.resizable(0,0)

    #equation variable and font    
    display_font = ('Arial', 12)
    display = StringVar()
        
    #output display
    screen = Entry(frame, textvariable=display, state="disabled", font=display_font)
    screen.grid(row=0, column=0, columnspan=4, padx=(0), pady=4)
    screen.config(disabledbackground="white")    
    #button creation
    b1 = Button(frame, text="1", height=2, bg="black", fg="white")
    b2 = Button(frame, text="2", height=2, bg="black", fg="white")
    b3 = Button(frame, text="3", height=2, bg="black", fg="white")
    b4 = Button(frame, text="4", height=2, bg="black", fg="white")
    b5 = Button(frame, text="5", height=2, bg="black", fg="white")
    b6 = Button(frame, text="6", height=2, bg="black", fg="white")
    b7 = Button(frame, text="7", height=2, bg="black", fg="white")
    b8 = Button(frame, text="8", height=2, bg="black", fg="white")
    b9 = Button(frame, text="9", height=2, bg="black", fg="white")
    b0 = Button(frame, text="0", height=2, bg="black", fg="white")
    b_dec = Button(frame, text=".", height=2, bg="black", fg="white")
    b_del = Button(frame, text="Del", height=2, bg="orange", fg="white")
    b_clear = Button(frame, text="Clr", height=2, bg="orange", fg="white")
    b_minus = Button(frame, text="-",  height=2, bg="red", fg="white")
    b_plus = Button(frame, text="+", height=2, bg="red", fg="white")
    b_divide = Button(frame, text="/", height=2, bg="red", fg="white")
    b_multiply = Button(frame, text="*", height=2, bg="red", fg="white")
    b_equals = Button(frame, text="=", height=2, bg="orange", fg="white")

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