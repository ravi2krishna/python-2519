# Student/Product/Employee Management System

# System Setup (Fixed) Using Tuples
SYSTEM_INFO = ("Edify Student Management Portal","v1","2025","Edify University")
ADMIN_INFO = ("admin@edify.com","9808080","Room 201")

# Display System Info At Startup
print("="*50)
print(f"    Welcome To {SYSTEM_INFO[0]}")
print(f"    Developed By Students at {SYSTEM_INFO[3]}")
print("="*50)

# Students Info is Dictionary 
students = {}

# Build Menu System 
while True:
    print("Choose an option below: ")
    print("1 - Add Student")
    print("2 - Modify Student")
    print("3 - Delete Student")
    print("4 - List Student")
    print("5 - Exist System")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
        print("Adding Student Logic")
    elif choice == "2":
         print("Modifying Student Logic")
    elif choice == "3":
         print("Deleting Student Logic")    
    elif choice == "4":
         print("Listing Students Logic") 
    elif choice == "5":
         print("Exiting System") 
         break
    else:
        print("Invalid Option, Select only (1-5): ") 