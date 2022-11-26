# WRITE A PSEUDOCODE TO FIND THE CIRCUMFERENCE OF A CIRCLE.

from tkinter import *

# Set root, geometry, title and resizable
root = Tk()
root.geometry('320x180')
root.title('Circumference Of A Circle')
root.resizable(0, 0)

# Set frame and pack
window_frame = Frame(root, width=500, height=500)
window_frame.pack()


# Create clear command
def clear():
    circumference.config(state='normal')
    radius_entry.delete(0, END)
    circumference.delete(0, END)
    circumference.config(state='readonly')


# Create clear frame
clear_frame = LabelFrame(window_frame, bd=1)
clear_frame.pack(anchor=N, side=RIGHT, pady=7, padx=10)

# Create clear button
clear_button = Button(clear_frame, text='Clear', command=clear)
clear_button.pack()

#  Set labelframe and entry box for radius
radius_label = LabelFrame(window_frame, width=100, height=70, bd=0)
radius_label.config(text='Enter radius here ⇑', labelanchor=S)
radius_label.pack()
radius_entry = Entry(radius_label, width=10, justify=CENTER)
radius_entry.focus()
radius_entry.pack(pady=10)


# Create command calculate
def calculate():
    # Enable circumference entry box and insert formular
    if radius_entry.get():
        circumference.config(state='normal')
        result = 2 * (3.14 * float(radius_entry.get()))
        # Clear entry box before input
        circumference.delete(0, END)
        # Insert result
        circumference.insert(0, f'{result}')
        circumference.config(state='readonly')
    else:
        # Disable circumference if no input
        circumference.config(state='readonly')


# Create calculate button
calculate_button = Button(window_frame, text='Calculate', command=calculate)
calculate_button.pack(pady=20)

# Set circumference frame
circumference_frame = LabelFrame(window_frame, text='Circumference Of A Circle=>', labelanchor=W)
circumference_frame.pack(pady=5)

# Set result entry box
circumference = Entry(window_frame, width=10, justify=CENTER,  state='disabled')
circumference.pack()


# Set Mainloop
root.mainloop()

