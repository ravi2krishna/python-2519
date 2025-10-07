# File Management Using Python 

# we have a file => file.txt 

# result = open("file_new.txt","r") # FileNotFoundError: [Errno 2] No such file or directory: 'file_new.txt'
result = open("file.txt","r")
print(result)