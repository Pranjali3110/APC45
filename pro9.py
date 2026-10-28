# 9. Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.

cities = ["Sangli", "Mumbai", "Delhi", "Kolhapur", "Pune"]
city = input("Enter city name: ")
if city in cities:
    print("City exists in the list.")
else:
    print("City does not exist in the list.")