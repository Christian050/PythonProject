# # from tkinter import ttk
# # from tkinter import Tk
# # from tkinter import messagebox
# #
# # master = Tk()
# # master.geometry("150x150")
# #
# # # Tabs
# # note = ttk.Notebook(master)
# # note.pack(pady=5)
# #
# # # Frame
# # info_frame = Frame(note, width=140, height=140)
# # info_frame.pack(fill='both', expand=1)
# #
# # # Create Tab
# # note.add(info_frame, text="Note Tab")
# #
# # master.mainloop()
#
#
# # master = Tk()
# # master.title("Currency Convertor")
# # master.geometry("500x500")
# #
# # # Tabs
# # nb = ttk.Notebook(master)
# # nb.pack(pady=5)
# #
# # #Two frames
# # currency_frame = Frame(nb, width=480, height=480)
# # conversion_frame = Frame(nb, width=480, height=480)
# #
# # currency_frame.pack(fill="both", expand=1)
# # conversion_frame.pack(fill="both", expand=1)
# #
# # # Add Tabs
# # nb.add(currency_frame, text="Currency")
# # nb.add(conversion_frame, text="Convert")
# #
# # # Disable 2nd Tab
# # nb.tab(1, state='disabled')
# #
# # master.mainloop()
#
# # from tkinter import *
# #
# #
# # root = Tk()
# # root.title("AREA OF A RECTANGLE")
# # root.config(background='sky blue')
# # root.geometry('500x500')
# #
# # default = ("times new roman", 20)
# #
# # # Command clickarea
# # def calcarea(w, h):
# #     return w * h
# #
# # def clickarea():
# #     area.set(calcarea(height.get(), width.get()))
# #
# # # Set Variable
# # width = IntVar()
# # height = IntVar()
# # area = IntVar()
# #
# # # Width
# # Label(root, bg='sky blue', width=10, padx=5, pady=5, bd=5, text="Width").grid(row=0, column=0)
# # Entry(root, textvariable=width).grid(row=0, column=1)
# #
# # # Height
# # Label(root, bg='sky blue', width=10, padx=5, pady=5, bd=5, text="Height").grid(row=1, column=0)
# # Entry(root, textvariable=height).grid(row=1, column=1)
# #
# # # Area
# # Label(root, bg='sky blue', width=10, padx=5, pady=5, bd=5, text="Area").grid(row=2, column=0)
# # Entry(root, textvariable=area).grid(row=2, column=1)
# #
# # # Calculate Area Button
# # button = Button(root, text="Calculate Area", command=clickarea)
# # button.grid(row=3, column=0, columnspan=2)
# #
# #
# #
# # mainloop()
# #
#
#
# from tkinter import *
# from tkinter import messagebox
#
# root = Tk()
# root.title('PERIMETER OF A RECTANGLE')
# root.configure(background='orange')
# geometry = ('500x500')
#
# default = ('Brightness', 14, 'bold')
#
#
# # command area
# def calPerimeter():
#     res = 2 * (Length.get() + Width.get())
#     Perimeter.set(0, f'{res}')
#
# def Exit():
#     Exist = messagebox.askyesno('Exit System', 'Do you to end programme?')
#     if Exist > 0:
#         root.destroy()
#         return
#
#
# # Set variable
# Length = IntVar()
# Width = IntVar()
# Perimeter = IntVar()
#
# # Length
# Label(root, bg='orange', font=default, width=10, height=1, padx=2, pady=2, text='Length').grid(row=1, column=0)
# Entry(root, textvariable=Length).grid(row=1, column=1)
#
# # Width
# Label(root, bg='orange', font=default, width=10, height=1, padx=2, pady=2, text='Width').grid(row=2, column=0)
# Entry(root, textvariable=Width).grid(row=2, column=1)
#
# # Result Entry Box
# Label(root, bg='orange', font=default, width=10, height=1, padx=2, pady=2, text='Perimeter').grid(row=3, column=0)
# Entry(root, textvariable=Perimeter, width=20).grid(row=3, column=1)
#
# # Calculate Button
# button = Button(root, font=default, text='Calculate Perimeter', command=calPerimeter)
# button.grid(row=4, column=0, columnspan=2)
#
# # Exit Button
#
# Exitbutton = Button(root, text='Exit', width=8, font=default, command=Exit).grid(row=4, column=2)
#
# mainloop()
#


# from tkinter import *
# from tkinter import messagebox
#
# root = Tk()
# root.title('PERIMETER OF A RECTANGLE')
# root.configure(background='orange')
# geometry = ('500x500')
#
# default = ('Brightness', 14, 'Bold')
#
#
# # command area
# def calPerimeter(2 * L + B):
#     return 2 * (L + B)
#
#
# def clickPerimeter():
#     Perimeter.set(calPerimeter(Length.get(), Width.get()))
#
#
# def Exit():
#     Exist = messagebox.askyesno('Exit System', 'Do you to end programme?')
#     if Exist > 0:
#         root.destroy()
#         return
#
#
# # Set variable
# Length = IntVar()
# Width = IntVar()
# Perimeter = IntVar()
#
# # Length
# Label(root, bg='orange', font=default, width=10, height=1, padx=2, pady=2, text='Length').grid(row=1, column=0)
# Entry(root, textvariable=Length).grid(row=1, column=1)
#
# # Width
# Label(root, bg='orange', font=default, width=10, height=1, padx=2, pady=2, text='Width').grid(row=2, column=0)
# Entry(root, textvariable=Width).grid(row=2, column=1)
#
# # Calculate Button
# button = Button(root, font=default, text='Calculate Perimeter', command=clickPerimeter)
# button.grid(row=3, column=0, columnspan=2)
#
# # Exit Button
#
# Exitbutton = Button(root, width=8, font=default, command=Exit).grid(row=3, column=2)
#
# mainloop()

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('PERIMETER OF A RECTANGLE')
root.configure(background='orange')
geometry = ('500x500')

default = ('Brightness', 14, 'bold')


# command area
def calPerimeter(Length, Width):
    return 2 * (Length + Width)


def clickPerimeter():
    Perimeter.set(calPerimeter(Length.get(), Width.get()))


def Exit():
    Exist = messagebox.askyesno('Exit System', 'Do you to end programme?')
    if Exist > 0:
        root.destroy()
        return


# Set variable
Length = IntVar()
Width = IntVar()
Perimeter = IntVar()

# Length
Label(root, bg='orange', font=default, width=10, height=1, padx=2, pady=2, text='Length').grid(row=1, column=0)
Entry(root, textvariable=Length).grid(row=1, column=1)

# Width
Label(root, bg='orange', font=default, width=10, height=1, padx=2, pady=2, text='Width').grid(row=2, column=0)
Entry(root, textvariable=Width).grid(row=2, column=1)

# Perimeter
Label(root, bg='orange', font=default, width=10, height=1, padx=2, pady=2, text='Perimeter').grid(row=3, column=0)
Entry(root, textvariable=Perimeter).grid(row=3, column=1)

# Calculate Button
button = Button(root, font=default, text='Calculate Perimeter', command=clickPerimeter)
button.grid(row=4, column=0, columnspan=2)

# Exit Button

Exitbutton = Button(root, text='Exit', width=8, font=default, command=Exit).grid(row=4, column=2)

mainloop()

