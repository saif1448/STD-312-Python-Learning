input_str = input("Enter the string: ")

size = len(input_str)

reversed_str = ""

for idx in range(size-1, -1, -1):
    reversed_str += input_str[idx]

print(reversed_str)

reversed_text_default = input_str[::-1]

print(reversed_str == reversed_text_default)


