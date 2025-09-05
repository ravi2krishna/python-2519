# Nested Conditional : Conditionals inside Conditionals

# dynamic voting app
age = int(input("Enter Age: "))
has_id = input("Do you have id (yes/no): ")

if age >= 18:
    if has_id == "yes":
        print("You can vote")
    else:
        print("You need an ID to vote") 
else:
    print("You are too young to vote") 