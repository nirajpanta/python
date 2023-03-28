#Change the String  Eg-"Hello World" "hELLO wORLD" 
#Method1
# string = "Hello World"
# new_string = ""
# for char in string:
#     if char.islower():
#         new_string += char.upper()
#     else:
#         new_string += char.lower()

# print(new_string)


#Method2
# s = "Hello World"
# s = s.swapcase()
# print(s)



#First Letter Lower case * Rest of the letter Upper Case
#Method1
# s = "HEllo World"
# s = s[0].lower() + s[1:].upper()
# print(s)

#Method2
# a = "HELLO World"
# test = a.split(' ')
# temp_list = []
# for i in test:
#     i = i[0].lower() + i[1:].upper()
#     temp_list.append(i)

# a = ' '.join(temp_list)
# print(a) 



#Dictionary
# car = {
#     "name" :"Mustang",
#     "Brand":"Ford",
#     "Color":"Red",
#     'Year' :2018,
#     "Mi leage": 20
# }

# print(car['name'])

# for key, value in car.items():
#     print(key,value)

# for key, value in car.items():
#     print(key)

# for key, value in car.items():
#     print(value)

#for adding item to dictionary 
# car.update({'type':'Electric'})
# print (car)
# print("-------------------------------------------------------------------------------")
# #car.popitem()
# car.clear()
# print(car)
# print("-------------------------------------------------------------------------------")

#copy dictionary
# car_1 = car.copy()
# car_1 = dict(car)
# car['color'] = 'White'
# print(car_1)


# some_dictionary = {
#     'child_1':{
#     'name':'xyz',
#     'age':21
#     },
#     'child_2':{
#     'name':'abc',
#     'age':20
#     },
#     'child_3':{
#     'name':'asd',
#     'age':23
#     }
# }

# print(some_dictionary['child_1']['name'])


#Suppose in a Election 4 candidate (A,B,C,D) increment their vote count and sort them according to their vote count 
# Initialize vote counts for each candidate
votes = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0
}

# Increment vote count for each candidate
votes["A"] += 10
votes["B"] += 20
votes["C"] += 5
votes["D"] += 15

# Sort candidates by vote count in descending order
sorted_candidates = sorted(votes.items(), key=lambda x: x[1], reverse=True)

# Print results
for candidate, vote_count in sorted_candidates:
    print(f"{candidate}: {vote_count}")

