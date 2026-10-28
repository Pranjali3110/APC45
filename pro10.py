# Q10. A company insures its drivers in the following cases:
# If the driver is married.
# If the driver is unmarried, male and above 30 years of age.
# If the driver is unmarried, female and above 25 years of age.
# In all the other cases, the driver is not insured.
# Write a PYTHON program to determine whether the driver is insured or not.

married = input("Is the driver married? (yes/no): ")
gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if married == "yes":
    print("Driver is Insured")
elif married == "no" and gender == "male" and age > 30:
    print("Driver is Insured")
elif married == "no" and gender == "female" and age > 25:
    print("Driver is Insured")
else:
    print("Driver is Not Insured")