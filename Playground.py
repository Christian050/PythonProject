import pyttsx3 as tts
voice = tts.init()
fv = voice.getProperty('voices')
voice.setProperty('rate', 170)
voice.setProperty('voice', fv[1].id)


#Display product if greater than 1000
import pyttsx3 as tts
# voice = tts.init()
# voice.setProperty('rate', 150)
# voice.setProperty('voice', voice[1].id)
# voice.say('Enter first number')
# voice.runAndWait()
# num1 = int(input("Enter first  number\n"))
# voice.say("Enter second number")
# voice.runAndWait()
# num2 = int(input("Enter second number\n"))
# product = num1 + num2
# if product >= 1000:
#     # engine = pyttsx3.init()
#     # voices = engine.getProperty('voices')
#     # engine.setProperty('voice',voices[1].id)
#     # engine.setProperty('rate', 120)
#     voice.say(product)
#     voice.runAndWait()
#     print(product)
# else:
#     # engine = pyttsx3.init()
#     # voices = engine.getProperty('voices')
#     # engine.setProperty('voice', voices[0].id)
#     # # print(voices[0].id)
#     # engine.setProperty('rate', 120)
#     voice.say("Product failed to show because the result is less or not equal to 1000")
#     voice.runAndWait()
#     print('_______________','\n','Product failed to load because product !<= 1000')


#Print the sum of current number and previous number
# for x in range(9):
#     current_num = x + 1
#     previous_num = x
#     sum = current_num + previous_num
#     print('current_num:',current_num,'previous_num',previous_num,'sum:',sum)


#Print('Calculator''\n--------------')
# Ins = 'Input the first number, the operator  and the second number.\nThe calculator will print out the result.'
# voice.say(Ins)
# voice.runAndWait()
# print(Ins)
# voice.say('Enter a number')
# voice.runAndWait()
# n1 = float(input('Enter a number\n'))
# voice.say('Okay,  Select an operator')
# voice.runAndWait()
# op = input('Select an operator(-,+,*,/)\n')
# voice.say('Finally,Enter the second number')
# voice.runAndWait()
# n2 = float(input('Enter a second number\n'))
# # op = ('-','+','*','/')
# if op == '-':
#     sSub = n1,'minus',n2, 'equals'
#     result = n1 - n2
#     Ans = n1 - n2
#     voice.say(sSub)
#     voice.runAndWait()
# if op == '+':
#     sAdd = n1,'+',n2,'equals'
#     result = n1 + n2
#     voice.say(sAdd)
#     voice.runAndWait()
# if op == '*':
#     sMp = n1,'multiplied by',n2,'equals'
#     result = n1 * n2
#     voice.say(sMp)
#     voice.runAndWait()
# if op == '/':
#     sDiv = n1,'divided by',n2,'equals'
#     result = n1 /n2
#     voice.say(sDiv)
#     voice.runAndWait()
#
# voice.say(result)
# voice.runAndWait()
# voice.stop()
# print('Answer\n>>>',result)



#Print characters in a string that are present in an even index string
# str = 'pynative'  # display 'p' 'n' 't' 'v'
# word = input('enter a word\n')
# print('original string:',word)
# size = len(word)
# print('Printing out only even index numbers')
# for i in range(0, size -1, 2):
#     print('index[',i,']',word[i])
# for i in range(0,size -1, 2):
#     print(word[i])
# so it starts from the empty space

#Simpler way
# word = input('Enter a word\n')
# size = len(word)
# for even_ltt in range(0, size-1, 2):
#     print(word[even_ltt])
# or
#Convert to list
# word = input('Enter a word\n')
# list_ = list(word)
# for i in list_[0::2]:
#     print(i)

# Remove first 'n' characters from a string(n == numbers)
# word = input('enter a word\n')
# def remove_chars(word,para):
#     x = word[para:]
#     return x
# print(remove_chars(word, 2))
# print(remove_chars(word,4))

#Check if the first and last numbers are the same
# fn = int(input('Enter first Set Of Numbers\n'))
# sn = int(input('Enter Second Set Of Numbers\n'))
# if fn == sn:
#     print(fn, '\n',sn, '\n''The Result Is True')
# else:
#     print(fn,'\n',sn, '\n''The Result Is False')

#Display numbers divisible by 5 from a given list
# num_list = [10, 20, 33, 46, 55]
# for num in num_list:
#     if num %5 == 0:
#         print(num)


#return the count of a given substring from a string
# wrd = 'Emma is a good developer.Emma is a good writer'
# count = wrd.count('Emma')
# print('Emma appeared',count,'times')


# print pattern
# for num in range(11):
#     for i in range(num):
#         print(num, end='')
#     print('\n')



#Program to check if given number is a palindrome
#A palindrome is a number that is the same after reversed
# def palindrome(number):
#     print("original number", number)
#     original_num = number
#
#     # reverse the given number
#     reverse_num = 0
#     while number > 0:
#         reminder = number % 10
#         reverse_num = (reverse_num * 10) + reminder
#         number = number // 10
#
#     # check numbers
#     if original_num == reverse_num:
#         print("Given number palindrome")
#         voice.say('Given number palindrome')
#         voice.runAndWait()
#         voice.stop()
#     else:
#         voice.say('Given number not a palindrome')
#         voice.runAndWait()
#         voice.stop()
#         print("Given number is not palindrome")
# pdr = int(input('Enter a number\n'))
# palindrome(pdr)


