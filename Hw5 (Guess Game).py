import random
num = random.randrange(1, 20)
guess = int(input("Guess a number between 1 and 20"))
while guess != num:
    if guess < num:
        print("Wrong, Guess higher"),
        guess = int(input("\nGuess a number between 1 and 20"))
    else:
        print("Wrong, Guess Lower")
        guess = int(input("\nGuess a number between 1 and 20"))

print("Correct, You guessed right")
