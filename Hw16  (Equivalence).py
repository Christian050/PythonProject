# WRITE A PSEUDOCODE TO CHECK EQUIVALENCE OF TWO NUMBERS. USE IF STATEMENT.

from tkinter import *
from tkinter import messagebox

# Set root
root = Tk()

# Set title
root.title('Equivalence of Two Numbers')

# Set geometry
root.geometry("237x230")

# Set resizable
root.resizable(0, 0)

# Set label frame
equi_frame = LabelFrame(root, text='Equivalence Of Two Given Numbers', labelanchor=N, bg='turquoise', bd=0)
equi_frame.pack()

# Set label frame and entry for input
entry_1_label = LabelFrame(equi_frame, text='First Entry ', bd=0, labelanchor=W, bg='turquoise')
entry_1_label.pack(pady=20, padx=50)

entry_1_entry = Entry(entry_1_label, width=10, justify=CENTER)
entry_1_entry.pack(padx=5, pady=5)
entry_1_entry.focus()

entry_2_label = LabelFrame(equi_frame, text='Second Entry', bd=0, labelanchor=W, bg='turquoise')
entry_2_label.pack(pady=20)

entry_2_entry = Entry(entry_2_label, width=10, justify=CENTER)
entry_2_entry.pack(padx=5, pady=5)


# Set command find_equivalence
def find_equivalence():
    if entry_1_entry.get().isnumeric() and entry_2_entry.get().isnumeric():
        # result_entry.config(state='normal')
        if entry_1_entry.get() > entry_2_entry.get():
            messagebox.showinfo("", f'{entry_1_entry.get()} is greater than {entry_2_entry.get()}!')
        if entry_1_entry.get() < entry_2_entry.get():
            messagebox.showinfo("", f'{entry_2_entry.get()} is greater than {entry_1_entry.get()}!')
        if entry_1_entry.get() == entry_2_entry.get():
            messagebox.showinfo("", f'The two numbers, {entry_1_entry.get()} and {entry_2_entry.get()} are equal!')
    else:
        messagebox.showerror("Retry", "Input Invalid!")


def clear():
    if entry_1_entry.get() or entry_2_entry.get():
        entry_1_entry.delete(0, END)
        entry_2_entry.delete(0, END)
        messagebox.showinfo("", "All cleared!")
    else:
        messagebox.showerror("Error", 'Nothing to clear!')


# Set Button find_equivalence
button_find = Button(equi_frame, text='Find Equivalence', command=find_equivalence)
button_find.pack(pady=10)

button_clear = Button(equi_frame, text='Clear', command=clear)
button_clear.pack()


root.mainloop()
