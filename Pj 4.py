from tkinter import *
from tkinter import messagebox
import customtkinter
import pyttsx3 as tts
import tkintermapview

# Set voice
speech = tts.init()
female_voice = speech.getProperty('voices')
speech.setProperty('rate', 150)
speech.setProperty('voices', female_voice[1].id)

# Set root
root = customtkinter.CTk()
root.geometry("220x220")
root.title("Christian's Pharmacy")

# Background Image
bg = PhotoImage(file="images\pic1.png")

# Label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()