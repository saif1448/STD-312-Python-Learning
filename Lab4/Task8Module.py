from math import inf

def get_avg_num(a, b):
    return (a+b)/2

def avg_main():
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    avg = get_avg_num(a, b)

    print(f"The average of {a} and {b} is : {avg}")


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

def largest_main():
    biggest_number = get_largest_number()

    print(f"The largest number is {biggest_number}")

