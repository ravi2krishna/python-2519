# Student Grade Tracker

# Collect Student Information
student_id = input("Enter Your ID: ")
student_name = input("Enter Your Name: ")

attendance = int(input("Enter Your Attendance: "))
number_of_subjects = 0
total_score = 0

# using while loop read user input for scores
continue_input = "yes"

# Repeatedly ask the user line 15
while continue_input == "yes" or continue_input == "Yes":
    # type casting
    current_score = int(input(f"Enter Scores For Subject {number_of_subjects+1}: "))
    continue_input = input("Do you want to enter another score (yes/no): ")
    # increment the number of subjects
    number_of_subjects += 1
    # Add each entered score to the total score 
    total_score += current_score

# Calculate Average Score
average_score = total_score / number_of_subjects

# Determine Performance based on Average Score
# conditional 
if average_score >=85:
    performance = "Excellent"
elif average_score >=70:
    performance = "Good"
elif average_score >=50:
    performance = "Average"
else:
    performance = "Needs Improvement"

# Check Attendance Status (ternary operator)
# value_if_true if condition else value_if_false
attendance_status = "WARNING Low Attendance" if attendance < 75 else "OK Attendance Satisfied"

# Display Final Results
print("="*50)
print("Student Grade Tracker")
print(f"Student ID: {student_id}")
print(f"Student Name: {student_name}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score}")
print(f"Total Subjects: {number_of_subjects}")
print(f"Performance: {performance}")
print(f"Attendance Status: {attendance_status}")
print("="*50)