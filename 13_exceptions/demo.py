# Exception Handling 

# When there are no errors, nothing to handle
print("Program Execution Started")

num1 = 10
num2 = 5

print(num1/num2)

print("Program Execution Ended")

print("="*50)

# When there are errors, see how python handles them -> abruptly stopped execution 
print("Program Execution Started")

num1 = 10
num2 = 0

# print(num1/num2) # ZeroDivisionError: division by zero

print("Program Execution Ended")

print("="*50)

# When there are errors, let's handle the errors by ourself
# -> try : used to keep the code that will cause errors 
# -> except : used to keep the code that should run, when error occurs  

print("Program Execution Started")

num1 = 10
num2 = 0
try:
    print(num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! You cannot divide number by zero - its a math rule")
    print("Check For More Info - https://en.wikipedia.org/wiki/Division_by_zero")
print("Program Execution Ended")

print("="*50)

# When we have multiple errors -> but same generic message 
print("Program Execution Started")
data = [1,2,'python',0,4,5]
# TypeError: unsupported operand type(s) for /: 'int' and 'str'
# ZeroDivisionError: division by zero
# data = [1,2,0,4,5]
for num in data:
    try:
        print(1/num)
    except:
        print("OOPS! Some Problem Occurred") 
print("Program Execution Ended")

print("="*50)

# When we have multiple errors -> giving specific error messages
print("Program Execution Started")
data = [1,2,'python',0,4,5]
# TypeError: unsupported operand type(s) for /: 'int' and 'str'
# ZeroDivisionError: division by zero
# data = [1,2,0,4,5]
for num in data:
    try:
        print(1/num)
    except:
        print("OOPS! Some Problem Occurred") 
    # except:
    #     print("OOPS! Some Problem Occurred") 
print("Program Execution Ended")

print("="*50)

# When we have multiple errors -> giving specific error messages
print("Program Execution Started")
data = [1,2,'python',0,4,5]
# TypeError: unsupported operand type(s) for /: 'int' and 'str'
# ZeroDivisionError: division by zero
# data = [1,2,0,4,5]
for num in data:
    try:
        print(1/num)
    except TypeError:
        print("OOPS! Don't pass Strings, we cannot divide a string and number") 
    except ZeroDivisionError:
        print("OOPS! You cannot divide number by zero - its a math rule")
print("Program Execution Ended")

print("="*50)


# When we have multiple errors -> giving specific error messages
print("Program Execution Started")
num1 = 10
num2 = 0
try:
    print(num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! You cannot divide number by zero - its a math rule")
    print("Check For More Info - https://en.wikipedia.org/wiki/Division_by_zero")
print("Calculation successful")
print("Program Execution Ended")

print("="*50)


# When we have multiple errors -> giving specific error messages
print("Program Execution Started")
num1 = 10
num2 = 0
try:
    print(num1/num2) # username & password correct
except:
    print("OOPS! You cannot divide number by zero - its a math rule")
    print("Check For More Info - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation successful") # prompt for two step verification 
finally:
    print("Program Execution Ended")

print("="*50)

# User Defined Exception
class AgeError(Exception):
    pass

age = int(input("Enter Age: "))

if age < 18:
    raise AgeError("Age Error at least 18 required")
else:
    print("You can vote")
    
# Handle Custom Exception 
class AgeError(Exception):
    pass

age = int(input("Enter Age: "))
try:
    if age < 18:
        raise AgeError
except:
    print("Age Error at least 18 required")
else:
    print("You can vote")