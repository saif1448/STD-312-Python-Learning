
# function contains a block of code
# purpose is to reuse that block of code any time any where as per demand

ls_1 = [200,100,300,50,1000,800,900,600]

ls_2 = [800,400,1200,500,450,390,110,480]

# max_val = 0
# for num in ls_1:
#     if num > max_val:
#         max_val = num
#
# print(f"The maximum number in ls_1 is {max_val}")


# max_val = 0
# for num in ls_2:
#     if num > max_val:
#         max_val = num
#
# print(f"The maximum number in ls_2 is {max_val}")

#structure
# def function_name(parameter_list) :
#   function_body ----> the code block I want to use


def find_max_value(input_list):
    max_val = 0
    for num in input_list:
        if num > max_val:
            max_val = num

    print(f"The maximum number in list is {max_val}")


find_max_value(ls_1)
find_max_value(ls_2)

ls_3 = [1500,2000,1700,2500,900,1800,3500,1400,7000]
find_max_value(ls_3)



# this function is taking 2 inputs
def add_two_number(a, b):
    print(f"The sum is {a+b}")

#we are calling the function --> add_two_number below

add_two_number(5,6)
add_two_number(11,29)
add_two_number(50,90)


#this function is taking 3 inputs
def find_the_largest(a, b, c):
    if a > b:
        if a > c:
            print(f"{a} is the largest")
        else:
            print(f"{c} is the largest")
    else:
        if b > c:
            print(f"{b} is the largest")
        else:
            print(f"{c} is the largest")

#we are calling the function --> find_the_largest below
find_the_largest(100,200,300)
find_the_largest(300,5000,1000)
find_the_largest(1000,600,900)


#This funciton is not taking any input
def say_greeings():
    print("Hi there!")

#we are calling the function --> say_greeting below
say_greeings()
say_greeings()
say_greeings()


# conclusion

# function will contain a block of code
# this block of code will be executed whenever the function is called
# function may take any number input or doesn't take any input at all
# function may return any value or doesn't return any value at all


# function is of two types ---> built-in and another is user-defined
# built-in ---> print(), len(), int()
# user-defined ---> say_grettings(), find_the_largest()


# parameter and argument
# parameter ----> the inputs function is taking is called the parameter
# example --> add_two_numbers(a, b) ----> here a and b are the parameters
# argument ---> the actual value passed to the function
# example ---> add_two_numbers(500,600) ---> here 500 and 600 are the actual values --> hence they are the arguments
# you have to pass the same number of arguments as the same number of parameters


# return value
def modified_add_two(a, b):
    print("In the modified add two function")
    return a + b # it is returning a value

res = modified_add_two(10,17) # we are stroing the returned value in the 'res' variable
print(f"using modified two res: {res}") # we are using the 'res' variable here


def modified_greeting(name):
    return f"Hello There {name}"


saif_greeting = modified_greeting("Saif")
abcd_greeting = modified_greeting("ABCD")

print(saif_greeting)
print(abcd_greeting)


# you are receiving an output from the function
# that is why you need to store the output in a variable
# later you can use that variable as the way you want


