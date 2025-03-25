
#Local and Global Scope

# the variable which is present into a particular code block only ---> the variable's scope is contrained into that code block
# here code block means ---> function, if else, loop

a = 10  # this variable is present until the program is being ended # whole through the program
# that is why this a variable's scope is global


def get_new_a_val():
    a += 25   # you cannot directly change the global variable value inside a function
    b = 100
    print(f"a : {a}")
    print(f"b : {b}")

print(f"a : {a}")

get_new_a_val()

print(f"a : {a}")

# But there is problem when we try to modify the global variable value inside a function