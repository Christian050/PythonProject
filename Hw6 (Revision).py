# With what we have studied so far, what is your outlook on the course?
# Build two programs based on the knowledge you have so far.
# Your program should incorporate not just a single branch of Python.
# I encourage collaboration where need be.
#
# Submission
# To my email not later than;
# Wednesday,23 March 2022, 17:00GMT

import modules_3
import datetime as datetime
import pyttsx3 as tts
import random
voice = tts.init()
fv = voice.getProperty('voices')
voice.setProperty('rate', 170)
voice.setProperty('voice', fv[1].id)

User_name = modules_3.Human['name']
User_age = modules_3.Human['age']
User_country = modules_3.Human['country']
# v = 'Okay',User_name,',you are',User_age,'and from',User_country
# voice.say(v)
# voice.runAndWait()
# print('Okay',User_name,',you are',User_age,'and from',User_country,'\n')
voice.say('Enter your email\n')
voice.runAndWait()
print('Now enter your Email')
Email = input('Enter email\n')
voice.say('Here are your details')
print('Name:', User_name, '\nAge:', User_age, '\nCountry:', User_country, '\nEmail:', Email)
# print(Email)
voice.say('Wanna play a game?')
voice.runAndWait()
Choice = input('Y/N\t')
if Choice == 'Y':
    print('Lets get started then')
    voice.say('This is a guess game,'
              '  guess a number between one and twenty')
    voice.runAndWait()
    num = random.randrange(1, 20)
    guess = int(input("Guess a number between 1 and 20\n"))
    while guess != num:
        if guess < num:
            voice.say('Wrong guess higher')
            voice.runAndWait()
            print("Wrong , Guess higher"),
            guess = int(input("\nGuess a number between 1 and 20\n"))
        else:
            voice.say('Wrong, guess lower')
            voice.runAndWait()
            print("Wrong , Guess Lower")
            guess = int(input("\nGuess a number between 1 and 20\n"))

    voice.say('You won the game!')
    voice.runAndWait()
    print("Correct, You guessed right")
elif Choice == 'N':
    voice.say('Okay')
    print('Alright, later then')
    Poem = open("Hope.txt", "r")
    voice.say('Want to read a poem?')
    voice.runAndWait()
    choice = input('Want to read a poem?\n Y/N\t')
    if choice == 'Y':
        print(Poem.read())
    else:
        print('Okay')
date = datetime.datetime.now()
print(date)
voice.say('Thank you for your time')
voice.runAndWait()
