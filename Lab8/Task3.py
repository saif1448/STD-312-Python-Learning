
source_file_path = 'foo.txt'
copied_file_path = 'bar.txt'

try:
    # it is opening the file in read mode
    with open(source_file_path, 'r') as file:
        file_content = file.read()

    #it is opening the file in new file creation mode
    with open(copied_file_path, 'x') as file:
        file.write(file_content)

except FileNotFoundError: # it is gonna handle the error if the file is not present
    print(f'File "{source_file_path}" not found.')
except FileExistsError: # it is gonna handle the error if the file already exists
    print(f'File "{copied_file_path}" already exists.')
