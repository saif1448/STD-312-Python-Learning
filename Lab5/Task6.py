import sys

def capitalize_word(word):
    capitalized_word = ""
    for char in word:
        capitalized_word += char.upper()

    return capitalized_word

def capitalize_word_list_side_effect(word_list):
    i = 0
    while i < len(word_list):
        word_list[i] = capitalize_word(word_list[i])
        i += 1

list_len = len(sys.argv)
L = []

i = 1
while i < list_len:
    L.append(sys.argv[i])
    i += 1

capitalize_word_list_side_effect(L)

print(L)


