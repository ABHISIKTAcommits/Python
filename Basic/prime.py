#prime check and print
a=int(input("enter the value of a"))
for i in range (2,a+1):
    isp=True
    for j in range (2,i):
        if(i%j==0):
            isp=False
            break
    if(isp):
        print(i)