# User Defined Module
name = "john"
email = "john@gmail.com"

def add(a,b):
    return a+b

def prod(a,b):
    return a*b

def profile(name,email):
    return f"Hi {name}, your registered email is {email}"

def info(name=name,email=email):
    return f"Hi {name}, your registered email is {email}"