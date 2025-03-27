
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


char = input("Enter the character: ")

modified_char = get_next_character(char)

print(f"The the character via the function {modified_char}")