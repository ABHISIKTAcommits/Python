#enter the number of rows: 3
#1 2 3 
#4 5 6 
#7 8 9 
a=int(input("enter the number of rows: "))
point=1
for i in range(1,a+1):
    for j in range(1,a+1):
        print(point,end=" ")
        point+=1
    print()