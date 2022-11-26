# WRITE A PSEUDOCODE TO DISPLAY MONTH NAME ACCORDING TO THEIR POSITION.

from tkinter.ttk import Combobox
from tkinter import *

root = Tk()
root.geometry('180x180')
root.title('')
root.config(bg='pink')
root.resizable(False, False)


my_label = Label(root, text='Month Of The Year', bg='pink')
my_label.pack(side=TOP, anchor=CENTER)

sb = Scrollbar()
cb = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
options = Combobox(root, values=cb, width=10, height=10, justify=CENTER, state='readonly', xscrollcommand=sb.set)
options.pack(pady=30)


def find_month():
    month_name.config(state='normal')
    month_name.delete(0, END)
    if options.get() == '1':
        month_name.insert(0, 'January(Jan)')
    if options.get() == '2':
        month_name.insert(0, 'February(Feb)')
    if options.get() == '3':
        month_name.insert(0, 'March(Mar)')
    if options.get() == '4':
        month_name.insert(0, 'April(Apr)')
    if options.get() == '5':
        month_name.insert(0, 'May')
    if options.get() == '6':
        month_name.insert(0, 'June(Jun)')
    if options.get() == '7':
        month_name.insert(0, 'July(Jul)')
    if options.get() == '8':
        month_name.insert(0, 'August(Aug)')
    if options.get() == '9':
        month_name.insert(0, 'September(Sep)')
    if options.get() == '10':
        month_name.insert(0, 'October(Oct)')
    if options.get() == '11':
        month_name.insert(0, 'November(Nov)')
    if options.get() == '12':
        month_name.insert(0, 'December(Dec)')
    month_name.config(state='readonly')


button = Button(root, text='Find Month', command=find_month, bd=0, bg='pink', activebackground='pink')
button.pack()

month_name = Entry(root, width=15, state='readonly', justify=CENTER, bd=0, readonlybackground='pink')
month_name.pack(side=BOTTOM, pady=10)

root.mainloop()
