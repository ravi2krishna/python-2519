# Conditional Statements
# if syntax
# if condition:
#      statements
if True:
    print("Correct Indentation")
    print("correct")  

if 5 < 2:
    print("Valid Condition")  
    
# if else
if 5 < 2:
    print("Valid Condition") 
else:
    print("InValid Condition")  

# voting app
age = 21
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")   

# input() -> for taking input from user
value = input("Enter Some Value: ")
print(value)
print(type(value))

# dynamic voting app
age = int(input("Enter Age: "))
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")   
    
# ternary operator : 
# value_if_true if condition else value_if_false
# dynamic voting app
age = int(input("Enter Age: "))
status = "You can vote" if age >= 18 else "You cannot vote"
print(status)

# elif ladder - multiple conditions
marks = int(input("Enter Your Marks: "))
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
elif marks >= 35:
    print("E")
else:
   print("Fail") 
   
# match-case (switch case in java) 
# this is introduced in python 3.1 onwards
choice = int(input("Enter Your Choice (1-5): "))
match choice:
    case 1:
        print("Python")
    case 2:
        print("Java")
    case 3:
        print("C#")
    case 4:
        print("Cloud")
    case 5:
        print("DevOps")
    case _:
        print("Select Only Valid Choice (1-5)")
    
# elif ladder style
age = 25

if age == 0 or age == 1 or age == 2 or age == 3 or age == 4:
   category = "Toddler"
elif age == 5 or age == 6 or age == 7 or age == 8 or age == 9 or age == 10 or age == 11 or age == 12:
   category = "Child"
elif age == 13 or age == 14 or age == 15 or age == 16 or age == 17 or age == 18 or age == 19:
   category = "Teenager"
elif age == 20 or age == 21 or age == 22 or age == 23 or age == 24 or age == 25 or age == 26:
   category = "Young Adult"
else:
   category = "Adult"

print(category) 
   
# match case style
age = 25

match age:
   case 0 | 1 | 2 | 3 | 4:
       category = "Toddler"
   case 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
       category = "Child"
   case 13 | 14 | 15 | 16 | 17 | 18 | 19:
       category = "Teenager"
   case 20 | 21 | 22 | 23 | 24 | 25 | 26:
       category = "Young Adult"
   case _:
       category = "Adult"

print(category)
