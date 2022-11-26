from tkinter import *
import customtkinter
import datetime
from datetime import date

root = customtkinter.CTk()
root.title("Age Calculator App")
root.geometry('400x570')
root.resizable(False, False)
# root.iconbitmap('C:/Users/NYAG/PycharmProjects/pythonCustoms/icons/cal-grey.ico')
customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme("blue")

# fonts
txt = ("Roboto Medium", -16)
d_txt = ("Roboto Medium", -20)
fg = ("white", "gray38")
bg = 'Turquoise'
tc = 'black'

# Main Frame
mainframe = customtkinter.CTkFrame(root, corner_radius=15)
mainframe.pack(expand=True, fill="both", pady=10, padx=10)
mainframe.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)


# functions
def calculate():
    # display_output.selection_clear()
    name = name_entry.get()
    year = year_entry.get()
    month = month_entry.get()
    day = day_entry.get()
    birth_date = datetime.date(int(year), int(month), int(day))
    day = birth_date.strftime('And you were born on %A')
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    results = "Heyy {user}!!!.\nYou are {age} years old!!!\n{day}".format(user=name, age=age, day=day)
    display_output.set_text(results)


def changeMode():
    if switch.get() == 1:
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")


def clear():
    name_entry.delete(0, END)
    day_entry.delete('0', END)
    month_entry.delete('0', END)
    year_entry.delete('0', END)
    display_output.set_text(text="")


# =========================================================== #
# Input display Interface/ labels, entry & selection boxes
# =========================================================== #
# Name & Entry label
name_label = customtkinter.CTkLabel(mainframe, text='Name: ', text_font=txt, width=1, justify=LEFT)
name_label.pack(padx=10, anchor=W)

name_entry = customtkinter.CTkEntry(mainframe, width=700, text_font=txt, placeholder_text='enter name here')
name_entry.pack(padx=10, anchor=W)

# day label & entry
day_label = customtkinter.CTkLabel(mainframe, text='Day: ', text_font=txt, width=1, justify=LEFT)
day_label.pack(padx=10, anchor=W)

day_entry = customtkinter.CTkEntry(mainframe, width=700, text_font=txt, placeholder_text='enter day here')
day_entry.pack(padx=10, anchor=W)

# month label & entry
month_label = customtkinter.CTkLabel(mainframe, text='Month: ', text_font=txt, width=1, justify=LEFT)
month_label.pack(padx=10, anchor=W)

month_entry = customtkinter.CTkEntry(mainframe, width=700, text_font=txt, placeholder_text='enter month here')
month_entry.pack(padx=10, anchor=W)

# year label & entry
year_label = customtkinter.CTkLabel(mainframe, text='Year: ', text_font=txt, width=1, justify=LEFT)
year_label.pack(padx=10, anchor=W, )

year_entry = customtkinter.CTkEntry(mainframe, width=700, text_font=txt, placeholder_text='enter year here')
year_entry.pack(padx=10, anchor=W)

# =========================================================== #
# Buttons code
# =========================================================== #
b_frame = customtkinter.CTkFrame(mainframe)
b_frame.pack(padx=10, pady=15, anchor=W)

# calculate button
calculate_button = customtkinter.CTkButton(b_frame, text='Calculate', text_font=txt, corner_radius=8, command=calculate)
calculate_button.grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=5, sticky=W)

spacer = customtkinter.CTkLabel(b_frame, text="", width=40)
spacer.grid(row=0, column=1)

# clear button
clear_button = customtkinter.CTkButton(b_frame, text='Clear', text_font=txt, corner_radius=8, command=clear)
clear_button.grid(row=0, column=2, padx=10, pady=10, ipadx=10, ipady=5, sticky=E)

# =========================================================== #
# Display output code
# =========================================================== #
# output display
display_output = customtkinter.CTkLabel(master=mainframe, text="", text_font=d_txt, width=700, height=150, fg_color=fg,
                                        justify=LEFT)
display_output.pack(padx=10, pady=10, anchor=W)

# ============== switch & close code ========================= #
c_frame = customtkinter.CTkFrame(mainframe)
c_frame.pack(padx=10, pady=10, anchor=W)

# close button
close_button = customtkinter.CTkButton(c_frame, text='Close', text_font=txt, text_color=tc, fg_color=bg,
                                       command=root.destroy)
close_button.grid(row=0, column=2, padx=10, pady=10, sticky='e')

# spacer
space = customtkinter.CTkLabel(c_frame, text="", width=90)
space.grid(row=0, column=1, pady=10)

# switch
switch = customtkinter.CTkSwitch(c_frame, text='Dark Mode', command=changeMode)
switch.select()
switch.grid(row=0, column=0, padx=10, pady=10, sticky='w')

root.update()
root.mainloop()
