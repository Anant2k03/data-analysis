print("line 1 ")
print("line 2 ")
print("line 3 ")
print("line 4 ")
num1 = int (input("enter the first num"))

num2 = int (input("enter the second num"))

try:
    print(num1/num2)
    print("inside a try ")

except ZeroDivisionError as e :
    print("inside a except ZeroDivisionError ",e)