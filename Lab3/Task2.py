
current_number = 0.0
largest_number = -111111

while True:
    current_number = input("Enter new number: ")
    if current_number == "stop":
        break
    else:
        current_number = float(current_number)
        if current_number > largest_number:
            largest_number = current_number


print(f"The largest number is {largest_number}")
