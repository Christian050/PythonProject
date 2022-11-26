#  Create a currency converter with GUI and draw a flowchart on its operation.
import time
from tkinter import Tk, StringVar, ttk
from tkinter import *
from tkinter import messagebox
from datetime import datetime

root = Tk()
root.title("CURRENCY CONVERTER")
root.configure(background='systembuttonface')
root.geometry('1000x300+0+0')

LeftMainFrame = LabelFrame(root, width=600, height=400, bd=8, relief="raise")
LeftMainFrame.pack(side=LEFT)
RightMainFrame = LabelFrame(root, width=200, height=400, bd=8, relief="raise")
RightMainFrame.pack(side=RIGHT)

DateofOrder = StringVar()
value0 = StringVar()
convert = DoubleVar()
currency = DoubleVar()

# conversion calculation
def conCurrency():
    if value0.get() == "USA":
        convert1 = float(convert.get() * 7.55)
        convert2 = "USA Dollar", str('%2f' % (convert1))
        currency.set(convert2)
    elif value0.get() == "Nigerian":
        convert1 = float(convert.get() * 415.58)
        convert2 = "Niara", str('%2f' % (convert1))
        currency.set(convert2)
    elif value0.get() == "Canada":
        convert1 = float(convert.get() * 1.27)
        convert2 = "Canadian Dollar", str('%2f' % (convert1))
        currency.set(convert2)
    elif value0.get() == "Euro":
        convert1 = float(convert.get() * 1.08)
        convert2 = "Euro", str('%2f' % (convert1))
        currency.set(convert2)


def qExist():
    qExist = messagebox.askyesno('Exit system', 'Do you want stop?')
    if qExist > 0:
        root.destroy()
        return

def Reset():
    value0.set("")
    convert.set("0.0")
    currency.set("0.0")

#Date
DateofOrder.set(time.strftime('%d/%m/%Y'))

#Entry
EntCurrency = Entry(LeftMainFrame, font=('Times new romans', 16, 'bold'), textvariable=convert, bd=2, width=20,
                    justify='center')
EntCurrency.grid(row=0, column=1)

#Label
lblDateofOrder = Label(RightMainFrame, font=('Time new romans', 16, 'bold'), textvariable=DateofOrder, bd=2, width=20,
                       justify='center')
lblDateofOrder.grid(row=0, column=0, sticky=W)

lblBritishPound = Label(LeftMainFrame, font=('Times new romans', 16, 'bold'), text='British Pound Equals',
                        bd=2, fg='black', width=18)
lblBritishPound.grid(row=0, column=2, padx=2, pady=2)


box = ttk.Combobox(LeftMainFrame, textvariable=value0, state='readonly', font=('Times new romans', 16, 'bold'), width=20)
box['values'] = ('Canada', 'Euro', 'Nigerian', 'USA')
box.current(0)
box.grid(row=4, column=2)

lblCurrency = Label(LeftMainFrame, font=('Times new romans', 16, 'bold'), textvariable=currency, bd=2, width=25,
                    bg='white', pady=2, padx=2, relief='sunken')
lblCurrency.grid(row=4, column=1)


# Buttons
butConvert = Button(RightMainFrame, text='Convert', padx=2, pady=2, bd=2, fg='black', font=('Time new romans', 16, 'bold'),
                   width=14, height=1, command=conCurrency).grid(row=1, column=0)

butReset = Button(RightMainFrame, text='Reset', padx=2, pady=2, bd=2, fg='black', font=('Time new romans', 16, 'bold'),
                   width=14, height=1, command=Reset).grid(row=2, column=0)

butExist = Button(RightMainFrame, text='Exit', padx=2, pady=2, bd=2, fg='black', font=('Time new romans', 16, 'bold'),
                    width=14, height=1, command=qExist).grid(row=3, column=0)



root.mainloop()
