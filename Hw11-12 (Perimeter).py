# WRITE A PSEUDOCODE TO FIND THE PERIMETER OF RECTANGLE.
# WRITE A PSEUDOCODE TO FIND THE PERIMETER OF A SQUARE.

from tkinter import colorchooser
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# Set Root
root = Tk()

# Set Geometry
root.geometry("350x430")

# Set Title
root.title('Perimeter')

# Set Resizable
root.resizable(0, 0)

# Set Notebook, pack notebook to show
nb = ttk.Notebook(root)
nb.pack()

# Input and Return Frames in Notebook
rectangle_frame = Frame(nb, width=400, height=415, bd=0)
square_frame = Frame(nb, width=400, height=400)
rectangle_frame.pack(fill='both', expand=1)
square_frame.pack(fill='both', expand=1)

# Set notebook Tabs for rectangle and square
nb.add(rectangle_frame, text='Perimeter of a Rectangle')
nb.add(square_frame, text='Perimeter of a Square')

# Disable second tab
nb.tab(1, state='disabled')

# Set Rectangle Image for "Perimeter of a Rectangle"
rectangle_canvas = Canvas(rectangle_frame, width=1000, height=200)
rectangle_canvas.pack()
rectangle_image = ImageTk.PhotoImage(Image.open('rectangleperimeter.png'))
rectangle_canvas.create_image(50, 10, anchor=NW, image=rectangle_image)


# Change color
def rectangle_color():
    rectangle_bg_color = colorchooser.askcolor()
    color_name = rectangle_bg_color[1]
    rectangle_frame.config(bg=color_name)
    rectangle_button_frame.config(bg=color_name)
    rectangle_canvas.config(bg=color_name)
    rectangle_length_label_frame.config(bg=color_name)
    rectangle_width_label_frame.config(bg=color_name)


# Set labelframe and entry to get Length and Width and result for Rectangle
rectangle_length_label_frame = LabelFrame(rectangle_frame, text='Length', width=30, height=30, bd=0)
rectangle_length_label_frame.pack(pady=5)

rectangle_length_entry = Entry(rectangle_length_label_frame, width=30, bg='systembuttonface')
rectangle_length_entry.pack(pady=5)

rectangle_width_label_frame = LabelFrame(rectangle_frame, text='Width', width=30, height=30, bd=0)
rectangle_width_label_frame.pack(pady=5)

rectangle_width_entry = Entry(rectangle_width_label_frame, width=30, bg='systembuttonface')
rectangle_width_entry.pack(pady=5)


# Set command calculate for rectangle
def calculate():
    # Set entry insert
    rectangle_result_entry.config(state='normal')
    rectangle_result_entry.delete(0, END)
    res = float(rectangle_length_entry.get())*2 + float(rectangle_width_entry.get())*2
    rectangle_result_entry.insert(0, f'{res}')
    rectangle_result_entry.config(state='readonly')


# Set command clear for rectangle
def clear():
    if not rectangle_length_entry.get() and not rectangle_width_entry.get() and not rectangle_result_entry.get():
        messagebox.showwarning('Error', "There's no input")
    else:
        rectangle_length_entry.delete(0, END)
        rectangle_width_entry.delete(0, END)
        rectangle_result_entry.config(state='normal')
        rectangle_result_entry.delete(0, END)
        rectangle_result_entry.config(state='readonly')
        rectangle_length_entry.focus()


# Set command next for next tab
def next():
    nb.tab(1, state='normal')
    nb.tab(0, state='disabled')


# Set button frame for rectangle
rectangle_button_frame = Frame(rectangle_frame, bd=0)
rectangle_button_frame.pack()

# Set calculate button for rectangle
rectangle_calculate_button = Button(rectangle_button_frame, text='Calculate', bd=1, command=calculate)
rectangle_calculate_button.grid(padx=30, pady=2, row=0, column=0, sticky=W)

# Set clear button for rectangle
rectangle_clear_button = Button(rectangle_button_frame, text='Clear', bd=1, command=clear)
rectangle_clear_button.grid(padx=30, pady=2, row=0, column=1, sticky=E)

