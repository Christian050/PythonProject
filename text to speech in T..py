from tkinter import *
import pyttsx3 as tts
import customtkinter

voice = tts.init()
female_voice = voice.getProperty('voices')
voice.setProperty('rate', 150)
voice.setProperty('voice', female_voice[1].id)

welcome = 'Welcome to the FBN Bank Chat Bot'
voice.say(welcome)
voice.runAndWait()

root = customtkinter.CTk()
root.title('')
root.geometry('385x190')
root.resizable(False, False)
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

label = customtkinter.CTkLabel(root, text='Text to Speech')
label.pack()

frame = customtkinter.CTkFrame(root, height=30)
frame.pack(pady=5)

Bot = customtkinter.CTkLabel(frame, text='', width=400, justify=CENTER)
Bot.pack(pady=10)


def cb():

    if user_ent.get().capitalize() == 'Hi':
        assistant_response = 'What can i do for you?'
        voice.say(assistant_response)
        voice.runAndWait()
        Bot.config(text=f'{assistant_response}')
        user_ent.delete(0, END)
    if user_ent.get().capitalize() == "Create account":
        assistant_response2 = 'Would you like me to direct you to the nearest branch?'
        voice.say(assistant_response2)
        voice.runAndWait()
        Bot.config(text=f'{assistant_response2}')
        user_ent.delete(0, END)
    if user_ent.get().capitalize() == "Yes":
        assistant_response3 = 'Whats your location?'
        voice.say(assistant_response3)
        voice.runAndWait()
        Bot.config(text=f'{assistant_response3}')
        user_ent.delete(0, END)
    elif user_ent.get().capitalize() == "No":
        assistant_done4 = 'Okay, download the FBN Bank app on google playstore or the apple app store' \
                                  'or open the FBN Bank webpage to create an account'
        voice.say(assistant_done4)
        voice.runAndWait()
        voice.stop()
        Bot.config(text=f'{assistant_done4}')
        user_ent.delete(0, END)
        assistant_done = 'Are you satisfied with the responses?'
        voice.say(assistant_done)
        voice.runAndWait()
        Bot.config(text=f'{assistant_done}')
        user_ent.delete(0, END)

    if user_ent.get().capitalize() == 'Yes':
        user_ent.placeholder_text('Yes/No')
        assistant_done2 = 'Thank you for using FBN Bank chat bot. Goodbye'
        voice.say(assistant_done2)
        voice.runAndWait()
        voice.stop()
        Bot.config(text=f'{assistant_done2}')
        user_ent.delete(0, END)

    elif user_ent.get().capitalize() == 'No':
        assistant_done3 = 'Please visit the nearest FBN branch or click this link to direct you to the FBN bank website.' \
                          ' \nGoodbye'
        voice.say(assistant_done3)
        voice.runAndWait()
        voice.stop()
        Bot.config(text=f'{assistant_done3}')
        user_ent.delete(0, END)
        link = 'https://www.fbnbankghana.com'
        user_ent.insert(0, link)
        root.destroy()

    if user_ent.get().capitalize() == 'Accra':
        assistant_response4 = 'The nearest branch is on ring road adjacent to the MTN Office'
        voice.say(assistant_response4)
        voice.runAndWait()
        Bot.config(text=f'{assistant_response4}')
        user_ent.delete(0, END)
        assistant_done = 'Are you satisfied with the responses?'
        voice.say(assistant_done)
        voice.runAndWait()
        Bot.config(text=f'{assistant_done}')
        user_ent.delete(0, END)

    if user_ent.get().capitalize() == 'Y':
        assistant_done2 = 'Thank you for using FBN Bank chat bot. Goodbye'
        voice.say(assistant_done2)
        voice.runAndWait()
        voice.stop()
        Bot.config(text=f'{assistant_done2}')
        user_ent.delete(0, END)

    elif user_ent.get().capitalize() == 'N':
        assistant_done3 = 'Please visit the nearest FBN branch or click this link to direct you to the FBN bank website.' \
                          ' \nGoodbye'
        voice.say(assistant_done3)
        voice.runAndWait()
        voice.stop()
        Bot.config(text=f'{assistant_done3}')
        user_ent.delete(0, END)
        link = 'https://www.fbnbankghana.com'
        user_ent.insert(0, link)


Chat = customtkinter.CTkButton(root, text='Chat', command=cb)
Chat.pack(pady=20)

user_ent = customtkinter.CTkEntry(width=200, justify=CENTER, text_font=('', 11, 'italic'))
user_ent.focus()
user_ent.pack()

root.mainloop()
