# Sets

# empty set
empty_set = {} # dict
print(type(empty_set))
print(empty_set)

# empty set should be created using class
empty_set = set() # set
print(type(empty_set))
print(empty_set)

# numbers set 
num_set = {10,20,30,40,50}
print(type(num_set))
print(num_set) # {50, 20, 40, 10, 30} # Unordered

# Duplicates eliminated 
num_set = {10,20,30,40,50,10,20}
print(num_set) # {50, 20, 40, 10, 30} # Unique 

# No Index 
num_set = {10,20,30,40,50}
# print(num_set[0]) # TypeError: 'set' object is not subscriptable # Unindex

# string & mixed 
text_set = {"ab","good","morning"}
print(text_set)

mixed_set = {10,20,30,40,50,"ab","good","morning"}
print(mixed_set)

# Accessing using __iter__
num_set = {10,20,30,40,50}
# print(dir(num_set))

for num in num_set:
    print(num) 
    
# convert to access using index
list_nums = list(num_set)
print(list_nums[0])
print(dir(num_set))