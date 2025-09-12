# Enhanced Student Grade & FEE Tracker
# Identifiers - Variables - Operators - Control Statements - Strings

print("="*50)
print("     Enhanced Student Grade & FEE Tracker")
print("="*50)

# Student ID
student_id_valid = False
while not student_id_valid:
    student_id = input("Enter Your ID: ")
    # check for negative numbers (-10) (-digit) (-101)
    if student_id.startswith("-") and student_id[1:].isdigit():
        print("Please Enter Positive Number For ID")
    # check for digits only above 0
    elif student_id.isdigit():
        student_id = int(student_id)
        if student_id > 0:
            student_id_valid = True
        else:
            print("Please Enter Non-Zero Value For ID")  
    else:
        print("Enter Numbers Only As ID")      

# format ID as EDIFY-ID
formatted_id = "EDIFY" + str(student_id)
print(formatted_id)