
#ord() example

# each and every character has an associated numerical value
# this numerical value is called the ascii value

#ord() ---> it gives you the ascii value of a particular character

char = 'a'
num = ord('a')

num += 2

print(num)

#chr() ---> it converts back the numeric ascii value to ascii character
new_char = chr(num)
print(new_char)

#isalpha() ----> it determines wheather the character is alphabetic

char = '5'
print(char.isalpha())