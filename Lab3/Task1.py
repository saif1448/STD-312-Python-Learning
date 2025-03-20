input_str = input("Enter the string: ")

size = len(input_str)

reversed_str = ""

for idx in range(size-1, -1, -1):
    reversed_str += input_str[idx]

print(reversed_str)

reversed_text_default = input_str[::-1]

print(reversed_str == reversed_text_default)





# ABCD
# len(ABCD) ---> 4
# size = len("ABCDE") = 5
# starting index = 0
# ending index = size-1 = 5-1 =4
# step = -1
# 4
# 3
# 2
# 1
# 0
# -1

