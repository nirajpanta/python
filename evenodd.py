a = int(input("Enter your  number: "))
if( a / 2 == 0):
    print("Even")

if( a / 2 != 0):
    print("odd")

#find positive and negative number
z = int(input("Enter value of z: "))
if(z > 0):
    print("Its Positive")
elif(z < 0):
    print("Its Negative")
else:
    print("zero")
    
import math
#Area of triangle 
a = int(input("Enter value of side1: "))
b = int(input("Enter value of side2: "))
c = int(input("Enter value of side3: "))

s = (a+b+c)/3
print("Area of triangle: "+str(math.sqrt(s*(s-a)*(s-b)*(s-c))))
