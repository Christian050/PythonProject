"""def fun(a):
    if a < 4:
        # throws ZeroDivisionError for a = 3
        b = a/(a - 0)
    #throws NameError if a >= 4
    print("value of b = ", b)
try:
    fun(3)
    fun(5)
#note that braces () are necessary here for multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")"""

def fun(a):
    if (a <= 10) and (a > 5):
        b = (a/(a + 0))
        print(b)
try:
    fun(7)
    fun(10)
except ZeroDivisionError:
    print("ZeroDivisionError has been handled")
except ValueError:
    print("ValueError has been handled")


# Formular Error
"""try:
    x = float(input("Enter first number:    "))
    y = float(input("Enter second number:   "))
    product = x * y
    if (x != 0) or (y != 0):
        raise print("You entered 0")
    print(product)
except TypeError:
    print("Invalid")"""



"""try:
    e = ValueError()
    e.strerror = "Name does not include numbers"
    Name = (input("What's your name?"))
    if Name.isdigit():
        raise e
           # print("Name does not include numbers")
    if type(Name) == str:
        print("alright," + Name)
except ValueError:
    print("Invalid input", e.strerror)"""

"""
try:
     user_name = input("enter your name")
     if user_name.isdigit():
          raise print("invalid input,enter letters only")
     else:
            print("alright,",user_name)
except TypeError:
     pass
"""