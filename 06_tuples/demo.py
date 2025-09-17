# Tuples in python

# empty tuple 
empty_tuple = ()
print(type(empty_tuple))
print(empty_tuple)

# store data in tuple
num_tuple = (10,20,30,40,50)
print(num_tuple)

string_tuple = ("python","django","scripting")
print(string_tuple)

mixed_tuple = (10,20,30,"python","django",2.5,True) # heterogenous 
print(mixed_tuple)

num_tuple = tuple((10,20,30,40,50))
print(num_tuple)

num_tuple = (10)
print(num_tuple)

# num_tuple = tuple(10) # no __iter__
# print(num_tuple)

# indexing
num_tuple = (10,20,30,40,50)
print(num_tuple[0])
print(num_tuple[2])
print(num_tuple[-1])

# slicing
print(num_tuple[:]) # start to end
print(num_tuple[::]) # start to end
print(num_tuple[1:3:]) # [20,30]
print(num_tuple[::2]) # [10,30,50]

print(num_tuple[::-1]) # [50, 40, 30, 20, 10]

# Memory 
num1 = 10
num2 = 10
print(id(num1))
print(id(num2))

num_tuple_1 = (10,20,30,40,50)
num_tuple_2 = (10,20,30,40,50)
print(id(num_tuple_1))
print(id(num_tuple_2))

print(id(num_tuple_1[0]))
print(id(num_tuple_2[0]))

# Accessing Errors
num_tuple = (10,20,30,40,50)
print(num_tuple[0])
# print(num_tuple[10]) # IndexError: tuple index out of range

num = 10
num *= 5
print(num)

# print each element 
num_tuple = (10,20,30,40,50)
for num in num_tuple:
    print(num)
    
# do some action on each element 
num_tuple = (10,20,30,40,50)
for num in num_tuple:
    print(num*5)
    
# using range to work tuple 
num_tuple = tuple(range(0,26,5))
print(num_tuple)

# perform conditional logics
days = ("sun","mon","tue","wed","thus","fri","sat")
day = input("Enter day name in week: ") # sun, mon etc
if day in days:
    print("Exists")
else:
    print("Does not Exists")

# duplicates inside tuple
t = (10,20,30,40,50,50,40,20)
print(t)

print(dir(t))