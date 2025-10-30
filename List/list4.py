#py code to print transpose of 2D matrix

arr = []
r = int(input("Enter number of rows: "))
c = int(input("Enter number of cols: "))

print("Enter elements row-wise: ")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input("Element: ")))
    arr.append(a)

print("Given matrix: ")
for row in arr:
    for val in row:
        print(val, end=' ')
    print()

print("TRANSPOSE: ")
for i in range(c):
    for j in range(r):
        print(arr[j][i], end=' ')
    print()
