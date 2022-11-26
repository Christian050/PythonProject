import customtkinter

root = customtkinter.CTk()
root.geometry('600x500')
root.title('Project 3')

entframe = customtkinter.CTkFrame(root)
entframe.pack(pady=5)

entlabel = customtkinter.CTkLabel(entframe, text='Input')
entlabel.pack()

ent = customtkinter.CTkEntry(entframe, width=300)
ent.pack()

root.mainloop()
