# Working with JSON Files

import json

student = {
   "id": 101,
   "name": "Ravi",
   "course": "Python Full Stack",
   "skills": ["Python", "Git", "AWS"],
   "score": 60
}

print(type(student))

# Writing Above Data To Json File - No Indentation
with open("12_file_ops/students.json","w") as file_data:
    json.dump(student,file_data)
    
# Writing Above Data To Json File With Indentation
with open("12_file_ops/students.json","w") as file_data:
    json.dump(student,file_data,indent=1)
    
# Writing Above Data To Json File With Recommended Indentation
with open("12_file_ops/students.json","w") as file_data:
    json.dump(student,file_data,indent=4)
    
# Reading JSON File 
with open("12_file_ops/students.json","r") as file_data:
    json_reader = json.load(file_data)
print(json_reader)
# get student name
print(json_reader["name"])

if json_reader["score"] >= 75:
    print(f'{json_reader["name"]} passed')
else:
    print(f'{json_reader["name"]} not passed')
    
# Working with Objects 

# Writing
student = {
   "id": 101,
   "name": "Ravi",
   "course": "Python Full Stack",
   "skills": ["Python", "Git", "AWS"],
   "score": 60
}
print(type(student))
student_data = json.dumps(student)
print(student_data)
print(type(student_data))


# Reading
json_obj = '{"id":101, "name":"john", "course":"python"}'
print(type(json_obj))

student_data = json.loads(json_obj)
print(student_data)
print(type(student_data))
print(student_data["course"])
