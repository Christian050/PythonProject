# simple game with instructions
# import random
# Box1 = random.randrange()
# Box2 = random.randrange()
# Box3 = random.randrange()
# Chocolate = random.randrange(Box1,Box2,Box3)
# userguess = int(input("Guess what box the chocolate is in"))
# while userguess != Chocolate:
#     if Chocolate == Box:
#         print("You Won the Game!")
#         userguess = int(input("\nGuess what box the chocolate is in"))
# print('Wrong,Choose another box')


from gtts import gTTS
import os
import random
print('Guess Game')
Instructions = "Welcome to High Low, guess a number between one and twenty"
Speech = gTTS(text=Instructions, lang='en', slow=False)
Speech.save("Instructions.mp3")
os.system("Instructions.mp3")
print(Instructions)
num = random.randrange(1, 20)
guess = int(input("Guess a number between 1 and 20"))
while guess != num:
    if guess < num:
        whi = "Wrong,guess higher"
        speech = gTTS(text=whi, lang='en', slow=False)
        speech.save("Guess Higher.mp3")
        os.system("Guess Higher.mp3")
        print("Wrong, Guess higher"),
        guess = int(input("\nGuess a number between 1 and 20"))
    else:
        print("Wrong, Guess Lower")
        wlo = "Wrong,Guess lower"
        speech = gTTS(text=wlo, lang="en", slow=False)
        speech.save("Guess Lower.mp3")
        os.system("Guess Lower.mp3")
        guess = int(input("\nGuess a number between 1 and 20"))
WinTG = "Congratulations,you won the game"
win = gTTS(text=WinTG, lang="en", slow=False)
win.save("win.mp3")
os.system("win.mp3")
print(WinTG)
