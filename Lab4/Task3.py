# Global Variable and Local Variable

from math import inf
# import math

largest_number = float(-inf)
def get_largest_number():

    global largest_number

    current_number = 0.0

    while True:
        current_number = input("Enter new number: ")
        if current_number == "stop":
            break
        else:
            current_number = float(current_number)
            if current_number > largest_number:
                largest_number = current_number

    # print(f"The largest number is {largest_number}")
    # return largest_number

# biggest_number = get_largest_number()

get_largest_number()

print(f"The largest number is {largest_number}")