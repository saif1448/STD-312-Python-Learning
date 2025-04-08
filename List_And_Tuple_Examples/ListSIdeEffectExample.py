
# call by value and call by reference

x = [10, 20, 30, 40, 50]
y = x

y[2] = 100

print(x)
print(y)

x[0] = 200
print(x)
print(y)

# when we are doing the = assignment, it assigns the address of the first element

# this is the thing we are calling the side effect,
# changing in x also changes the values in y and vise versa
# this thing is called as call by reference


y = x.copy() # it wont pass tje reference, rather it will copy everything in x to y

x[1] = 300
print(x)
print(y)


# this is how we are avoiding the side effect