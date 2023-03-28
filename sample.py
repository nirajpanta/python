#Palindrome
# num = int(input("Enter num: "))
# temp = num
# rev = 0
# while(num>0):
#     r = num%10
#     rev = rev*10 + r
#     num = num//10

# if(temp == rev):
#     print("Palindrome")
# else:
#     print("Non palindrome")

# print(f"Reverse of a number: {rev}")

   

#Reverse a number
# num = int(input("Enter num: "))
# rev = 0
# while(num>0):
#     r = num%10
#     rev = rev*10 + r
#     num = num//10


# print(f"Reverse of a number: {rev}")


#Sum of numbers until zero or negative number is entered
a = int(input("Enter num a: "))
b = int(input("Enter num b: "))
sum = a+b
while(a>0 and b>0):
    a = int(input("Enter Number1: "))
    b = int(input("Enter Number2: "))
    sum += (a+b)

print(f"Sum of number = {sum}")
