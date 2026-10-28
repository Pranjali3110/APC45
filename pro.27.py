# Q27. Email Validator
# Validate whether a given email address follows a valid format.

email = input("Enter email address: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")