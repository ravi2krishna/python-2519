# Dictionary Operations

# update() : adds / updates dict items 
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)

fruits_dict.update({"c":"cherry"}) # adding 
print(fruits_dict)

fruits_dict.update({"a":"avocado"}) # updating
print(fruits_dict)

# pop() : removes item with specified key 
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)

fruits_dict.pop("a") # TypeError: pop expected at least 1 argument, got 0
print(fruits_dict)

# fruits_dict.pop("c") # KeyError: 'c'
print(fruits_dict)

# popitem() : removes last item 
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)
fruits_dict.popitem()
print(fruits_dict)

# clear() : removes all items i.e empties dictionary
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)
fruits_dict.clear()
print(fruits_dict)

# get() : used to get the value for key 
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)
print(fruits_dict.get("b"))
print(fruits_dict.get("c")) # if key doesn't exist -> None

# keys() : returns all the keys 
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)

print(fruits_dict.keys()) 

only_keys = fruits_dict.keys()
for key in only_keys:
    print(key)


fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)

for key in fruits_dict:
    print(key)

# values() : returns all values 
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)

print(fruits_dict.values())

only_values = fruits_dict.values()
for value in only_values:
    print(value)
    
# items() : returns both keys and values 
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)

print(fruits_dict.items())
keys_values = fruits_dict.items()

for item in keys_values:
    print(item)
    print(item[0])

# copy() : create a shallow copy 
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)

bk_fruits_dict = fruits_dict.copy()
print(bk_fruits_dict)

bk_fruits_dict.update({"c":"cherry"})
print(fruits_dict)
print(bk_fruits_dict)

# soft copy using = 
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)

bk_fruits_dict = fruits_dict
print(bk_fruits_dict)

bk_fruits_dict.update({"c":"cherry"})
print(fruits_dict)
print(bk_fruits_dict)
print("======")
# setdefault() - Returns value of a key, if not present sets it
# if the key is present, will not update
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)

print(fruits_dict.setdefault("b","blackberry"))
print(fruits_dict)

print("======")

fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)

print(fruits_dict.setdefault("c","cherry"))
print(fruits_dict)