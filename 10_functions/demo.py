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
def emp_info(emp_name="ravi",emp_email="ravi@gmail.com",emp_location="hyderabad"):
    print(f"Hi {emp_name}, your email is {emp_email} and location is {emp_location}")
    
emp_info()
emp_info("user2","user2@gmail.com")

# With Keyword Argument
def emp_info(emp_name,emp_email,emp_location,emp_country="India"):
    print(f"Hi {emp_name}, your email is {emp_email} and location is {emp_location} in {emp_country}")

emp_info(emp_name="Ravi",emp_location="Hyd",emp_email="ravi@gmail.com")
emp_info(emp_location="Pune",emp_name="John",emp_email="john@gmail.com")


# Arbitrary Positional Argument Based (*args)
def add_two_nums(a,b):
    print(a+b)
    
def add_unknown(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print(f"Sum is : {sum}")    

add_unknown()
add_unknown(1)
add_unknown(1,2,3)
add_unknown(1,2,3,4,5,6,7,8,9)


# Arbitrary Keyword Argument Based (**kwargs)
def profile(**info):
    print(info)

profile()
profile(name="ravi")
profile(id=101,name="ravi",city="hyd")

# transactions
def cred_transactions(**transactions):
    print(transactions)
    total = 0
    for i in transactions:
        total = total + transactions[i]
    print(f"You have done {len(transactions)} transactions and total value of all transactions is {total}")

cred_transactions(jan=1000,feb=2500,mar=6000)

# using both Arbitrary Positional Argument Based (*args) & Arbitrary Keyword Argument Based (**kwargs)
def cred_transactions_new(*transactions,**account):
    print(transactions)
    print(account)
    total = 0
    for i in transactions:
        total = total + i
    print(f"Hi {account['name']} you have done {total} amount of transactions in account {account['account_id']}")

cred_transactions_new(1000,3000,6000,name="Ravi",account_id=30930393388)


# without return
def add(a,b):
    a+b

add(10,20)
print(add(20,30)) # None

# with return
def add(a,b):
    return a+b
add(10,20)
print(add(20,30))

# multiple returns - incorrect 
def math_new(a,b):
    return a+b
    return a*b
    return a/b

print(math_new(10,20))

# multiple returns - correct 
def math_new(a,b,opr):
    if opr == "+":
        return a+b
    elif opr == "*":
        return a*b
    elif opr == "/":
        return a/b
    else:
        return "Invalid Operator"
    print("This will not be reachable")

print(math_new(10,20,"+"))
print(math_new(10,20,"*"))
print(math_new(10,20,"#"))

# function Composition
def add(a,b):
    return(a+b)

def sub(c,d,e):
    return add(c,d)-e

print(sub(3,4,5)) # 2

# local scope of variables
def add():
    # local variables 
    la = 5
    lb = 10
    print(la) # accessing within function
    print(lb) # accessing within function
add()

# outside the function
# print(la) # accessing outside the function

# parameters passed to functions are local variables
def add(la,lb):
    print(la) # accessing within function
    print(lb) # accessing within function
add(10,20)

# outside the function
# print(la) # accessing outside the function
    
# global variable
ga = 30

def add(la,lb):
    print(la)
    print(lb)
    print(ga) # accessing global variable inside function
    
add(1,2)
print(ga) # accessing global variable outside function

# name conflict 
ga = 30

def add(la,lb,ga):
    print(la) # 1
    print(lb) # 2
    print(ga) # 3
    print(globals()['ga']) # 30

add(1,2,3)

# trying to change global variable 
count = 0
def increment():
    global count
    count += 1
increment()
print("Count: ",count)

# Without Lambda Function 
def add(a,b):
    return a+b

print(add(3,4))

# With Lambda Function 
# lambda arguments: expression
sum = lambda a,b: a+b
print(sum(5,10))

# IILE
print((lambda a,b: a+b) (1,2))
print((lambda a,b: a+b) (10,20))
print((lambda a,b: a+b) (100,200))

# Regular Function 
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(10))
print(is_even(11))


# Lambda Style
is_even = lambda num: num % 2 == 0
print(is_even(10))
print(is_even(11))

print((lambda num: num % 2 == 0) (10))
print((lambda num: num % 2 == 0) (11))

print(dir(__builtins__))