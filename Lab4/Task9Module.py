

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

def reverse_string(input_str):
    size = len(input_str)

    reversed_str = ""

    for idx in range(size - 1, -1, -1):
        reversed_str += input_str[idx]

    return reversed_str


def extract_numbers(input_str):

    extracted_number_str = ""

    for num in input_str:
        if num.isdigit():
            extracted_number_str += num

    if extracted_number_str == "":
        return 0
    else:
        extracted_number = int(extracted_number_str)
        return extracted_number


def shift_string(input_str):
    shifted_str = ""
    for char in input_str:
        shifted_str += get_next_character(char)  # a --> b

    return shifted_str