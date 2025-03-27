# from Task4 import get_next_character

def get_next_character(char):
    if char.isalpha():
        char_numeric_val = ord(char)
        char_numeric_val += 1
        if char_numeric_val > 90 and char_numeric_val < 97:
            char_numeric_val = 65
        elif char_numeric_val > 122:
            char_numeric_val = 97
        char = chr(char_numeric_val)
        return char
    else:
        return char


def shift_string(input_str):
    shifted_str = ""
    for char in input_str:
        shifted_str += get_next_character(char)  # a --> b

    return shifted_str


while True:
    input_str = input("Enter the string: ")

    if input_str == "stop":
        print("The program is being stopped")
        break

    shifted_str = shift_string(input_str)

    print(f"Shifted String: {shifted_str}")


# program flow:
# main program ---> shift_string() ----> get_next_character()