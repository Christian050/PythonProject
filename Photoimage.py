from tkinter import *

root = Tk()
root.title("Photo Image Project")
root.geometry("500x500")

bg = PhotoImage(file="C:/Users/pc/OneDrive/Pictures/Screenshots/Screenshot 2022-11-07 000408.png")

# LAbel
ml = Label(root, image=bg)
ml.place(x=0, y=0, relwidth=1, relheight=1)

# Text
mt = Label(root, text='Welcome to Python', fg='white')
mt.pack()

root.mainloop()