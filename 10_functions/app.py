# Student/Product/Employee Management System

# System Setup (Fixed) Using Tuples
SYSTEM_INFO = ("Edify Student Management Portal","v1","2025","Edify University")
ADMIN_INFO = ("admin@edify.com","9808080","Room 201")

# Display System Info At Startup => display_system_info()
def display_system_info():
    print("="*50)
    print(f"    Welcome To {SYSTEM_INFO[0]}")
    print(f"    Developed By Students at {SYSTEM_INFO[3]}")
    print("="*50)

# Students Info is Dictionary 
students = {}

# add_student()
def add_student():
        student_id = input("Enter ID: ")
        if student_id in students:
            print("ID Already exists")
        else:
            name = input("Enter Name: ").title()
            scores = []
            while True:
                score_input = input("Enter Score or type done: ")
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0<= score <=100:
                        scores.append(score)
                    else:
                        print("Scores should be in range (0-100)")
                else:
                    print("Scores can be numbers only")
            
            skills = set()
            while True:
                skill_input = input("Enter Skill or type done: ")
                if skill_input == "done":
                    break
                skills.add(skill_input.title())
            
            # save student details 
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            print("Student Added")
            
            # for confirmation
            print(students)

# update_student()
def update_student():
        student_id = input("Enter ID To Update: ")
        if student_id in students:
            new_name = input("Enter New Name: ").title()
            students[student_id]["name"] = new_name
            print("Name Updated")
        else:
            print("ID Doesn't exists")
        
        # for confirmation
        print(students)

# delete_student()
def delete_student():
        student_id = input("Enter ID To Delete: ")
        if student_id in students:
            remove = students.pop(student_id)
            print(remove)
        else:
            print("ID Doesn't exists")
    
        # for confirmation
        print(students)

# read_student()
def read_student():
        if not students:
            print("No Students Available")
        else:
            print("Student Details")
            
            for sid, data in students.items():
                name = data["name"]
                scores = data["scores"]
                
                avg = sum(scores)/len(scores)
                high_score = max(scores)
                
                skills = data["skills"]
                skills_count = len(skills)
                
                print("========= DETAILS =========")
                print(f"ID: {sid}")
                print(f"Name: {name}")
                print(f"All Scores: {scores}")
                print(f"Average Score: {avg}")
                print(f"Highest Score: {high_score}")
                print(f"All Skills: {skills}")
                print(f"Count Of Skills: {skills_count}")
                
# search_student()
def search_student():
    skill_to_search = input("Enter Skill To Search: ").title()
    matched_students = list(filter(lambda s: skill_to_search in students[s]['skills'], students))
    print(matched_students)
    if matched_students:
        print(f"Students With Skills {skill_to_search} :")
        for sid in matched_students:
            print(f"ID: {sid}   |   Name: {students[sid]['name']}")
    else:
        print(f"No students found with skill {skill_to_search}")
        
# exit_app()
def exit_app():
         print("="*50)
         print(f"ADMIN CONTACT DETAILS")
         print("="*50)
         print(f"ADMIN PHONE: {ADMIN_INFO[1]}")
         print(f"ADMIN EMAIL: {ADMIN_INFO[0]}")    


# Application Startup
display_system_info()

# Build Menu System 
while True:
    print("Choose an option below: ")
    print("1 - Add Student")
    print("2 - Modify Student")
    print("3 - Delete Student")
    print("4 - List Student")
    print("5 - Search Student By Skill")
    print("6 - Exist System")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
        add_student()               
    elif choice == "2":
        update_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        read_student() 
    elif choice == "5":
         search_student()        
    elif choice == "6":
         exit_app()
         break
    else:
        print("Invalid Option, Select only (1-5): ") 