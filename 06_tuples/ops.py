# Tuples Methods / Operations

# count() : gives number of times a specific elements appears in list
tuple_nums = (10, 20, 30, 20, 40, 20, 10, 20, 10, 20, 10)
# count_10 = list_nums.count() # TypeError: list.count() takes exactly one argument (0 given)
count_10 = tuple_nums.count(10)
print(count_10)
count_40 = tuple_nums.count(40)
print(count_40)


# index() : returns the index position of a specified value
tuple_nums = (10,20,30,40,50)
print(tuple_nums)
# list_nums.index() # TypeError: index expected at least 1 argument, got 0
# list_nums.index(1) # ValueError: 1 is not in list
index = tuple_nums.index(10)
print(index)