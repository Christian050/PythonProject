from tkinter import *
from tkinter import ttk
from tkinter import messagebox



master = Tk()
master.title("Currency Convertor")
master.geometry("500x500")

# Tabs
nb = ttk.Notebook(master)
nb.pack(pady=5)

#Two frames
currency_frame = Frame(nb, width=480, height=480)
conversion_frame = Frame(nb, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

# Add Tabs
nb.add(currency_frame, text="Currency")
nb.add(conversion_frame, text="Convert")

# Disable 2nd Tab
nb.tab(1, state='disabled')

# Currency
##########

# Create Lock & Unlock Commands (functions)
def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning("Warning!", "You Didn't Fill Out All The Fields")
    else:
        # Disable Entry Boxes
        home_entry.config(state='disabled')
        conversion_entry.config(state='disabled')
        rate_entry.config(state='disabled')
        # Enable Tabs
        nb.tab(1, state='normal')
        # Change Tab Fields
        amount_label.config(text=f'Amount of {home_entry.get()} to convert to {conversion_entry.get()}')
        converted_label.config(text=f'Equals this many {conversion_entry.get()}')
        convert_button.config(text=f'Convert from {home_entry.get()}')

def unlock():
    # Enable Entry Boxes
    home_entry.config(state='normal')
    conversion_entry.config(state='normal')
    rate_entry.config(state='normal')
    # Disable Tabs
    nb.tab(1, state='disabled')

# Info Command
def info():
    messagebox.showinfo('Info', "    In GHC\n\n USD => 10.5\n EUR => 9.10")

home = LabelFrame(currency_frame, text="Currency")
home.pack(pady=20)

# Home Entry Box
home_entry = Entry(home, font=("Helvetica", 24))
home_entry.pack(pady=10, padx=10)

# Conversion Currency Frame
conversion = LabelFrame(currency_frame, text="Conversion Currency")
conversion.pack(pady=20)

# Convert to Label
conversion_label = Label(conversion, text="Currency To Convert To...")
conversion_label.pack(pady=15)

# Convert to Entry
conversion_entry = Entry(conversion, font=("Helvetica", 24))
conversion_entry.pack(pady=10, padx=10)

# Rate Label
rate_label = Label(conversion, text="Current Conversion Rate\n(Click Info for Rate in GHC)")
rate_label.pack(pady=10)

# Rate Entry
rate_entry = Entry(conversion, font=("Helvetica", 24))
rate_entry.pack(pady=10, padx=10)


# Button Frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

# Create buttons
lock_button = Button(button_frame, text="Lock", command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="Unlock", command=unlock)
unlock_button.grid(row=0, column=2, padx=10)

# Info button
Inf = Button(button_frame, text="Info", command=info)
Inf.grid(row=0, column=1, padx=10)


# Conversion
##########
def convert():
    # Clear Converted Entry Box (if it's filled)
    converted_entry.delete(0, END)

    # Convert
    conversion = float(rate_entry.get()) * float(amount_entry.get())
    # Convert to Two Decimal Places
    conversion = round(conversion, 2)
    # Add Commas
    conversion = '{:,}'.format(conversion)
    # Update Entry Box
    converted_entry.insert(0, f'{conversion}')
# Add symbols for other currencies and an "info" button with messagebox to display rate of conversion and combobox/list in playground to display currency conversion

def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)


amount_label = LabelFrame(conversion_frame, text="Amount to Convert")
amount_label.pack(pady=20)


# Entry Box for Amount
amount_entry = Entry(amount_label, font=("helvetica", 24))
amount_entry.pack(pady=10, padx=10)


# Convert Button
convert_button = Button(amount_label, text="Convert", command=convert)
convert_button.pack(pady=20)

# Equals Frame
converted_label = LabelFrame(conversion_frame, text="Converted Currency")
converted_label.pack(pady=20)


# Converted Entry
converted_entry = Entry(converted_label, font=("Helvetica", 24), bd=0, bg="systembuttonface")
converted_entry.pack(pady=10, padx=10)


# Clear Button
clear_button = Button(conversion_frame, text="Clear", command=clear)
clear_button.pack(pady=20)

# Fake Label for Spacing
spacer = Label(conversion_frame, text="", width=69)
spacer.pack()


master.mainloop()
