# Working with CSV Files

import csv

with open("12_file_ops/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        print(row)
        
print("="*50)  
  
# Fetch me customers of Hyderabad 
with open("12_file_ops/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # Fetch customers of Hyderabad
        # print(row[3])
        if row[3] == "hyderabad":
            print(row)

print("="*50)  
  
# Fetch me customers of google
with open("12_file_ops/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # Fetch customers of gmail accounts
        # print(row[1])
        if row[1].endswith("@gmail.com"):
            print(row)
   
print("="*50)  
         
# Using DictReader 
with open("12_file_ops/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        print(row)
    
print("="*50)  

# Fetch me customers of yahoo
with open("12_file_ops/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        if row['email'].endswith("@yahoo.com"):
            print(row)

print("="*50)  

# Fetch me customers whose name is ravi
find_customer = "ravi"
with open("12_file_ops/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        if row["name"] == find_customer:
            print(row)
   
# Writing Data 
with open("12_file_ops/employees.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'email', 'mobile', 'address'])
    csv_writer.writerow(['ravi', 'ravi@gmail.com', '998998998', 'hyderabad'])
    csv_writer.writerow(['krishna', 'krishna@gmail.com', '998998998', 'hyderabad'])
    csv_writer.writerows([['ramu', 'ramu@outlook.com', '998998998', 'bangalore'],
['suresh', 'suresh@gmail.com', '998998998', 'pune'],
['mahesh', 'mahesh@yahoo.com', '998998998', 'chennai']])
            
# Appending Data 
with open("12_file_ops/employees.csv","a") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'email', 'mobile', 'address'])
    csv_writer.writerow(['ravi', 'ravi@gmail.com', '998998998', 'hyderabad'])
    csv_writer.writerow(['krishna', 'krishna@gmail.com', '998998998', 'hyderabad'])
    csv_writer.writerows([['ramu', 'ramu@outlook.com', '998998998', 'bangalore'],
['suresh', 'suresh@gmail.com', '998998998', 'pune'],
['mahesh', 'mahesh@yahoo.com', '998998998', 'chennai']])

# DictWriter 
with open("12_file_ops/employees.csv","w") as file_data:
    fieldnames = ['name', 'email', 'mobile','address']
    csv_writer = csv.DictWriter(file_data,fieldnames=fieldnames)
    csv_writer.writeheader()  # Write the header row
    csv_writer.writerow({'name': 'mahesh', 'email': 'mahesh@yahoo.com', 'mobile': '998998998', 'address': 'chennai'})
    
with open("12_file_ops/employees.csv","w") as file_data:
    fieldnames = ['name', 'email', 'mobile','address']
    csv_writer = csv.DictWriter(file_data,fieldnames=fieldnames)
    csv_writer.writeheader()  # Write the header row
    csv_writer.writerows([{'name': 'ravi', 'email': 'ravi@gmail.com', 'mobile': '998998998', 'address': 'hyderabad'},
{'name': 'ramu', 'email': 'ramu@outlook.com', 'mobile': '998998998', 'address': 'bangalore'},
{'name': 'suresh', 'email': 'suresh@gmail.com', 'mobile': '998998998', 'address': 'pune'},
{'name': 'mahesh', 'email': 'mahesh@yahoo.com', 'mobile': '998998998', 'address': 'chennai'},
{'name': 'krishna', 'email': 'krishna@gmail.com', 'mobile': '998998998', 'address': 'hyderabad'}])