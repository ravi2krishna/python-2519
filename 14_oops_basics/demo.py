# OOPS Basics

# class
class Employee:
    pass 

# object 
emp_obj = Employee()

# Student Real World Entity
class Student:
    # attributes / variables 
    student_name = "ravi"
    student_email = "ravi@gmail.com"
    
    # statement
    print(student_name,student_email)


# function 
def student_fun():
    student_name = "john"
    student_email = "john@gmail.com"
    print(student_name,student_email)
    
# function call
student_fun()

# Student Real World Entity
class Student:
    # attributes / variables 
    student_name = "ravi"
    student_email = "ravi@gmail.com"
    
    # statement
    print(student_name,student_email)
    
    # method
    def info(self):
        print(self.student_name,self.student_email)

student_obj = Student()

# print(student_obj)
# print(student_obj.student_name)
# print(student_obj.student_email)
# student_obj.info() # TypeError: Student.info() takes 0 positional arguments but 1 was given

# NOTE : In OOP There is a default behavior in python that is, 
# python automatically passes the object (student_obj) as the 
# first argument to a method and it's called as "self"
print("="*50)
student_obj.info()

# Recommended Way To Use : Class, Object, Method, Constructor
class Student:
    # attributes / variables 
    student_name = "ravi"
    student_email = "ravi@gmail.com"
    
    def __init__(self,student_name,student_email):
        print(student_name)
        print(student_email)
        
# student_obj = Student() # TypeError: Student.__init__() missing 2 required 
                    # positional arguments: 'student_name' and 'student_email'

john_obj = Student("john","john@gmail.com")
mike_obj = Student("mike","mike@gmail.com")

# Not Recommended Way To Use : Class, Object, Method, Constructor
class Student:
    # attributes / variables 
    student_name = "ravi"
    student_email = "ravi@gmail.com"
    
    def __init__(self,student_name,student_email):
        # return student_name # TypeError: __init__() should return None, not 'str'
        # return student_email
        pass
        
# student_obj = Student() # TypeError: Student.__init__() missing 2 required 
                    # positional arguments: 'student_name' and 'student_email'

john_obj = Student("john","john@gmail.com")
mike_obj = Student("mike","mike@gmail.com")


# Recommended Way To Use : Class, Object, Method, Constructor
class Student:

    # constructor (actual purpose)    
    def __init__(self,student_name,student_email):
        self.student_name = student_name
        self.student_email = student_email
        
    # method to show info
    def info(self):
        print("Student Name: ",self.student_name)
        print("Student Email: ",self.student_email )

john_obj = Student("john","john@gmail.com")
mike_obj = Student("mike","mike@gmail.com")