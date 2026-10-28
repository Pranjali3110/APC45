import re

email = input("Enter email: ")

if re.search("@", email):
    print("Valid email")
else:
    print("Invalid email")