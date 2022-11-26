email = input("Enter your email address: ").strip()
user_name = email[: email.index('@') +0: ]
domain = email[email.index('@') +1: ]
result = "Your username = {}\nYour domain = {}".format(user_name, domain)
print(result)

# import datetime
# print('Email Address Slicer')
# user_name = input("Enter your Username")
# domain_name = input("Enter domain name")
# my_email = user_name + "@" + domain_name + '.com'
# date = datetime.datetime.today()
# print('This is your email: ' + str.lower(my_email) + date)

