#program to print a natural nos. find odd even,sum
a=int(input("enter the value of a"))
print("Natural numbers are: ")
sum=0;
for i in range(1,a+1):
    print(i)
print("sum is: ")
for i in range(1,a+1):
    sum+=i
print(sum)
for i in range(1,a+1):
    if(i%2==0):
        print(i,"is even")
    else:

        print(i,"is odd")
