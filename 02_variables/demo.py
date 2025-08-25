# Working Variables
# syntax --> var_name = value
# Syntax for text data is to enclose the text inside ' ' or " "
student_name = "Ravi"
student_age = 20
student_gpa = 9.5
student_passed = True 

dynamic_variable = 10
print(type(dynamic_variable))

dynamic_variable = 9.5
print(type(dynamic_variable))

dynamic_variable = False
print(type(dynamic_variable))

dynamic_variable = "Hello"
print(type(dynamic_variable))

a = 10
print(id(a))

b = 20
print(id(b))

c = 10
print(id(c))

# List means collection of multiple items -> list is represented using [ ]
a_list = [10,20,30]
print(type(a_list))
print(id(a_list))

c_list = [10,20,30]
print(id(c_list))

x = "Python "
y = "is "
z = "awesome"

# output = Python is awesome
# print(xyz) # NameError: name 'xyz' is not defined

# + (add takes multiple numeric values and add them)
# + when used with numerics it's called as addition operator
# + when used with text it's called as concatenation operator

# What is concatenation ? -> Joining multiple Strings
print(x+y+z) # + as concatenation operator

x = 10
y = 20
z = 30
print(x+y+z) # + as addition operator

a = "10"
b = "10"

# print(x+a) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(a+b)

# Multiple Variables
x,y,z = 10,20,30
# x,y,z = 10,20,30,40 (LHS == RHS) # ValueError: too many values to unpack (expected 3)
print(x+y+z)

s1,s2,s3 = "orange","apple","cherry"
print(s1+s2+s3)

# using concatenation 
name = "ravi"
age = 25
# print("My name is " +name +" and im " +age + "years old")
# TypeError: can only concatenate str (not "int") to str

print("My name is {name}  and im {age} years old") 

# using interpolation
print(f"My name is {name}  and im {age} years old") 

# using different values dynamically
x,y,z = 10,20,30
age = 25
print(f"Sum of x,y,z,age: {x+y+z+age}")

# school student info
student_name = "john"
student_class = 8
student_school = "DPS"
print(f"My name is {student_name} im studying in {student_class} class in {student_school} school")

# Operators 

# Arithmetic Operators
n1 = 3
n2 = 2
print(f"Sum of n1 and n2 is: {n1+n2}")
print(f"Difference of n1 and n2 is: {n1-n2}")
print(f"Product of n1 and n2 is: {n1*n2}")
print(f"Division of n1 and n2 is: {n1/n2}")
print(f"Modulus of n1 and n2 is: {n1%n2}")
print(f"floor division of n1 and n2 is: {n1//n2}")
print(f"exponentiation of n1 and n2 is: {n1**n2}")

# without Compound Assignment Operators
x = 10
x = x + 5
print(x)

# with Compound Assignment Operators
x = 10
x += 5 # x = x + 5
print(x)

x = 10
x *= 5 # x = x * 5
print(x)

# Comparison Operators    
n1 = 3
n2 = 2
n3 = 3
print(n1 == n2)
print(n1 == n3)
print(n1 >= n2)
print(n1 != n2)

# Logical Operators
x = 7
y = 5
a = 15
b = 9

resultand = x > y and a < b # T and F -> F
print(resultand)

resultor = x > y or a < b # T or F -> T
print(resultor)

resultnot = x > y or a < b # T or F -> T
print(not resultnot)