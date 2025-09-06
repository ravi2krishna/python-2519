# While 
# syntax
# while condition:
    # code to repeat 

count = 1
while count <=5:
    print(count)
    count += 1
    
# Simulate real world use case for while
atm_correct_pin = 1234
user_given_pin = 0 

while user_given_pin != atm_correct_pin:
    user_given_pin = int(input("Enter PIN: "))

print("You can Withdraw")

# Infinite Loop
# count = 1
# while True:
#     print(count)
#     count += 1

# For loop : Used to Iterate over a Sequence(Multiple)
# syntax
# for elements in Sequence:
    # statements  
text = "python is a general purpose programming language"
for character in text:
    print(character)

# num = 10
# for character in num: # TypeError: 'int' object is not iterable
#     print(character)

# Test to check given object is iterable --> __iter__ 
num = 10
print(type(num))
print(dir(num))

text = "python"
print(type(text))
print(dir(text))

list_nums = [10,20,30]
print(type(list_nums))
print(dir(list_nums))
for num in list_nums:
    print(num)
    
# For loop : Repeat block of code, if you know number of iterations in advance
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")

# range()
for num in range(10):
    print(num)

for num in range(10):
    print("Hi")

for num in range(1,6):
    print(num)

for num in range(1,6,1):
    print(num)

for num in range(2,10,2):
    print(num)

# for num in range(2,10,2,1): # TypeError: range expected at most 3 arguments, got 4
#     print(num)

for num in range(1,10,1):
    print(num)

for num in range(10,1,-1):
    print(num)

for num in range(10,1,-2):
    print(num)

# get even nums
print("printing even nums from 1 to 20")
num = 2
while num <= 20:
    print(num)
    num += 2

# get even nums
# Loop with condition
print("printing even nums from 1 to 20")
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1

# get even nums
print("printing even nums from 1 to 20")
for num in range(2,22,2):
    print(num)

# List of courses
course_list = ["python","cloud","devops","ai"]
for course in course_list:
    print(course)

# Nested Loops
for i in range(1,4):
    for j in range(1,4):
        print(f"{i} X {j} = {i * j}")
    print("---")

# Nested Loops
i = 1
while i < 4:
    j = 1
    while j < 4:
        print(f"{i} X {j} = {i * j}")
        j += 1
    print("---")
    i += 1

# Branching Statements (Jump Statements)

# break : exits the loop entirely
for num in range(5):
    if num == 3:
        break # loop will stop here
    print(num)

# continue : skips the current iteration and continue the loop
for num in range(5):
    if num == 3:
        continue # skip this current iteration
    print(num)

# pass : does nothing, generally used as place holder
if 5 > 9:
    pass
    
# pass : using for future
for num in range(5):
    if num == 3:
        pass # keep future code here
    print(num)