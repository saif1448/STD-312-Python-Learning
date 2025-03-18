
#Concatenation --> +

str_1 = "A"
str_2 = "B"

res = str_1 + str_2

print(f"Concatenated String {res}")

#String conversion to int or float
# int() ---> int
# float() ---> float

# To check if a string is substring of a main string

input_str = "I am a good boy"
# every part of string is called a substring
# for checking we can use the 'in' operator

sub_str = "good"

#I -- 0
#  -- 1
# a -- 2
# m -- 3

print(sub_str in input_str)

# to check from which index the substring is being initiated ---> use find()

sub_str_idx = input_str.find(sub_str)

print(sub_str_idx)

# if the value is -1 --> it means the sub string is not present in the main string


