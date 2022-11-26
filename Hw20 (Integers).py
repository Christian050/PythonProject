# WRITE A PSEUDOCODE TO DISPLAY INTEGERS UP TO N.

from tkinter import *

root = Tk()

label = Label(root, text='Integers 1 to 100')
label.pack()


def cmd_integers():
    integers.delete(0, END)
    for x in range(0, 100):
        integers.insert(0, f' {x}')


bt = Button(root, text='Find', command=cmd_integers)
bt.pack(pady=20)

integers = Entry(root, width=400)
integers.pack()

root.mainloop()
