from gtts import gTTS
import os
class FormularError(Exception): pass
def parse_input(user_input):
    input_list = user_input.split()
    if len(input_list) != 3:

        raise FormularError("Input does not consist of three elements")
    n1, op, n2 = input_list
    try:
        n1 = int(n1)
        n2 = int(n2)
    except ValueError:
        raise FormularError("the first and third input must be numbers")
    return n1, op, n2
def calculate (n1, op, n2):
    if op == "+":
        return n1 + n2
    if op == "-":
        return n1 - n2
    if op == "*":
        return n1 * n2
    if op == "/":
        return n1 / n2
    raise FormularError('{0} is not a valid operator', format(op))
while True:
    user_input = input(">>> ")
    if user_input == "quit":
        break
    n1, op, n2 = parse_input(user_input)
    userinput = n1, op, n2
    # speech = gTTS(text=str(userinput), lang='en', slow=False)
    # speech.save('userinput.mp3')
    # os.system('userinput.mp3')
    result = calculate(n1, op, n2)
    print(result)
    res = "The sum for",userinput,"is",result
    speech = gTTS(text=str(res), lang="en", slow=False)
    speech.save("Final_result.mp3")
    os.system("Final_result.mp3")