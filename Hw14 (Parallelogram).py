# WRITE A PSEUDOCODE TO FIND THE AREA OF A PARALLELOGRAM.
# Area of a parallelogram a = b x h

from tkinter import *

# Set root/master
master = Tk()

# Set geometry
master.geometry('315x250')

# Set title
master.title('Area of A Parallelogram')

# Set resizable
master.resizable(0, 0)

# Set frame
fr = Frame(master, width=500, height=500)
fr.pack(fill='both', expand=1)

#  Title label
title_label = Label(fr, text='Area of a Parallelogram', anchor=CENTER)
title_label.pack(side=TOP, pady=10)

# Label Frame for base
base_label = LabelFrame(fr, text='Base', width=135, height=40, labelanchor=W)
base_label.pack(pady=20)

# Entry for base
base_entry = Entry(base_label, width=10, justify=CENTER)
base_entry.pack(padx=20, pady=7)

# Set base entry focus
base_entry.focus()

# Label frame for height
height_label = LabelFrame(fr, text='Height', width=135, height=40, labelanchor=W)
height_label.pack()

# Entry for height
height_entry = Entry(height_label, width=10, justify=CENTER)
height_entry.pack(padx=20, pady=7)

# Command calculate
def calculate():
    if base_entry.get().isnumeric() and height_entry.get().isnumeric():
        result_entry.config(state='normal')
        result_entry.delete(0, END)
        product = float(base_entry.get()) * float(height_entry.get())
        result_entry.insert(0, f"Area of Parallelogram with base {base_entry.get()} and height {height_entry.get()} is {product}")
        result_entry.config(state='readonly')
    else:
        result_entry.config(state='normal')
        result_entry.delete(0, END)
        result_entry.config(state='disabled')


# Calculate button
calculate_button = Button(fr, text='Find Area', bd=1, command=calculate)
calculate_button.pack(pady=20)

# Result entry box
result_entry = Entry(fr, width=50, justify=CENTER, state='disabled')
result_entry.pack()


mainloop()
