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