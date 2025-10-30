#py code to print largest & smallest element

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

l = arr[0][0]
s = arr[0][0]

for e in arr:
    for i in e:
        if i > l:
            l = i
        elif i < s:
            s = i

print(f"Smallest element: {s}")
print(f"Largest element: {l}")
