#py code to print 2D list with input

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
