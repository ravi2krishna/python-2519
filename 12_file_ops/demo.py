# File Management Using Python 

# we have a file => file.txt 

# result = open("file_new.txt","r") # FileNotFoundError: [Errno 2] No such file or directory: 'file_new.txt'
# 1st Approach -> file is not automatically closed after operations
file = open("file.txt","r")
print(file)
print(file.closed)
file.close()
print(file.closed)

# 2nd Approach (recommended) -> file is automatically closed after operations
with open ("file.txt","r") as file_data:
    print(file_data)
print(file_data.closed)

# Reading Entire Content -> read() 
with open ("file.txt","r") as file_data:
    print(file_data.read())

# Reading Character by Character -> read()
with open ("file.txt","r") as file_data:
    for char in file_data.read():
        print(char)
        
# Reading Word by Word -> read()
with open ("file.txt","r") as file_data:
    words = file_data.read().split()
    for word in words:
        print(word)
        
# Reading Line -> readline()
with open ("file.txt","r") as file_data:
    print(file_data.readline()) # 1st line
    print(file_data.readline()) # 2nd line
    
# Reading All Lines -> readlines()
with open ("file.txt","r") as file_data:
    print(file_data.readlines()) # All Lines
    
# Reading All Lines -> readlines()
with open ("file.txt","r") as file_data:
    data = file_data.readlines()
    for line in data:
        print(line)

# Reading All Lines -> readlines()
with open ("file.txt","r") as file_data:
    data = file_data.readlines()
    for line in data:
        print(line.strip())

# Write Mode -> Create file
with open ("write.txt","w") as file_data:
    print(file_data)
    
# Write Mode -> Write/Update Content 
with open ("write.txt","w") as file_data:
    file_data.write("Hello")

# Write Mode -> Write/Update Content --> It Overwrites 
with open ("write.txt","w") as file_data:
    file_data.write("World")

# Write Mode -> Write/Update Content --> It Overwrites 
with open ("write.txt","w") as file_data:
    file_data.write("Hello \n")
    file_data.write("World")
    
# Write Mode -> Write/Update Content --> It Overwrites 
with open ("write.txt","w") as file_data:
    file_data.writelines(["this is first line \n", "this is second line \n"])
    
# Append Mode -> Appending Data, same as write but keeps previous data then write new data 
with open ("write.txt","a") as file_data:
    file_data.writelines(["this is third line \n", "this is fourth line"])
    
# Delete File 
import os
os.remove('write.txt')

# Directory Creation 
# os.mkdir("mydir") 

# Empty Directory Deletion
# os.rmdir("new")

# Non-Empty Directory Deletion
import shutil
shutil.rmtree("mydir") 