#
# file1 = open('TestFile1.txt', 'r')
# file2 = open('TestFile2.txt', 'r')
# file3 = open('TestFile3.txt', 'r')

# we must use the close() to close the file after file operation

# it is exactly safer to use with operator

with open("file.txt", "w") as file:
    file.write("Hello World")

# with operator autimatically close the file after file operation