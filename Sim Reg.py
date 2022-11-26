# Create a program with an (to apply entry widgets,title/label widget) to facilitate sim registration and show.

import tkinter as tk

# fields = 'Last Name', 'First Name', 'Sim Card', 'I.D'
# class lab:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.geometry("300x500+10+10")
#         self.window.title("Sim Registration")
#
#     def entries(self):
#         for entry in entries:
#             field = entry[0]
#             text = entry[1].get()
#             print('%s: "%s" ' % (field, text))
#     def inp(self):
#         self.
#
import tkinter as tk
font_ = ('Arial', 16, 'bold')

def show_entry_fields():
    print("First Name: %s\nLast Name: %s\nSIM:  %s\nI.D: %s" % (e1.get(), e2.get(), e3.get(), e4.get()))

master = tk.Tk()
tk.Label(master, text="First Name", font=font_, width=10, bg="yellow").grid(row=0)
tk.Label(master, text="Last Name", font=font_, width=10, bg="yellow").grid(row=1)
tk.Label(master, text="SIM", font=font_, width=10, bg="yellow").grid(row=2)
tk.Label(master, text="I.D", font=font_, bg="yellow", width=10).grid(row=3)
master.title("SIM Registration Popup")
master.config(bg="yellow")
master.geometry("375x300")
# master.resizable(0, 0)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)

e1.grid(row=0, column=1, pady=20)
e2.grid(row=1, column=1, pady=20)
e3.grid(row=2, column=1, pady=20)
e4.grid(row=3, column=1, pady=20)
tk.Button(master, text='Quit', command=master.quit, width=20).grid(row=4, column=0, sticky=tk.W, pady=30, padx=10)
tk.Button(master, text='Show', command=show_entry_fields, width=20).grid(row=4, column=1, sticky=tk.E, pady=30, padx=10)
tk.mainloop()
