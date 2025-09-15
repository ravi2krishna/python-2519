# Lists In Python

# empty list 
empty_list = []
print(type(empty_list))
print(empty_list)

# store data in list
num_list = [10,20,30,40,50]
print(num_list)

string_list = ["python","django","scripting"]
print(string_list)

mixed_list = [10,20,30,"python","django",2.5,True] # heterogenous 
print(mixed_list)

num_list = list([10,20,30,40,50])
print(num_list)

num_list = [10]
print(num_list)

# num_list = list(10) # no __iter__
# print(num_list)

num_list = list([10]) # __iter__ -> use dir(num_list)
print(num_list)

# Accessing Data in lists

# indexing
num_list = [10,20,30,40,50]
print(num_list[0])
print(num_list[2])
print(num_list[-1])

# slicing
print(num_list[:]) # start to end
print(num_list[::]) # start to end
print(num_list[1:3:]) # [20,30]
print(num_list[::2]) # [10,30,50]

print(num_list[::-1]) # [50, 40, 30, 20, 10]

# Memory 
num1 = 10
num2 = 10
print(id(num1))
print(id(num2))

num_list_1 = [10,20,30,40,50]
num_list_2 = [10,20,30,40,50]
print(id(num_list_1))
print(id(num_list_2))

print(id(num_list_1[0]))
print(id(num_list_2[0]))

# Accessing Errors
num_list = [10,20,30,40,50]
print(num_list[0])
# print(num_list[10]) # IndexError: list index out of range

num = 10
num *= 5
print(num)

# print each element 
num_list = [10,20,30,40,50]
for num in num_list:
    print(num)
    
# do some action on each element 
num_list = [10,20,30,40,50]
for num in num_list:
    print(num*5)
    
# using range to work list 
num_list = list(range(0,26,5))
print(num_list)

# perform conditional logics
days = ["sun","mon","tue","wed","thus","fri","sat"]
day = input("Enter day name in week: ") # sun, mon etc
if day in days:
    print("Exists")
else:
    print("Does not Exists")

# list methods
list = [10]
print(dir(list))