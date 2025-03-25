# variable name
# function name
# must be self explanatory

# a and b are two parameters
# function name explains what the function do ----> getting the average of 2 numbers
def get_avg_num(a, b):
    return (a+b)/2

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

avg = get_avg_num(a,b)

print(f"The average of {a} and {b} is : {avg}")