#Create a new list from a two list using the list condition
# def merge_list(list1, list2):
#     result_list = []
#
#     # iterate first list
#     for num in list1:
#         # check if current number is odd
#         if num % 2 != 0:
#             # add odd number to result list
#             result_list.append(num)
#
#     # iterate second list
#     for num in list2:
#         # check if current number is even
#         if num % 2 == 0:
#             # add even number to result list
#             result_list.append(num)
#     return result_list
#
#
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# print("result list:", merge_list(list1, list2))

#Program to extract each digit from an integer in the reverse order
# number = int(input('Input numbers\n'))
# print("Given number", number)
# while number > 0:
#     # get the last digit
#     digit = number % 10
#     # remove the last digit and repeat the loop
#     number = number // 10
#     print(digit, end=" ")


#Program to calculate income tax for given income
# income = int(input('Enter income\n'))
# tax_payable = 0
# print("Given income", income)
#
# if income <= 10000:
#     tax_payable = 0
# elif income <= 20000:
#     # no tax on first 10,000
#     x = income - 10000
#     # 10% tax
#     tax_payable = x * 10 / 100
# else:
#     # first 10,000
#     tax_payable = 0
#
#     # next 10,000 10% tax
#     tax_payable = 10000 * 10 / 100
#
#     # remaining 20%tax
#     tax_payable += (income - 20000) * 20 / 100
#
# print("Total tax to pay is", tax_payable)


#Print multiplication table from 1 to 10
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end=" ")
#     print("\t\t")

#Print downward half pyramid with star(*)
# for i in range(6, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")


#Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# def exponent(base, exp):
#     num = exp
#     result = 1
#     while num > 0:
#         result = result * base
#         num = num - 1
#     print(base, "raises to the power of", exp, "is: ", result)
#
# exponent(5, 4)

# import tkinter as tk
# import sys
# from tkinter import *
# from tkinter.ttk import Combobox
# # show entry fields
# # set font style + size
# fs = ('Calibri Light', 20, 'italic')
# fs1 = ('Calibri Light', 11, 'italic')
# n = "New User"
# e = "Existing User"
#
# def show_entry_fields():
#    print('First Name =>\t %s\nLast Name => \t %s \nI.D => \t %s' % (e1.get(), e2.get(), e3.get()))# print fields and get entries
#
#
# def Btn_Click(event):
#    print('Double Click, Terminate')
#    sys.exit()
#
# # Set master and Label
#
# master = tk.Tk()
# # window = Tk()
# tk.Label(master, text='First Name', bg='Yellow', width=10).grid(row=0, pady=10)
# tk.Label(master, text='Last Name', bg='Yellow').grid(row=2, pady=10)
# tk.Label(master, text='I.D', bg='Yellow').grid(row=4, pady=10)
# master.config(bg="Yellow")
# master.title("SIM Reg Popup")
# master.geometry("355x195")
# master.resizable(0, 0)
#
# # Set entry (name from show_entry_fields)
# e1 = tk.Entry(master)
# e2 = tk.Entry(master)
# e3 = tk.Entry(master)
#
# # Set stringvar for combobox
# var = StringVar()
# var.set('one')
# var.data = (n, e)
# cb = Combobox(master, values=var.data, background='Yellow', foreground='Black')
# cb.place(x=210, y=10)
#
# # Set listbox
# lb = Listbox(master, height=5, bg='Yellow', selectmode='single', selectbackground='Yellow', selectforeground='Black')
# lb.data = ('MTN', 'AirtelTigo', 'Vodafone', 'Glo', 'Other')
# for num in lb.data:
#    lb.insert(END, num)
#    lb.place(x=218, y=50)
#
# # Set Radiobutton
# v0 = IntVar()
# v0.set(1)
# Rad1 = Radiobutton(master, text='Male', bg='Yellow', variable=v0, value=1)
# Rad1.place(x=30, y=128)
# Rad2 = Radiobutton(master, text='Female', bg='Yellow', variable=v0, value=2)
# Rad2.place(x=100, y=127)
#
#
#
# # Set grid
# e1.grid(row=0, column=1, columnspan=2)
# e2.grid(row=2, column=1, columnspan=2)
# e3.grid(row=4, column=1, columnspan=2)
#
# # Set buttons, commands and grid
# tk.Button(master, text='Quit', font=fs1, command=master.quit).place(y=163)
# tk.Button(master, text='Show', font=fs1, command=show_entry_fields).place(x=310, y=163)   # .grid(row=6, column=100, sticky=tk.E)
# tk.mainloop()

# A python code to accept 3 numbers and arrange them in ascending order
# user_input_1 = float(input('Enter first number\n'))
# user_input_2 = float(input('Enter second number\n'))
# user_input_3 = float(input('Enter third number\n'))
#
# List = [user_input_1, user_input_2, user_input_3]
# List.sort()
# print(List)
