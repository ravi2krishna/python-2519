# Functional Based Programming 

# without functions (code repetition)
a = 10
b = 12

# math operations 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 14 
b = 15

# math operations 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 225 
b = 325

# math operations 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# with functions
a = 200 
b = 300

def math_ops():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# call function
math_ops()

a = 2000 
b = 3000

# call function
math_ops()

a = 20 
b = 30

# call function
math_ops()

# functions with parameters --> a & b are parameters
def math_ops(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# call function
# math_ops() # TypeError: math_ops() missing 2 required positional arguments: 'a' and 'b'
math_ops(100,200) # --> 100 & 200 are arguments
math_ops(150,250) 
math_ops(300,550) 

# Positional Based 
def login(username,password):
    if username == "ravi" and password == "1234":
        print("Login Success")
    else:
        print("Login Failed")

# call login function
login("ravi","1234") 
login("ravi","7890")    
login("1234","ravi")    
    
# Without Default Argument --> means we are using positional based
def emp_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and location is {emp_location}")
    
emp_info("hyderabad","ravi","ravi@gmail.com")

# With Default Argument
def emp_info(emp_name="ravi",emp_email="ravi@gmail.com",emp_location="hyderabad",):
    print(f"Hi {emp_name}, your email is {emp_email} and location is {emp_location}")
    
emp_info()
emp_info("user2","user2@gmail.com")