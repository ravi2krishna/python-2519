# Strings
s1 = "data"
s2 = 'data'
s3 = '''data'''
s4 = """data"""

print(s1)
print(s2)
print(s3)
print(s4)

print(type(s1))
print(type(s2))
print(type(s3))
print(type(s4))

# Multi Line Strings 
# mls = "this is a very
# big line of string
# more lines
# more line"
# print(mls)

mls = '''this is a very
big line of string
more lines
more line'''
print(mls)

# ' inside a string
question = "how are you ?"
# answer = 'i'm fine' # SyntaxError: unterminated string literal (detected at line 32)
answer = "i'm fine"
print(answer)

# answer = "doing "great"" # SyntaxError: invalid syntax
answer = 'doing "great"'
print(answer)

# If you want to use both ' and " quote, then use triple single or double quotes
answer = '''i'm fine doing "great"'''
print(answer)
answer = """i'm fine doing "great" """
print(answer)

# Indexing : Accessing characters 
text = "python"
print(text)
print(text[0]) # positive index
print(text[3]) # positive index
print(text[-1]) # negative index
print(text[-2]) # negative index

# print(text[10]) # IndexError: string index out of range
# print(text[-10]) # IndexError: string index out of range

# string accessing
text = "python"
print("Manually")
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

# using loops to access
print("Using Loops")
for character in text:
    print(character)

# len() -> Return the number of items in a object
text = "python " # space is also a character
print("Length is ", len(text))
text = "python"
print("Length is ", len(text))

# example using list 
list_data = ["dell","lenovo","mac","acer"]
print("Brands Count is ", len(list_data))

# len() -> doesn't work with numbers 
# num = 100
# print(dir(num))
# print("Length is ", len(num)) # TypeError: object of type 'int' has no len()

# Slicing In Python
text = "python"
print(text[0]) # access using index

# [start:stop:step]
print(text[0:3]) # start : stop

print(text[0:]) # start : end
print(text[:]) # start : end

print(text[2:5]) # start : stop --> tho

print(text[:4]) # start(0) : stop(4) --> pyth


text = "python"
print(text[-1])

    #     0   1   2   3   4   5 (positive indexing)
    #     p   y   t   h   o   n
    #    -6   5   4   3   -2   -1 (negative indexing)
print(text[-1:])
print(text[-4:-1]) # tho
print(text[-4:-1:1]) # tho

print(text[-4:-1:-1]) # empty 
print(text[-4:-6:-1]) # ty

print(text[1:4:-1]) # empty

# Reversing string with slicing
print(text[::-1]) # nohtyp  
 
text = "python"
reversed_text = ""

# Reversing string with logic
for char in text:
    reversed_text = char + reversed_text # adding each character to front  yp
print("Reversed Text", reversed_text)


# Reassigning 
text = "hello"
print(text)

text = "hi"
print(text)

# String Immutability
text = "hello"
print(text)

# modify hello to Hello
# text[0] = "H"
# print(text) # TypeError: 'str' object does not support item assignment

# String Concatenation
s1 = "Hello"
s2 = "Good Morning"
print(s1+s2)

# String Formatting
age = 30
# print("My Age is " +age) # TypeError: can only concatenate str (not "int") to str
print(f"My Age is {age}")
print("My Age is ", age)
print("My Age is ", +age)
print("My Age is " +str(age))


# String Repetition
text = "Ha"
laugh = "HaHaHaHa"
print(laugh)

laugh_hard = text * 10
print(laugh_hard)

# String Methods
text = "Ha"
# print(dir(text))

# simulate gmail functionality using strings -> gmail.com
user_given_email = input("Enter Your Email ID: ")
format_email = user_given_email.lower() + "@gmail.com"
print("User Given ID: "+user_given_email)
print("Gmail Auto Format ID: "+format_email)

# simulate PAN correction -> https://www.pan.utiitsl.com/panonline_ipg/forms/csfPan.html/csfPreForm
user_given_pan = input("Enter Your PAN ID: ")

if user_given_pan.isalnum():
    format_pan = user_given_pan.upper()
    print("User Given PAN: "+user_given_pan)
    print("PAN Auto Format ID: "+format_pan)
else:
    print("User Given PAN is INVALID: "+user_given_pan)    

# check for sub string 
# simulate email id verification -> name@gmail.com
user_given_email = input("Enter Your Email ID: ")
if user_given_email.find("@") != -1:
    print("Valid Email")
else:
    print("InValid Email")
    
# above can be achieved using operator also 
user_given_email = input("Enter Your Email ID: ")
if "@" in user_given_email:
    print("Valid Email")
else:
    print("InValid Email")
    
# redirect call based on given isd code
# https://us1.discourse-cdn.com/flex016/uploads/weweb/original/2X/d/dbe25afb4aeb05640347e2f7c1b7ae532ebb28f2.png
phone_number = input("Enter Your Phone Number with ISD CODE: ")
if phone_number.startswith("+91"):
    print("Call Connected To INDIA")
elif phone_number.startswith("+86"):
    print("Call Connected To CHINA")
elif phone_number.startswith("+33"):
    print("Call Connected To FRANCE")
else:
    print("ISD Available Only To INDIA, CHINA & FRANCE")

# Check if email synchronization is possible or not
source_email = input("Enter Your Source Email ID: ")
dest_email = input("Enter Your Destination Email ID To SYNC: ")
if source_email.endswith("@gmail.com") and dest_email.endswith("@gmail.com"):
    print("synchronizing")
else:
    print("Both Emails should be from same providers")

# simulate gmail functionality -> remove spaces from input
user_given_email = input("Enter Your Email ID: ")
format_email = user_given_email.strip()
print("User Given ID: "+user_given_email)
print("Gmail Auto Format ID: "+format_email)

# Read Data From CSV File

# sample data taken from a CSV file
# "Name,City,Age,Email,Role"
csv_line = "John,Hyd,20,john@gmail.com,developer"

# Original Data
print("Original Line: ",csv_line)

parsed_fields = csv_line.split(",")

# Parsed Data
print("Parsed Data: ",parsed_fields)

# Access Name & Role 
print("Name: ",parsed_fields[0])
print("Role: ",parsed_fields[4])

# VS Code Find & Replace / OTP template / Order ID Template
email_template = "Hello User, your order #{order_id} has been shipped"

order_id = "OD-ID-9090"

# Replacing placeholder with values
personalized_email = email_template.replace("{order_id}",order_id)

# sending email
print(personalized_email)
