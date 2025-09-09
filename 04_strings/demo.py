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


