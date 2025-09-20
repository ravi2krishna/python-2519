# Set Operations 

# add() : add element to set
s1 = {10,20,30,40,50}
print(s1)
s1.add(60)
print(s1)
# s1.add(70,80) # TypeError: set.add() takes exactly one argument (2 given)
print(s1)

# update() : adds multiple elements of iterables only 
s1 = {10,20,30,40,50}
print(s1)
s1.update([60,70,80])
print(s1)

# remove() : remove element, if not found error
s1 = {10,20,30,40,50}
print(s1)
s1.remove(20)
print(s1)
# s1.remove(90) # KeyError: 90
print(s1)

# discard() : remove element, if not found no error
s1 = {10,20,30,40,50}
print(s1)
s1.discard(20)
print(s1)
s1.discard(90) 
print(s1)

# clear() : removes all elements, empties set
s1 = {10,20,30,40,50}
print(s1)
s1.clear()
print(s1)

# pop() : removes an random element 
s1 = {10,20,30,40,50}
print(s1)
s1.pop()
print(s1)

# NOTE : Sets are Mutable (add, remove)

# copy() : creates a backup/shallow copy
s1 = {10,20,30,40,50}
print(s1)
s1_bk = s1.copy()
print(s1_bk)
s1_bk.add(60)
print(s1)
print(s1_bk)

# soft copy using =
s1 = {10,20,30,40,50}
print(s1)
s1_bk = s1
print(s1_bk)
s1_bk.add(60)
print(s1)
print(s1_bk)

# set specific operations (math related set operations)
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# union() : combines elements from both sets 
print(s1.union(s2))
print(s1 | s2)

# intersection() : extract only common elements
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)
 
# intersection_update() : extract only common elements, also update the calling set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.intersection_update(s2))
print(s1)
print(s2)

# difference() : removes the elements which also occur in other set(common elements)
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference(s2))
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)

# difference_update() : removes the elements which also occur in other set(common elements), updates calling set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference_update(s2))
print(s1)
print(s2)

# symmetric_difference() : removes common elements and take the combine elements left in both sets
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1)
print(s2)

# symmetric_difference_update() : removes common elements and take the combine elements left in both sets, , updates calling set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

# issubset() : checks if given set is subset of another set
s1 = {10,20,30,40,50}
s2 = {40,50}
s3 = {80,90}
print(s2.issubset(s1))
print(s3.issubset(s1))

# issuperset() : checks if given set is superset of another set
s1 = {10,20,30,40,50}
s2 = {40,50}
s3 = {80,90}
print(s1.issuperset(s2))
print(s1.issuperset(s3))

# isdisjoint() : checks if two sets have no common elements 
s1 = {10,20,30,40,50}
s2 = {40,50}
s3 = {80,90}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

# all 17 operations performed

# Frozenset : Immutable sets
fz_set = frozenset({10,20,30,40,50})
print(type(fz_set))
print(dir(fz_set))

fs1 = frozenset({10,20,30,40,50})
fs2 = frozenset({40,50,60,70,80})
print(fs1.union(fs2))
