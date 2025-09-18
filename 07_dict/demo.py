# dictionaries

# empty dict 
empty_dict = {}
print(type(empty_dict))
print(empty_dict)

# dict_nums 
dict_nums = {1:10,2:20,3:30}
print(dict_nums)

dict_nums = {1.1:101,2.1:201,3.1:301}
print(dict_nums)

# dict_text
dict_text = {"one":"1","two":"2"}
print(dict_text)

# mixed_data
dict_mixed = {1:101,"two":2,3:"three"}
print(dict_mixed)

# incorrect 
# dict_data = {[10]:"ten",[20]:"twenty"} # TypeError: unhashable type: 'list'
dict_data = {(10):"ten",(20):"twenty"} # tuple is immutable
print(dict_data)

# list inside list 
nested_list = [10,20,30,["one","two"]]
print(nested_list)
print(nested_list[0])
print(nested_list[3][0]) # one

# tuple inside tuple
nested_tuple = (10,20,30,("one","two"))
print(nested_list)

# dict inside dict 
students = {
   "101": {
       "name": "Ravi",
       "email": "ravi@gmail.com",
       "course": "Python"
   },
   "102": {
       "name": "Anjali",
       "email": "anjali@gmail.com",
       "course": "Java"
   },
   "103": {
       "name": "John",
       "email": "john@gmail.com",
       "course": "DevOps"
   }
}

print(students)

# accessing 
dict_nums = {1:10,2:20,3:30}
print(dict_nums)
# print(dict_nums[0]) # KeyError: 0
print(dict_nums[1]) # Access with key, not index

dict_text = {"one":"1","two":"2"}
print(dict_text)
print(dict_text["one"])
# print(dict_text["three"]) # KeyError: 'three'

print(students)

print(students["101"])
print(students["101"]["email"])

# add item to dictionary
dict_nums = {1:10,2:20,3:30}
print(dict_nums)
dict_nums[4] = 40
print(dict_nums)

# update 
dict_nums[4] = 400
print(dict_nums)

# using class
dict_nums = dict({1:10,2:20,3:30})
print(dict_nums)

# accessing using loops will get only keys, but not values 
dict_nums = {1:10,2:20,3:30}
print(dict_nums)
for num in dict_nums:
    print(num)

# print(dir(dict_nums))

# duplicates : duplicate keys are not allowed, replaced  
dict_nums = {1:10,2:20,3:30,1:40}
print(dict_nums)

# duplicates : duplicate values are allowed 
dict_nums = {1:10,2:20,3:30,4:10,5:10}
print(dict_nums)