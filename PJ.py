from tkinter import *
from tkinter import messagebox
import customtkinter
import pyttsx3 as tts
import tkintermapview


# Setting Voice
speech = tts.init()
female_voice = speech.getProperty('voices')
speech.setProperty('rate', 150)
speech.setProperty('voice', female_voice[1].id)


# Root
root = customtkinter.CTk()
root.geometry('500x500')
root.title('Pharmacy')


# Frames
first_frame = customtkinter.CTkFrame(root)
first_frame.pack(fill='both', expand=1)

second_frame = customtkinter.CTkFrame(root, bd=1)
second_frame.pack(fill='both', expand=1)

second_label = customtkinter.CTkLabel(second_frame, text='Show Map Location')
second_label.pack(side=TOP, pady=10)


# # Scroll Bar
# sb = Scrollbar()
# sb.pack(fill='y', side='right')


# Map View
mv = tkintermapview.TkinterMapView(second_frame, width=300, height=250, corner_radius=10)
mv.set_position(5.6037, -0.1870)
mv.set_zoom(7)
mv.set_address('Accra, Ghana')
mv.pack(pady=5)


def set(event):
    if btn_set:
        btn_set.bind("<Enter>", set)
        messagebox.showinfo('Done', 'Location Set Successfully')
    pass


# Set Button
btn_set = customtkinter.CTkButton(second_frame, text='Set', command=set)
btn_set.pack()


root.mainloop()
