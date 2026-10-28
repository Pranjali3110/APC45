# 13. Accept 10 numbers and sort them in ascending and descending order.

a = []
for i in range(10):
    a.append(int(input("Enter number: ")))
a.sort()
print("Ascending:", a)
a.sort(reverse=True)
print("Descending:", a)