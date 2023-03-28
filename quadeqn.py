import math
# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))
# c = int(input("Enter value of c: "))

# x = (-b + math.sqrt(b*b - 4*a*c))/2*a
# print("Quadratic Equation: "+str((a*x*x)+(b*x)+c))

a = 1
b = -2
c = -15

eqn = b**2-(4*a*c)
if(eqn<0):
    print("Imaginary Roots")
else:
    eqn2 = (-b+(math.sqrt(eqn)))/2*a
    eqn2 = (-b-(math.sqrt(eqn)))/2*a

print(f"Roots: {eqn2: .2f},{eqn3:.2f}")
