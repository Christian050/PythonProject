# WRITE A PSEUDOCODE TO DISPLAY EVEN NUMBERS FROM 1 TO 14.

from tkinter import *

master = Tk()

label = Label(text='Even Numbers From 0 To 14')
label.pack(anchor=CENTER)


def even():
    for x in range(0, 14):
        if x %2 == 0:
            even_numbers.insert(0, f' {x}')
    even_numbers.config(state='readonly')


bt = Button(master, text='Click Button', command=even)
bt.pack(pady=20)

even_numbers = Entry(master, insertwidth=15, justify=CENTER)
even_numbers.pack()
master.mainloop()
