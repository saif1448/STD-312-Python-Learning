
# Dictionary is a data structure, it stores the value using the key value pair
# Key ----> The unique thing ---> it will be used like an index
# Value ---> They are changeable
# To create dictionary we can use {}

# Dictionary  ---> Hash Map, Map, Object

book_lib = {} # it is creating a blank dictionary

# insertion
# key  can be any object ---> string, int, float, character
book_lib['ABCD'] = "It is a novel describing the history"
book_lib['EFGH'] = [1, 3, 5, 7, 9]
        # key       # value

# if you want to createa a dictionary directly
new_dic = {
    'abc' : 10,
    'def' : 20,
    'ghi' : 30,
}

print(new_dic)
# value ---> value can be anything
# anything means
    # it can be a string
        # a list
        # a tuple
        # a set
        # a dictionary itself
        # a object
print(book_lib)

new_dic['ihj'] = 40
print(new_dic)

# deletion
# pop() ----> it removes the value of a given key and returns the given key value
var = new_dic.pop('ghi')
print("After popping ghi key value")
print(new_dic)
print(var)

#del
del new_dic['ihj'] # like pop() , del does not return anything
print(new_dic)

#popitem() ---> it removes the last element and returns its value
var = new_dic.popitem()
print(var)
print(new_dic)

# searching
# print(book_lib['PQWR']) ----> it will raise error as there is no key named PQWR

# get()
print(book_lib.get("ABCD", "Key is not present")) # get or default

# sorting
new_dic = {
    'ghi' : 30,
    'abc' : 10,
    'def' : 20,
}

output_list = sorted(new_dic) # sorted() will return the sorted key list here
print(output_list)
output_list = sorted(new_dic.items()) # you are getting key value pair as tuple and they are sorted
print(output_list)

# traversal

# traverse with the key
for key in new_dic:
    print(f"{key} : {new_dic[key]}")

# traverse only with the values
#values()
print(new_dic.values())
for val in new_dic.values():
    print(f"{val} ")

# both key and value separately
#items()
for key,value in new_dic.items():
    print(f"{key} : {value}")

# merging
# it means combining multiple dictionaries
new_dic_2 = {
    'pqr': 60,
    'wxy': 70,
    'xyz' : 80
}

# we have to use the function update

new_dic.update(new_dic_2)

print(new_dic)

new_dic['wxy'] = 1000
print(new_dic)


