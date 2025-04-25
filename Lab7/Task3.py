import os

file_path = "test3.txt"
file_size = os.path.getsize(file_path)
print(f'The initial file size is {file_size} bytes')

with open(file_path, mode='r+', encoding='utf-8') as file:
    lines = []

    #fetching first 2 lines
    for i in range(1,3):
        line = file.readline()
        lines.append(line)
    #appending first 2 lines
    for line in lines:
        file.write(line)

    #going back to the initial position in the file
    #then reading 3 lines and printing them
    file.seek(0)
    for i in range(1, 4):
        line = file.readline()
        print(f'line {i}: {line}', end='') # end='' is omitting the the \n character at the end

    size = os.path.getsize(file_path)
    print(f'The updated file size is {size} bytes')
