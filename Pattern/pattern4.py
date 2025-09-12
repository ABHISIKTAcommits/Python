#Enter the number of rows: 4
#      1 
#    2 1 
#  3 2 1 
#4 3 2 1 

n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    print("  " * (n - i), end="") 
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
