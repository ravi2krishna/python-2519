# list methods : perform operations on List
list = [10]
# print(dir(list))

list_nums = [10,20,30,40,50]

# append() : adds an element to end of the list
# list_nums.append() # TypeError: list.append() takes exactly one argument (0 given)
# list_nums.append(60,70) # TypeError: list.append() takes exactly one argument (2 given)
list_nums.append(60)
print(list_nums)

# extend() : takes an iterable and adds each element to the list individually at the end
list_nums = [10,20,30,40,50]
# list_nums.extend(60) # TypeError: 'int' object is not iterable
print(list_nums)
# list_nums.extend() # TypeError: list.extend() takes exactly one argument (0 given)
list_nums.extend([60])
list_nums.extend([70,80,90])
print(list_nums)

# insert() : allows you to insert element at a specific position 
list_nums = [10,20,40,50]
print(list_nums)
# list_nums.insert() # TypeError: insert expected 2 arguments, got 0
list_nums.insert(2,30)
print(list_nums)

list_nums.insert(10,100) # if index is out of range, adds element at end
print(list_nums)

list_nums.insert(0,5) # moving and placing elements 
print(list_nums)

list_nums[0] = 0 # replace not move
print(list_nums)

# pop() : removes an element in list by default is last element 
list_nums = [10,20,30,40,50]
print(list_nums)
list_nums.pop() # by default is last element 
print(list_nums)
list_nums = [10,20,30,40,50]
list_nums.pop(2) # based on index number within range
print(list_nums)
list_nums = [10,20,30,40,50]
# list_nums.pop(10) # based on index number out of range # IndexError: pop index out of range
print(list_nums)

# remove() : removes element based on value not index
list_nums = [10,20,30,40,50]
print(list_nums)
# list_nums.remove() # TypeError: list.remove() takes exactly one argument (0 given)

# list_nums.remove(1) # ValueError: list.remove(x): x not in list
list_nums.remove(10)
print(list_nums)

list_nums = [10,20,30,40,50,10,30,10]
print(list_nums)
list_nums.remove(10) # by default only first occurrence will be removed
print(list_nums)

list_nums = [10,20,30,40,50,10,30,10]
print(list_nums)
# my req is remove all 10's
while 10 in list_nums:
    list_nums.remove(10)
print(list_nums)

# clear() : removes all the elements and empties list 
list_nums = [10,20,30,40,50]
print(list_nums)
list_nums.clear()
print(list_nums)

# NOTE : with above observations we can say list data type is changeable (mutable)

# index() : returns the index position of a specified value
list_nums = [10,20,30,40,50]
print(list_nums)
# list_nums.index() # TypeError: index expected at least 1 argument, got 0
# list_nums.index(1) # ValueError: 1 is not in list
index = list_nums.index(10)
print(index)

index = list_nums.index(30)
print(index)

# index = list_nums.index(80) # ValueError: 80 is not in list
print(index)

# index() with start and stop
list_nums = [10, 20, 30, 20, 40, 20, 10, 20, 10, 20, 10]

# value, start
print(list_nums.index(20,2))  # 3

# value, start, stop
print(list_nums.index(20,4,8))  # 5

# count() : gives number of times a specific elements appears in list
list_nums = [10, 20, 30, 20, 40, 20, 10, 20, 10, 20, 10]
# count_10 = list_nums.count() # TypeError: list.count() takes exactly one argument (0 given)
count_10 = list_nums.count(10)
print(count_10)
count_40 = list_nums.count(40)
print(count_40)

list = [10]
print(dir(list))

# reverse() : reverses the elements in the list, inplace operation
list_nums = [10,20,30,40,50]
print(list_nums)
list_nums.reverse()
print(list_nums)

# reverse using slicing technique 
list_nums = [10,20,30,40,50]
print(list_nums)
print(list_nums[::-1])
print(list_nums)

# sort() : sort the elements of list, inplace operation, ascending order 
list_nums = [20,10,30,50,40]
print(list_nums)
print(list_nums.sort())
print(list_nums)

# sort in descending order 
list_nums = [20,10,30,50,40]
print(list_nums)
print(list_nums.sort(reverse=True))
print(list_nums)

# sort with text
list_courses = ["c","python","java","cloud"]
print(list_courses)
print(list_courses.sort())
print(list_courses)

# mixed data
list_mix = [20,10,"c","python",30,50,40]
print(list_mix)
# print(list_mix.sort()) # TypeError: '<' not supported between instances of 'str' and 'int'
print(list_mix)

# copy() : creates a shallow copy, meaning when we modify the backup copy, original will not affect 
list_nums = [10,20,30,40,50]
print(list_nums)

bk_list = list_nums.copy()
print(bk_list)

bk_list.append(60)
print("Backup Copy: ",bk_list)
print("Original Copy: ",list_nums)

# soft copy(=), meaning when we modify the backup copy, original will also affect 
list_nums = [10,20,30,40,50]
print(list_nums)

bk_list = list_nums
print(bk_list)

bk_list.append(60)
print("Backup Copy: ",bk_list)
print("Original Copy: ",list_nums)