from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Please write a python code to accept 3 numbers and arrange them in ascending order
# user_input_1 = float(input('Enter first number\n'))
# user_input_2 = float(input('Enter second number\n'))
# user_input_3 = float(input('Enter third number\n'))
#
# List = [user_input_1, user_input_2, user_input_3]
# List.sort()
# print(List)

# a = int(input("a:\t"))
# b = int(input("b:\t"))
# c = int(input("c:\t"))
#
# if (a <= b) and (b <= c):
#     print(a, b, c)
# elif(a < c) and (c <= b):
#     print(a, c, b)
# if (b < a) and (a <= c):
#     print(b, a, c)
# elif (b < c) and (c <= a):
#     print(b, c, a)
# if (c < a) and (a <= b):
#     print(c, a, b)
# elif (c < b) and (b <= a):
#     print(c, b, a)


# master = Tk()
# master.geometry("150x150")
#
# # Tabs
# note = ttk.Notebook(master)
# note.pack(pady=5)
#
# # Frame
# info_frame = Frame(note, width=140, height=140)
# info_frame.pack(fill='both', expand=1)
#
# # Create Tab
# note.add(info_frame, text="Note Tab")
#
# master.mainloop()
#
#
# master = Tk()
# master.title("Currency Convertor")
# master.geometry("500x500")
#
# # Tabs
# nb = ttk.Notebook(master)
# nb.pack(pady=5)
#
# #Two frames
# currency_frame = Frame(nb, width=480, height=480)
# conversion_frame = Frame(nb, width=480, height=480)
#
# currency_frame.pack(fill="both", expand=1)
# conversion_frame.pack(fill="both", expand=1)
#
# # Add Tabs
# nb.add(currency_frame, text="Currency")
# nb.add(conversion_frame, text="Convert")
#
# # Disable 2nd Tab
# nb.tab(1, state='disabled')
#
# master.mainloop()

# SET master
master = Tk()
master.geometry('450x450')
note = ttk.Notebook(master)
note.pack()

# Input and Return Frames
input_frame = Frame(note, width=400, height=400)
return_frame = Frame(note, width=400, height=400)
input_frame.pack(fill='both', expand=1)
return_frame.pack(fill='both', expand=1)

# Equals Label frame
Equals_label_frame = LabelFrame(return_frame, text='Sort')
Equals_label_frame.pack(padx=20, pady=20)

# Entries
Entry_a_labelframe = LabelFrame(input_frame, text='Entry A')
Entry_a_labelframe.pack(pady=20)
Entry_b_labelframe = LabelFrame(input_frame, text='Entry B')
Entry_b_labelframe.pack(pady=20)
Entry_c_labelframe = LabelFrame(input_frame, text='Entry C')
Entry_c_labelframe.pack(pady=20)

# Tabs
note.add(input_frame, text='Input')
note.add(return_frame, text='Return')
note.tab(1, state='disabled')

# Entries Pack
Entry_a = Entry(Entry_a_labelframe, width=50)
Entry_a.pack(pady=20, padx=20)
Entry_b = Entry(Entry_b_labelframe, width=50)
Entry_b.pack(pady=20, padx=20)
Entry_c = Entry(Entry_c_labelframe, width=50)
Entry_c.pack(pady=20, padx=20)

# Equals Data And Entry data
Equals = Entry(Equals_label_frame, width=50, bg='systembuttonface', bd=0)
Entry_data = [Entry_a.get(), Entry_b.get(), Entry_c.get()]

Equals.pack(pady=20, padx=20)

# Button Frame
button_frame = Frame(input_frame)
button_frame.pack(padx=2)
sort_list = list()

# Done Command
def done():
    Entry_data = str(Entry_a.get()) + str(Entry_b.get()) + str(Entry_c.get())
    Entry_a.config(state='disabled')
    Entry_b.config(state='disabled')
    Entry_c.config(state='disabled')
    note.tab(1, state='normal')
    if not Entry_a.get().isnumeric() or not Entry_b.get().isnumeric() or not Entry_c.get().isnumeric():
        messagebox.showerror('ERROR!', 'Entries include letters. Enter only numbers/digits.')
        Entry_a.config(state='normal')
        Entry_b.config(state='normal')
        Entry_c.config(state='normal')
        note.tab(1, state='disabled')
        Entry_a.delete(0, END)
        Entry_b.delete(0, END)
        Entry_c.delete(0, END)
    else:
        e = sort_list.append(Entry_data)
        
        # for i in e:
        #     print(i)


# Next Button
nxt = Button(button_frame, text='Done', command=done)
nxt.pack(padx=100, pady=20)




master.mainloop()