# Set result entry box for rectangle
rectangle_result_entry = Entry(rectangle_frame, width=30, bg='systembuttonface', state='readonly')
rectangle_result_entry.pack(pady=10)

# Set next button for rectangle
next_button = Button(rectangle_frame, text='Next>>>', bd=1, command=next)
next_button.pack(side=RIGHT)

rectangle_color_picker = Button(rectangle_frame, text='Change Color', bd=1, command=rectangle_color)
rectangle_color_picker.pack(side=LEFT)

# SQUARE

# Set Square Image for "Perimeter of a Square"
square_canvas = Canvas(square_frame, width=600, height=200)
square_canvas.pack(padx=0)
square_image = ImageTk.PhotoImage(Image.open('square.png'))
square_canvas.create_image(15, 10, anchor=NW, image=square_image)

# Set labelframe and entry to get Length and Width and result for Square
square_length_label_frame = LabelFrame(square_frame, text='    Length', width=30, height=30, bd=0)
square_length_label_frame.pack(pady=5)

square_length_entry = Entry(square_length_label_frame, width=10, justify=CENTER)
square_length_entry.pack(pady=5)

square_width_label_frame = LabelFrame(square_frame, text='    Width', width=30, height=30, bd=0)
square_width_label_frame.pack(pady=5)

square_width_entry = Entry(square_width_label_frame, width=10, justify=CENTER)
square_width_entry.pack(pady=5)


# Set command square_cmd_calculate for square
def square_cmd_calculate():
    if not square_length_entry.get() or not square_width_entry.get():
        messagebox.showwarning('Error', "There's no input")
        square_entry_box.config(state='readonly')
    elif square_length_entry.get() == int or float and square_width_entry.get() == int or float:
        # Set entry insert
        square_entry_box.config(state='normal')
        square_entry_box.delete(0, END)
        square_result = float(square_length_entry.get())*2 + float(square_width_entry.get())*2
        square_entry_box.insert(0, f'{square_result}')
        square_entry_box.config(state='readonly')
    if square_length_entry.get().isalpha() or square_width_entry.get().isalpha():
        square_entry_box.config(state='normal')
        square_entry_box.delete(0, END)
        square_entry_box.config(state='disabled')
        messagebox.showwarning('Error', "Needs numbers to calculate")
    # elif square_length_entry.get().isalnum() or square_width_entry.get().isalnum():
    #     square_entry_box.config(state='normal')
    #     square_entry_box.delete(0, END)
    #     square_entry_box.config(state='disabled')
    #     messagebox.showwarning('Error', "Includes letters")


# Set command square_cmd_clear for square
def square_cmd_clear():
    if not square_length_entry.get() and not square_width_entry.get() and not square_entry_box.get():
        messagebox.showwarning('Error', "There's no input")
    else:
        square_length_entry.delete(0, END)
        square_width_entry.delete(0, END)
        square_entry_box.config(state='normal')
        square_entry_box.delete(0, END)
        square_entry_box.config(state='readonly')


# Set back command for previous tab
def back():
    nb.tab(0, state='normal')
    nb.tab(1, state='disabled')


# Set button frame for square
square_button_frame = Frame(square_frame, bd=0)
square_button_frame.pack()

# Set calculate button for square
square_calculate_button = Button(square_button_frame, text='Calculate', bd=1, command=square_cmd_calculate)
square_calculate_button.grid(padx=30, pady=2, row=0, column=0, sticky=W)

# Set clear button for square
square_clear_button = Button(square_frame, text='Clear', bd=1, command=square_cmd_clear)
square_clear_button.pack(anchor=SE, side=RIGHT)

# Set result entry box for square
square_entry_box = Entry(square_frame, width=10, justify=CENTER, state='readonly', bd=0)
square_entry_box.pack(pady=10, padx=10,  anchor=S, ipadx=20)

square_back_button = Button(square_frame, text='<<<Back', bd=1, command=back)
square_back_button.pack(anchor=SW, side=BOTTOM)

root.mainloop()
