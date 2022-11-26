# WRITE A PSEUDOCODE TO FIND THE GREATEST OF TWO NUMBERS.

from tkinter import *

# Set root/master
root = Tk()

# Set geometry
root.geometry('380x250')

# Set title
root.title('Greatest of Two Numbers')

# Set resizable
root.resizable(0, 0)

# Label frame for input
input_label = LabelFrame(root, text='Input', labelanchor=N, bd=0)
input_label.pack(pady=20, padx=10)

# Label and entry for input
first_label = LabelFrame(input_label, text='First Number =>', labelanchor=W, bd=0)
first_label.pack(side=LEFT, anchor=NW)

first_entry = Entry(first_label, width=10, justify=CENTER)
first_entry.pack(padx=5, pady=10)

second_label = LabelFrame(input_label, text='Second Number =>', labelanchor=W, bd=0)
second_label.pack(side=RIGHT, anchor=NE)

second_entry = Entry(second_label, width=10, justify=CENTER)
second_entry.pack(padx=5, pady=10)

# Spacer
spacer = Label(input_label, text="")
spacer.pack(anchor=CENTER, padx=10)

# Set focus
first_entry.focus()


# Create find_greatest command
def find_greatest():
    if first_entry.get().isnumeric() and second_entry.get().isnumeric():
        result_entry.config(state="normal")
        result_entry.delete(0, END)
        if first_entry.get() > second_entry.get():
            result_entry.insert(0, f'{first_entry.get()} is the greatest of the two.')
        if second_entry.get() > first_entry.get():
            result_entry.insert(0, f'{second_entry.get()} is the greatest of the two.')
        if first_entry.get() == second_entry.get():
            result_entry.insert(0, f'Both numbers are equal.')
        result_entry.config(state='readonly')
    else:
        result_entry.config(state="normal")
        result_entry.delete(0, END)
        result_entry.config(state='readonly')


# Create find button     add button frame, clear button and spacer
find_button = Button(root, text='Find', bd=1, command=find_greatest)
find_button.pack(pady=20)

# Create result label frame and entry
result_label = LabelFrame(root, text='Greatest Number', labelanchor=N, bd=0)
result_label.pack()

result_entry = Entry(result_label, width=35, justify=CENTER, state='disabled', bd=0)
result_entry.pack(padx=10, pady=10)

root.mainloop()
