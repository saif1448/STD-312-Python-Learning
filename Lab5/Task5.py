
def capitalize_word(word):
    capitalized_word = ""
    for char in word:
        capitalized_word += char.upper()

    return capitalized_word

# this is the function without side effect
def capitalize_word_list(word_list):
    capitalized_word_list = []
    for word in word_list:
        capitalized_word = capitalize_word(word)
        capitalized_word_list.append(capitalized_word)
    return capitalized_word_list

def capitalize_word_list_side_effect(word_list):
    i = 0
    while i < len(word_list):
        word_list[i] = capitalize_word(word_list[i])
        i += 1

L = ['apple', 'banana', 'asd']

# word_list = L ----> it raises a concern for side effect
# capitalized_word_list = capitalize_word_list(L)

# print(capitalized_word_list)

capitalize_word_list_side_effect(L)
print(L)