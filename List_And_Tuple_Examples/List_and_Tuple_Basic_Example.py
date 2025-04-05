import math

# List or Tuple
# Both of them are sequential data containers
# Sequential ---> Data will be placed in the memory in sequential manner

# ls = [ 10, 20, 30, 40, 50 ]

# --------------------------------------------
#  205  | 206   |  207  | 208   | 209   |
#---------------------------------------------
#   10  | 20    | 30    |  40   |  50   |
#---------------------------------------------
#   0   | 1     |  2    |  3    |  4    |
#---------------------------------------------
#   -5  | -4    | -3    |  -2   |  -1   |               -----> this is how the negative indexing works
#---------------------------------------------


# As the data ar put in sequential manner, they are placed in an offset distance
# these offset numbers are called the indexes of the data

# just like list, tuple can also be indexed

ls = ["asd"]

tup = ("aasd",) # for the case of tuple there must be a comma after the first element

print(type(ls))
print(type(tup))


# Most common task of every data structure
# Searching: Finding a specific element or value within a data structure.
# Sorting: Arranging elements in a specific order (ascending or descending).
# Insertion: Adding new elements or data to a data structure.
# Deletion: Removing existing elements or data from a data structure.
# Traversal: Visiting each element of a data structure in a specific order.
# Merging: Combining two or more data structures into one.

ls = [ 10, 20, 30, 40, 50 ]
tup = (10, 20, 30, 40, 50)


# Searching

# we can search via the index number

print(ls[3])
print(tup[2])

# there is an operator called in

if 10 in ls:
    print("yes")
else:
    print("no")

if 200 in tup:
    print("yes")
else:
    print("no")

#sorting
# both list and tuple can contain any type of data
ls = ['a', True, 1, "asda", [1,2,3], 1.2]

tup = ('a', True, 1, "asda", [1,2,3], 1.2)

print("Printing list items types")
for val in ls:
    print(type(val))

print("Printing tuple items types")
for val in tup:
    print(type(val))

# for the case of sorting, try to put similar type of data
# for sorting, use the sort() function, and put similar data
# ls.sort()
# print(ls) # here there will be an error

ls = [50.0, 70.29, 10.0, 100.0, 30.0]
ls.sort()
print(ls)


# but you cannot sor thed tuple

tup = (50.0, 70.29, 10.0, 100.0, 30.0)
# tup.sort() ---> there is no sort() funtion for tuple
# because tuple is immutable ------>


#Mutability
    # Mutable -----> which can be changed
    # Immutable ----> which cannot be changed

ls[1] = 89
print(ls) # example of mutablity
# tup[1] = 89 ----> this is not possible, re assigning values is prohibited in tuple

# dot operator
# class and objects ----> they are part of object oriented programming
# for case of oop --> rather then asking how to do something, we ask what to do with

# You are gonna do something with Car
# A car has 4 wheels, 1 horn, glasses, engines
# A can can drive, a car can sound the horn etc.
# Practical example of car is ---> Toyota, Mercedes
# Here the class is the Car
# and Toyota and Mercedes are the objects of this Car class

# just like this, every type in python are in their respective Classes

# ls1 = [ 10, 20, 30 ]
# ls2 = ['a', 'b', 'd']
# here both ls1 and ls2 are objects of list class
# list class has a set of methods or functions
    # sort()
    # append()

# when you are gonna call a method of a class you have to use the dot operator
# dot operator will gonna be associated with the object

# ls1.sort()
# ls2.sort()




# Insertion and Merging

ls =  [50.0, 70.29, 10.0, 100.0, 30.0]
tup = (50.0, 70.29, 10.0, 100.0, 30.0)

# for inserting a new value at the end of the list ---> append()
ls.append(90)
print("After inserting at 5th index")
print(ls)

# if we want to add a value in a particular indes ---> insert()
ls.insert(2, 200)
print("after inserting at 2 index")
print(ls)

# if we want to add at the end of the list ---> extend() ---> which works similar like the + operator

ls += [1000]
print("After using the + oeprator")
print(ls)

# you can also add a list using extend()
# It is also an example of merging
ls.extend([2000, 3000, 4000])
print(ls)

ls2 = [900, 800, 700]
ls.extend(ls2)

#extend and append is not same
#extend put the new value at the end of list as a part of the list
# but append doesnt do that
# append is suitable is to insert single object into the list
ls.append([6000,7000,8000])
print(ls)


# and none of the above inserting functions is gonna work for tuple



# Deletion
# remove(), pop(), clear()

# clear() ----> it clears out everything in the list, and not suitable for tuple

print("Clear function effect")
ls.clear()
print(ls)

ls.extend([10, 20, 30, 40, 50, 60, 70])
print(ls)


# pop() ---> it removes value either from the left end or right end
print("Pop function by default delete the right most value and also this function returns the right most value after deletion")
val = ls.pop()
print(ls)
print(val)

#it can also remove value at particular index
print("It is deleting a value in a particular position")
val = ls.pop(0)
print(ls)
print(val)

val = ls.pop(3)
print(ls)
print(val)

# remove() ---> it removes the first occurance of the given object
val = ls.remove(30) #it doesnt return a value like the pop()
print(ls)
print(val)

ls.remove(60)
print(ls)

ls.clear()

ls = ['a', 'b', 'a', 'b', 'a', 'b' ]
print(ls)
ls.remove('b')
print(ls)


# Traversal ----> moving over every value in the tuple of list

print("Traversal over the every value in the list or tuple")
for val in ls:
    print(val)

for val in tup:
    print(val)



