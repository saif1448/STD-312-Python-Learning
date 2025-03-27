
def reverse_string(input_str):
    size = len(input_str)

    reversed_str = ""

    for idx in range(size - 1, -1, -1):
        reversed_str += input_str[idx]

    return reversed_str


while True:
    input_str = input("Enter a string to reverse: ")

    if input_str == "stop":
        print("The program is being stopped")
        break

    reversed_str = reverse_string(input_str)

    print(f"Revesed String: {reversed_str}")
