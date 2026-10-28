import re

m = input("Enter mobile number: ")

if re.match('^[6-9][0-9]{9}$', m):
    print("Valid mobile number")
else:
    print("Invalid mobile number")