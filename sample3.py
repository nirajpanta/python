#smallest no. from the list
# a = [2,4,5,4]

# smallest = a[0] 

# for i in a:
# 	if i<smallest:
# 		smallest=i

# print("Smallest element is:",smallest)



#sum of even and odd from list
# s_list = [1,2,3,4,5]
# sum_o = 0
# sum_e = 0

# for i in s_list:
#     if(i%2 == 0):
#         sum_e += i
#     else:
#         sum_o += i

# print(f"sum of even numbers:  {sum_e}")
# print(f"sum of odd numbers:  {sum_o}")



#Insert Data to the list
# some_list = [1,2,3,4,5]

# some_list.append(6)
# print(some_list)

# some_list.insert(2,7)
# print(some_list)



#python code to insert even and odd number in even and odd index from 1 to 50
#method1
# my_list = []

# for num in range(0, 50):
#     if num % 2 == 0:
#         my_list.insert(len(my_list) // 2 * 2 + 1, num)
#     else:
#         my_list.insert(len(my_list) // 2 * 2, num)

# print("Final list:", my_list)


# #method2
# e_list = []

# for i in range(0,51):
#     if(i%2 == 0):
#         e_list.append(i+1)
#     else:
#         e_list.append(i-1)

# print(e_list)


#Removing elements from list
#list remove('A')
#s_list pop()
#s_list pop(4)
#del s_list[2]
#del s_list
#clear s_list


# s_list = ['A','B','C','D','E']

# print(s_list)
# s_list.remove('D')
# print(s_list)
# print(s_list.pop())
# print(s_list.pop(1))
# del s_list[0]
# print(s_list)
# s_list.clear()
# print(s_list)

# #sort the list
# s_list = [2,4,1,3,7,6,0]
# s_list.sort(reverse=True)
# print(s_list)

#sort the list[10,5,2,25,40,0,77,1] without using sort function