

line_list = []

# Reading this file
with open("TestFile1.txt", "r") as f:
    count = 1
    for line in f:
        print(f'{count}. {line}', end='')
        count += 1
        line_list.append(line)

#writing a txt file
with open("TestNewFile.txt", "w") as f:
    for line in line_list:
        f.write(line)




