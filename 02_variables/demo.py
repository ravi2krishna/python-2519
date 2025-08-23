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