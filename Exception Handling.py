# Error - Mistake
# Exception -
# Syntax - Language
# Try block contains code that may raise an error
# Except block contains code that handles the exception

# Syntax error -  terminates the program
# Exception error continues with the program (the flow of the code is not interrupted)

amount = 10000
if amount > 2999:
    print("You are eligible to purchase Dsa Self Paced")

    def favourite_ice_cream():
        ice_creams = [
            "chocolate"
            "vanilla"
            "strawberry"
        ]
    print(favourite_ice_cream())


def sms():
    msg = "Marie,have a lovely day!"
    print(msg)
    return msg

for numbers in range(10):
    count = numbers
    print("the count is:", count)

file_handler = open('openlabs.txt', 'r')
print(file_handler.read())

def divide(x,y):
    try:
        result = x // y
        print("Yeah ! Your answer is:", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

print(divide(3,2))