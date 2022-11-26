from tkinter import *
from tkinter import messagebox
from tkinter import Tk
from tkinter import ttk
# windows = Tk()
# # add widgets here
# windows.title("Christian's Session")
# windows.geometry("300x200+10+20")
# # geometry creates the size/dimension of the window
# windows.mainloop()

# from tkinter import *
# window = Tk()
# window.title("Christian's Session")
# btn = Button(window, text="This is Button widget", fg='blue')
# btn.place(x=80, y=100)
# lbl = Label(window, text="This is label widget", fg='red', font=("Helvetica", 16))
# lbl.place(x=60, y=50)
# txtfld = Entry(window, text="This is Entry Widget", bd=5)
# txtfld.place(x=80, y=150)
# # window.title("Christian's Session")
# window.geometry("300x200+10+10")
# window.mainloop()

# from tkinter.ttk import Combobox
# from tkinter import *
# window = Tk()
# var = StringVar()
# var.set("one")
# data = ("9-11", "11-1", "3-5", "5-7")
# cb = Combobox(window, values=data)
# cb.place(x=60, y=150)
#
# lb = Listbox(window, height=5, selectmode='multiple')
# for num in data:
#     lb.insert(END, num)
# lb.place(x=250, y=150)
#
# v0 = IntVar()
# v0.set(1)
# r1 = Radiobutton(window, text="male", variable=v0, value=1)
# r2 = Radiobutton(window, text="Female", variable=v0, value=2)
# r1.place(x=100, y=50)
# r2.place(x=180, y=50)
#
# v1 = IntVar()
# v2 = IntVar()
# C1 = Checkbutton(window, text="Ghana", variable=v1)
# C2 = Checkbutton(window, text="Nigeria", variable=v2)
# C1.place(x=100, y=100)
# C2.place(x=180, y=100)
# window.title("Christian's Session")
# window.geometry("400x300+10+10")
# window.mainloop()

# Event handling
# A notification received by the application object from various GUI widgets as a result of user interaction.
# Events are expressed as strings in <modifier-type-qualifier> format.

"""Event            Modifier         Type           Qualifier           Action
<Button 1>                          Button             1        The left mouse button click.
<Button 2>                          Button             2        Middle mouse button click.
<Destroy>                           Destroy                     The window is destroyed.
<Double button 1>                   Double             1        Double click the first mouse button 1.
<Focus In>                          Focus In                    Widget gains focus.
<Enter>                             Enter                       Cursor enters window.
<Key Release>                       Key Release                 Any key has been released.
<Key Press-a>                       Key Press          a        Any key has been pressed.
<Expose>                            Expose                      Window fully or partially exposed.
<Leave>                             Leave                       Cursor leaves window.
<Print>                                               Print     Print key has been pressed.
<Focus out>                         Focus Out                   Widget loses focus."""

# Binding an event to an action
# from tkinter import *
# def hello (event):
#     print("Single Click, Button-1")
# def quit(event):
#
#     print("Double Click, so let's stop")
#     import sys
#     sys.exit()
#
# widget = Button(None, text='Mouse Clicks')
# widget.pack()
# widget.bind('<Button-1>', hello)
# widget.bind('<Double-1>', quit)
# widget.mainloop()

# Motion Event Handling
# from tkinter import *
#
# def motion(event):
#     print('Mouse position: (%s %s)' % (event.x, event.y))
#     return
#
# master = Tk()
# whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
# msg = Message(master, text=whatever_you_do)
# msg.config(bg="light green", font=('Times', 24, 'italic'), fg='red')
# msg.bind('<Motion>', motion)
# msg.pack()  # grid(row= , column=)
# mainloop()

# import tkinter as tk
# master = tk.Tk()
# quote = "Our lives begin to end the day we become silent of the things that matter.\n(Martin Luther King Jnr)"
# msg = tk.Message(master, text=quote)
# msg.config(bg="yellow", font=('calibri body', 24, 'bold', 'italic'))
# msg.pack()
# tk.mainloop()


# Entry Widgets
# import tkinter as tk
#
# master = tk.Tk()
# tk.Label(master, text="First Name").grid(row=0)
# tk.Label(master, text="Last Name").grid(row=1)
#
# e1 = tk.Entry(master)# width=(n)
# e2 = tk.Entry(master)
#
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1) # columnspan=(n) padx=(n), pady=(n)
#
# master.mainloop()


#Get() method(receives input and prints out an action)

#Entry Widget 2 (Reading the content of an Entry using the GET method)
# import tkinter as tk
# def show_entry_fields():
#     print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
#
# master = tk.Tk()
# tk.Label(master, text="First Name").grid(row=0)
# tk.Label(master, text="Last Name").grid(row=1)
#
# e1 = tk.Entry(master)
# e2 = tk.Entry(master)
#
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
#
# tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
# tk.Button(master, text='Show',command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)
# tk.mainloop()


#Timer with a stop button
# import tkinter as tk
#
# counter = 0
# def counter_label(label):
#     counter = 0
#     def count():
#         global counter
#         counter += 1
#         label.config(text=str(counter))
#         label.after(1000, count)
#     count()
#
#
# root = tk.Tk()
# root.title("Counting Seconds")
# label = tk.Label(root, fg="dark green")
# label.pack()
# counter_label(label)
# button = tk.Button(root, text='Stop', width=25, command=root.destroy)
# button.pack()
# root.mainloop()

master = Tk()
note = ttk.Notebook(master)
def inf():
    messagebox.showinfo("INFO", 'This is the info messagebox')

info_frame = Frame(note, width=480, height=480)
info_frame.pack(fill='both', expand=1)
note.add(info_frame, text='Info')


Info = Button(info_frame, text="Info", font=('Helvetica', 24), width=480, command=inf)
Info.grid(row=0, column=0)
master.mainloop()



