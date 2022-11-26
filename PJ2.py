from tkinter import *
import tkintermapview


dark = 'White'
ft = ('Helvetica', 20, 'italic')
mb = '#99a3a4'
aft = ('', 11, 'italic')


# root
root = Tk()
root.title('Pharmaceutical Delivery Services')
root.geometry('600x600')
root.config(bg="blue")

intro_label = Label(root, text='Step1\nPlease Fill The Entries Below To Proceed To The Next Step.', bg=dark,
                    font=('helvetica', 15, 'bold', 'italic'))
intro_label.pack(side=TOP, anchor=CENTER, pady=20)


######################################################################################
# COMMANDS
######################################################################################


# Def Command Clear Name
def clear_name():
    if name_entry.get():
        name_entry.delete(0, END)


# Def Command Clear Email
def clear_email():
    if email_entry.get():
        email_entry.delete(0, END)


# Def Command Clear Age
def clear_age():
    if age_entry.get():
        age_entry.delete(0, END)
    if not age_entry.get().isnumeric():
        age_entry.delete(0, END)


# Def Command Next
def nxt():
    if name_entry.get().isnumeric():
        name_entry.delete(0, END)
    if '@' not in email_entry.get():
        email_entry.delete(0, END)
    if not age_entry.get().isnumeric():
        age_entry.delete(0, END)
    if name_entry.get() and age_entry.get() and email_entry.get():
        top = Toplevel(root)
        top.geometry('600x650')
        top.config(bg=dark)
        # top.resizable(False, False)

        # Introduction
        intro_label2 = Label(top, text='Step2\nAlmost There, Fill This To Proceed To The Next Step.', bg=dark,
                             font=('helvetica', 15, 'bold', 'italic'))
        intro_label2.pack(side=TOP, anchor=CENTER, pady=20)

        #######################################################
        # Commands
        #######################################################

        # Def Set Position
        def sp():
            if location_entry.get():
                map_widget.set_address(f'{location_entry.get()}, Ghana', marker=True)
                map_widget.set_zoom(15)

        def clr():
            pbk_entry.delete(0, END)

        def stp3():
            if pbk_entry.get() and location_entry.get():
                master = Toplevel(root)
                master.geometry("600x600")
                master.config(bg=dark)
                master.resizable(False, False)

                # introduction
                intro_label3 = Label(top, text='Step3\nPlease Confirm The Data. ', bg=dark,
                                     font=('helvetica', 15, 'bold', 'italic'))
                intro_label3.pack(side=TOP, anchor=CENTER, pady=20)

        #######################################################
        # LABEL FRAMES
        ######################################################

        # PhoneBook
        pbk = LabelFrame(top, text='Phone No.', font=ft, labelanchor=N, bg=dark, bd=0)
        pbk.pack(pady=30, anchor=CENTER)

        # Longitude And Latitude Label Frame
        lnl_label_frame = LabelFrame(top, bd=0, bg=dark)
        lnl_label_frame.pack()

        # Location Label Frame In 'lnl_label_frame'
        location_label_frame = LabelFrame(lnl_label_frame, text='Location  ', labelanchor=W, bd=0, font=ft, bg=dark)
        location_label_frame.pack(pady=5, padx=5)

        #####################################################
        # ENTRIES
        #####################################################

        # Phonebook Entry
        pbk_entry = Entry(pbk, width=10, justify=CENTER, font=ft)
        pbk_entry.pack(pady=10, padx=5)

        # Location Entry
        location_entry = Entry(location_label_frame, justify=CENTER, width=8, font=ft)
        location_entry.pack()

        ###################################################
        # MAP VIEW
        ###################################################

        # Map View
        map_widget = tkintermapview.TkinterMapView(top, width=250, height=250, corner_radius=10)
        map_widget.set_position(5.614818, -0.205874)
        map_widget.set_zoom(5)
        map_widget.pack(pady=20)

        #################################################
        # BUTTONS
        #################################################

        # Button Set Position With Command 'sp'
        btn_set = Button(lnl_label_frame, text='Set', command=sp, width=10, bg=mb)
        btn_set.pack(anchor=CENTER, pady=10)

        # Button Next with command clr
        btn_clear = Button(pbk, text='Clear', width=10, bg=mb, command=clr)
        btn_clear.pack(side=BOTTOM, anchor=CENTER, pady=10)

        # Button Next
        btn_next = Button(top, text='Next', bg=mb, width=10, command=stp3)
        btn_next.pack(side=BOTTOM, anchor=E)

#####################################################################################
# LABEL FRAMES
#####################################################################################


# Name Label Frame
name_label_frame = LabelFrame(root, text='Enter Name Here', font=ft, labelanchor=N, bg=dark, bd=0)
name_label_frame.pack(pady=30)

# Email Label Frame
email_label_frame = LabelFrame(root, text='Email Address', font=ft, labelanchor=N, bg=dark, bd=0)
email_label_frame.pack(pady=30)

# Age Label Frame
age_label_frame = LabelFrame(root, text='Age', font=ft, labelanchor=W, bg=dark, bd=0)
age_label_frame.pack(pady=30, side=LEFT)

#####################################################################################
# ENTRIES
#####################################################################################

# Name Entry
name_entry = Entry(name_label_frame, width=30, justify=CENTER, font=ft)
name_entry.pack(pady=10, padx=5)

# Email Entry
email_entry = Entry(email_label_frame, width=30, font=ft)
email_entry.pack(pady=10, padx=5)

# Age Entry
age_entry = Entry(age_label_frame, width=5, justify=CENTER, font=ft)
age_entry.pack(pady=10, padx=5)

#####################################################################################
# RADIOBUTTON
#####################################################################################

v0 = IntVar()
v0.set(1)
r1 = Radiobutton(root, text="Male", variable=v0, value=1, bg=dark, activebackground=dark, font=ft)
r2 = Radiobutton(root, text="Female", variable=v0, value=2, bg=dark, activebackground=dark, font=ft)
r1.place(x=350, y=500)
r2.place(x=450, y=500)


######################################################################################
# BUTTONS
######################################################################################

# Name Clear Button
clear_button = Button(name_label_frame, text='Clear', command=clear_name, width=10, bg=mb)
clear_button.pack()

# Email Clear Button
clear_button2 = Button(email_label_frame, text='Clear', command=clear_email, width=10, bg=mb)
clear_button2.pack()

# Age Clear Button
clear_button3 = Button(age_label_frame, text='Clear', command=clear_age, width=10, bg=mb)
clear_button3.pack()

# Next Button
next_button = Button(root, text='Next', command=nxt, width=10, bg=mb)
next_button.pack(side=BOTTOM, anchor=E)

root.mainloop()
