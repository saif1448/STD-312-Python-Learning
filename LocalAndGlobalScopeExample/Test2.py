
# More on local and global scope

#This variable is global
a = 10

def show_a_val():
    print(f"a : {a}")


print(f"a : {a}")

show_a_val()

a += 25 # we are changing the global variable value

print(f"a : {a}") # we are printing the changed value here

show_a_val() # and also the function is getting the changed value here


# There is no problem to use the global variable inside a function
