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

# membership operators
a_list = [10,20,30]
is_present = 10 in a_list
print(is_present)
is_present = 100 in a_list
print(is_present)
is_present = 100 not in a_list
print(is_present)

data = "hello"
is_present = "a" in data
print(is_present)

n1 = 10
n2 = 10
print(id(n1))
print(id(n2))
print(n1 is n2)
print(n1 == n2)

n1 = [10,20,30]
n2 = [10,20,30]
print(id(n1))
print(id(n2))
print(n1 is n2)
print(n1 == n2)

print(n1 is not n2)

# Data Types 
num = 10 # int 
print(type(num))
      
num = 10.0 # float 
print(type(num))

num = 1 + 2j # complex
print(type(num))

data = "hello" # string
print(type(data))

data = "h" # string
print(type(data))

canVote = True
print(type(canVote))

list_nums = [10,20,30,10]
list_colors = ["blue","red","green"]
print(type(list_nums))
print(type(list_colors))
print(list_nums)

list_nums = (10,20,30,10)
print(type(list_nums))
print(list_nums)

list_nums = {10,20,30,10}
print(type(list_nums))
print(list_nums)

list_nums = {"n1":10,"n2":20,"n3":30}
print(type(list_nums))
print(list_nums)

x = None
print(type(x))
print(x)

class Student: # class
    pass # skip - do nothing 

edify_student = Student() # object
print(type(edify_student))


# Student Management System
student_id = 101
student_name = "John"
student_age = 20

# Scores
quiz_score = 80
assignment_score = 75
exam_score = 90

# attendance
student_attendance = 90

# calculations
total_score = quiz_score + assignment_score + exam_score
avg_score = total_score/3

student_passed = avg_score > 75

# increment attendance
# student_attendance = student_attendance + 1 # long hand
student_attendance += 1 # short hand

# award eligibility
award_eligibility = student_attendance >= 90 and student_passed

# Process output
print("======= Student Report =======")
print(f"Student Name: {student_name}")
print(f"Student Total Score: {total_score}")
print(f"Student Average Score: {avg_score}")
print(f"Student Current Attendance: {student_attendance}")
print(f"Student Passed: {student_passed}")
print(f"Student Awarded: {award_eligibility}")

# Type Conversion -> Automatic / Implicit
a = 10
b = 3.5
c = a + b # 13.5
print(c)
print(type(c))

# Type Casting -> Manual / Explicit
x = 100
y = x
print(y)
print(type(y)) 
# explicit conversion
y = float(x)
print(y)
print(type(y))

# Data loss can occur
r = 3.14
value = int(r)
print(value)

# strings
value = "100"
print(type(value))
value_int = int(value)
print(value_int/10)
# print(value/10) # TypeError: unsupported operand type(s) for /: 'str' and 'int'

value = "hundred"
# value_int = int(value) # ValueError: invalid literal for int() with base 10: 'hundred'
