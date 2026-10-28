# 5. Create a list of student names. Remove:
# First student
# Last student
# A specific student by name
# Display the remaining list.

students = ["Pranjali", "Prabha", "Anjali", "Sneha", "Varad"]

students.pop(0)
students.pop()
students.remove("Anjali")

print("Remaining list:", students)