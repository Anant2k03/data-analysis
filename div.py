print("the numbers which are even and divisible by 3 and also lies between 100 and 1000 are :")
#for x in range(100,1000):
    #if(x%2 == 0 and x%3==0):
       # print(x)


x = 100
while(x<1000):
    if (x % 2 == 0 and x %  3 == 0):
        print(x , end = ",")
    x=x+1
