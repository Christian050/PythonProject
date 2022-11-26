# WRITE A PSEUDOCODE TO FIND THE AREA OF RECTANGLE

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

# Set root
root = Tk()

# Set Notebook
note = ttk.Notebook(root)
note.pack(pady=5)

# Geometry And Title
root.geometry("400x575")
root.title("Area of a Rectangle")
# root.resizable(False, False)

# Label Frame
ar = LabelFrame(root, text='Area of a Rectangle', width=10, labelanchor=N, bd=0)
ar.pack()


# Image
canvas = Canvas(ar, width=300, height=170)
canvas.pack(padx=45)
img = ImageTk.PhotoImage(Image.open('index.png'))
canvas.create_image(20, 20, anchor=NW, image=img)

# Label Frames
length_lbf = LabelFrame(ar, text='Length', width=70, height=70)
length_lbf.pack(pady=30)

width_lbf = LabelFrame(ar, text='Width', width=70, height=70)
width_lbf.pack(pady=10)

res = LabelFrame(ar, text='Result', width=70)
res.pack(pady=10)


# Entry
length_entry = Entry(length_lbf, width=70)
length_entry.pack(pady=20, padx=20)

width_entry = Entry(width_lbf, width=70)
width_entry.pack(pady=20, padx=20)

res_entry = Entry(res, width=70)
res_entry.pack(pady=20, padx=20)
res_entry.config(state='disabled')


# Commands
def done():
    res_entry.delete(0, END)
    if not length_entry.get().isnumeric() and not width_entry.get().isnumeric():
        messagebox.showerror("Error!", "Enter numbers/digits.")
        res_entry.config(state='disabled')
    # if length_entry.get().isalnum() or width_entry.get().isalnum():
    #     messagebox.showwarning("Error!", "Includes letters. Enter only\n\t numbers")
    else:
        res_entry.config(state='normal')
        area = float(length_entry.get()) * float(width_entry.get())
        res_entry.insert(0, f'{area}')
        # res_entry.config(state='disabled')


def clear():
    length_entry.delete(0, END)
    width_entry.delete(0, END)
    res_entry.delete(0, END)
    res_entry.config(state='disabled')
    # if not length_entry.get() or not width_entry.get() or not res_entry.get():
    #     messagebox.showerror("ERROR!", "Nothing to clear.")


# Button find area
btn = Button(ar, text='Find Area', width=70, height=2, bd=1, command=done)
btn.pack()

# Button clear
btn_clr = Button(ar, text='Clear', width=70, height=2, bd=1, command=clear)
btn_clr.pack()

root.mainloop()
