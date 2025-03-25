from math import inf
# import math
def get_largest_number():
    current_number = 0.0
    largest_number = float(-inf)

    while True:
        current_number = input("Enter new number: ")
        if current_number == "stop":
            break
        else:
            current_number = float(current_number)
            if current_number > largest_number:
                largest_number = current_number

    # print(f"The largest number is {largest_number}")
    return largest_number

biggest_number = get_largest_number()

print(f"The largest number is {biggest_number}")