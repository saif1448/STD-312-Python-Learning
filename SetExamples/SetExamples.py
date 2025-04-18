
# List ---> sequential
# Tuple ---> sequential
# Dictionary ---> non sequential
# Set ---> non sequential

# Set

s = {'a', 'b', 'c'}
print(s)
print(type(s))
#you have to create using the set function
s = set()

# what is a set?
# Set is a collection of unique items
# the positions of the unique items can be changed
# it is non sequential
s = {'a', 'b', 'c', 'a', 'b', 'c'}
print(s)

words_with_repeats = [
    "apple", "banana", "apple",
    "cherry", "banana", "apple",
    "date", "cherry", "banana",
    "fig", "grape", "banana"
]

s = set(words_with_repeats)

s = {10, 230, 40,5, 100}

max = max(s)
min = min(s)
sum = sum(s)

print(f"max = {max}, min = {min}, sum = {sum}")

sorted_items = sorted(s)
print(sorted_items)
print(type(sorted_items))

# you cannot index over the set
# because of this it is non sequential

# Insertion
# add()
s = {10, 20, 30, 400}
s.add(50)
print(s)

#Deletion
# remove()
s.remove(20)
print(s)
# s.remove(1000) # it will raise an error if the element is not found while using the remove()
s.discard(30)
print(s)
s.discard(1000) # discard() will only remove if the element is found, and it won't raise error if not found

#po() ---> removes the first element in the set and returns that element, but you cannot be certain which element is gonna be the first element
val = s.pop()
print(val)
print(s)

# clear() ----> it clears out the set
s.clear()
print(s)

# searching
# for searching we are gonna use the in operator
# only we can check if an element is present in the set or not
s = {10, 20, 30, 400}
print(100 in s)

# sorting
# we cannot sort a set
# if we want to sort a set, we can use sorted(), but it will return a list of sorted items
items = sorted(s)
print(items) # here the items is a list of sorted items from the set

#traversing
# we can use the loop
for item in s:
    print(item)

# merging
# UNION ---> union function and | operator works the same way
a = {1,2,4,5}
b = {4,5,6}
c = a.union(b)
d = a | b
print(c)
print(d)
# INTERSECTION ---> intersection() and & operator
c = a.intersection(b)
d = a & b
print(c)
print(d)
# DIFFERENCE ----> difference() and - operator
c = a.difference(b)
print(c)
d = a - b
print(d)
# SYMMETRIC DIFFERENCE ---->  symmetric_difference()
c = a.symmetric_difference(b)
print(c)






