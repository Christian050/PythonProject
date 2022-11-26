# WRITE A PSEUDOCODE TO PRINT THE FIRST FIVE NUMBERS.

from tkinter import *

root = Tk()


def print_first_five():
    first_five.config(state='normal')
    for i in range(0, 5):
        first_five.insert(0, f' {i}')
    first_five.config(state='readonly')


Bt = Button(root, text='Print first five numbers', command=print_first_five)
Bt.pack(pady=5)

first_five = Entry(root, width=15, justify=CENTER, state='disabled')
first_five.pack()

root.mainloop()
