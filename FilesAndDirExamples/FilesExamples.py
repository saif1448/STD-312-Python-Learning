
# text files
# binary files ---> explicitly mention

# file contents are being saved as byte chunks ---> HDD or SSd ---> in your secondary memory

# all files are being located with their paths
# 2 types of paths
    # Absolute path
    # Relative path

# Absolute Path
    # The path of a file from the root directory
    # windows ---> \ ---> back slash
    # unix ---> / ---> forward slash
    # it is not portable
    # problematic to use

# Relative path
    # This is relative to some source folder
    # We call this current working directory (CWD)
    # More portable

# we can use the os module to work with the directories
import os

print(os.getcwd())

# when we are gonna deal wit the files, we must first open it
# and after using that file we must close it

# open file
# open() ---> to open a particular

# file = open('TestFile2.bin', 'rb')

# 2 types file checking
# t ---> for text files
# b ---> binary files


#read(n) ---> read first n characters
#read() ----> it will read the entire file

file = open('TestFile1.txt', 'r')

# file_output = file.read()

# file_output = file.readline()
# print(file_output)
# file_output = file.readline()
# print(file_output)

# readline() ---> read lines one at a time, one by one, read the next line


for line in file:
    print(line, end='') # the end='' is skipping the new line character at the end of each line

file.close()

file = open('TestFile1.txt', 'w')
file.write('Hello World new version')

# when we perform the write operation over a file, it is gonna truncate the entire file
# truncate means it is going to remove everything in the file first
# then it is gonna re-write the new content

file.close()

file = open('TestFile1.txt', 'a')
file.write(' Hello World in the next line')
file.close()

# append mode does not truncate the file. it just append the new text at the end of the file

#file.tell() ----> right now in which position you are reading the file
# file.seek(n) ---> it will change the position from where the file is gonna be read

file = open('TestFile1.txt', 'r')
file.seek(7)
output_str = file.read()
print(output_str)


