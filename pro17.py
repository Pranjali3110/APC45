# 17. Create two 3x3 matrices using nested lists and perform matrix addition.

a = [[1,2,3], [4,5,6], [7,8,9]]
b = [[9,8,7], [6,5,4], [3,2,1]]
c = [[a[i][j] + b[i][j] for j in range(3)] for i in range(3)]

print(c)