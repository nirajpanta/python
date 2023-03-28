# #Built a simple calculator using functions(+,-,*,/)
# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     return x / y

# print("Select Operation: ")
# print("1.Add")
# print("2.substract")
# print("3.Muktiply")
# print("4.Divide")

# while True:
#     choice = input("Enter choice(1/2/3/4): ")

#     if choice in ('1', '2', '3', '4'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue

#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))

#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))

#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))

#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
        
#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#           break
#     else:
#         print("Invalid Input")


# def std_info (name = "xyz", Section = "B"):
#     print(name)
#     print(Section)

# std_info('asd','c')


#Create a function to add 4 numbers
# def sum(a,b,c,d,e,f,g,h,i,j):
#     print(a+b+c+d+e+f+g+h+i+j)

# sum(1,2,3,4,5,6,7,8,9,10)


# def sum(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)

# sum(1,2,3,4,5,6,7,8,9,10)


# def factorial (num):
#     if(num==1 or num == 0):
#         return 1
#     return num*factorial(num-1)

# print(factorial(5))


#lamda function
# x = lambda a:a**3

# print(x(5))
# def cube(num):
#     return num**3


    player_turn = not player_turn
    empty_board = board_empty(board)
else:
    print("\nIt's a tie.\n")







