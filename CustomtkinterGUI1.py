from tkinter import *
import tkinter.messagebox
import customtkinter

# Set Root
root = customtkinter.CTk()

# Set Geometry
root.geometry('500x500')

# Set CTK Appearance (Optional)
customtkinter.set_appearance_mode('Dark')

# Set CTk Color Theme (Optional)
customtkinter.set_default_color_theme('dark-blue')

# Set Label
label = customtkinter.CTkLabel(root, text='Custom Tkinter')
label.pack(pady=5)

# Set Entry
entry_color = customtkinter.CTkEntry(root, width=50)
entry_color.pack()


# Command change_color
def change_color():
    if entry_color.get().capitalize() == 'Light':
        customtkinter.set_appearance_mode('Light')
        tkinter.messagebox.showinfo('Done', 'Appearance has been set to light mode')
    if entry_color.get().capitalize() == 'Dark':
        customtkinter.set_appearance_mode('Dark')
        tkinter.messagebox.showinfo('Done', 'Appearance has been set to dark mode')
    entry_color.delete(0, END)


# Set Button
button = customtkinter.CTkButton(root, text='Change Color', bd=0, command=change_color)
button.pack(pady=5)

root.mainloop()
