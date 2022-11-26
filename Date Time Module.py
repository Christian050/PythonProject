""""#DateTime Module
import datetime
datetime_object = datetime.datetime.now()
print(datetime_object)"""
# We can also use the TODAY(),in generating the current date.

"""import datetime
datetime_object = datetime.date.today()
print(datetime_object)"""

# A simple program to receive outputs from a user.Then you display the inputs and the current date

# import datetime
# Name = input("Input your name")
# if Name.isalpha():
#     print("Okay:" + Name)
# # else:
# #     print("Name not valid, enter your name")
# Address = input("Enter your address")
# Current_Date = datetime.date.today()
# print(Name)
# print(Address)
# print(Current_Date)

"""
#Indicate current day, year and month
from datetime import date
today = date.today()

print("Current Year:", today.year)
print("Current Month:", today.month)
print("Current Day:", today.day)
"""
# Date formats
# MM/DD/YY
# DD/MM/YY
# YY/DD/MM

# current date and time
from datetime import datetime
now = datetime.now()

T = now.strftime("%H:%M:%S")
print("Time:", T)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

s3 = now.strftime("%Y/%d/%m, %H:%M:%S")
# YY/dd/mm H:M:S format
print("s3:", s3)

# strftime() defined under the date, datetime and time classes.
# This is a method that creates a formatted string, from a given object.
# strptime() conventions

# import datetime
# now = datetime.datetime.now()
# print(now.strftime("Date:%D"))
# print(now.strftime("Date:%F"))
# print(now.strftime("Day:%A"))
# print(now.strftime("Year:%Y"))
# print(now.strftime("Month:%b"))
# print(now.strftime("Time:%T"))

'''
# You should know this(Basics)
print(now.strftime("Date:%a"))
print(now.strftime("Date:%b"))
print(now.strftime("Day:%-m"))
print(now.strftime("Year:%-y"))'''


# strptime() Function
# string to datetime object

from datetime import datetime
date_string = ("04 June, 2022")
print("date_string =", date_string)

# subtract a week(7 days) from a given date in Python
# from datetime import datetime, timedelta
# given_date = datetime(2020, 2, 25)
# print("Given date")
# print(given_date)
# days_to_subtract = 7
# res_date = given_date - timedelta(days = days_to_subtract)
# print('New date')
# print(res_date)

# from datetime import datetime, timedelta
# given_date = datetime(2022, 3, 9)
# print(given_date)
# res_date = timedelta(17, 8, 50)
# print(res_date)



# Name = input("Input your name: ")
# address = input('Enter address: ')
# while True:
#     if Name != Name.isalpha():
#         print("Okay:" + Name + address)
#         break
#     else:
#         # if Name.isnumeric() or Name.isalnum():
#             print("Name not valid, enter your name")
#             # Name = input('Input your name:')



# user_name = input('Enter username').isalpha()
# address = input('Enter address')
# new_user_name = input('Enter address').isalpha()
# max_att = 2
# while user_name is True:
#      print(input('Enter address'))
# else:
#        print("Wrong username,attempts left: 2", new_user_name)
#  if user_name is not True:
#      print(input(user_name))

# user_name = input('Enter your username')
# if (user_name == float()) or user_name == int():
#     print('Wrong input,enter your username')
# else:
#     print(input("Enter address"), user_name)


# subtract a week(6 days) from a given date in Python
# from datetime import datetime, timedelta
# given_date = datetime(2020, 2, 25)
# print("Given date")
# print(given_date)
# days_to_subtract = 6
# res_date = given_date - timedelta(days = days_to_subtract)
# print('New date')
# print(res_date)

# from datetime import timedelta
# given_date = input('Enter date')
# print('Given Date')
# print(given_date)
# days_to_subtract = 6
# new_date =  - timedelta(days = days_to_subtract)
# print('New date')
# print(new_date)

# from datetime import datetime.
# date_time_str = '18/09/19 01:55:19'
# date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
#
# print("The type of the date is now", type(date_time_obj))


######
# from datetime import datetime,timedelta
# user_input = input("Enter date and time (DD/MM/YY) %H:%M")
# given_date = user_input
# print("Given Date")
# print(given_date)
# date_time_obj = datetime.strptime(given_date, '%d/%m/%y')
# new_date = date_time_obj - timedelta(days=6)
# print('New date')
# print(new_date)

# from datetime import datetime
# given_date = datetime(2022, 3, 8)
# print(given_date)

# find the day of the week of a given date:(2020,7,26)
# from datetime import datetime
# given_date = datetime(2020, 7, 26)
# Day = given_date.strftime('%A')
# print(Day)

# add a week(7 days and 12 hours) to a given date: (2020, 6, 26)
# from datetime import datetime, timedelta
# date = datetime(2020,6,26)
# new_date = date + timedelta(days=7,hours=12)
# print(new_date)