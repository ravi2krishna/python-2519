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