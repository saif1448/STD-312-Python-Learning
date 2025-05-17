import csv


all_student_data = []

def calculate_letter_grade(total_mark):
    if total_mark >= 80:
        return 'HD'
    elif total_mark >= 70:
        return 'D'
    elif total_mark >= 60:
        return 'C'
    elif total_mark >= 50:
        return 'P'
    else:
        return 'F'


def check_duplicate_student_number(student_number):
    for std in all_student_data:
        if std['ID'] == student_number:
            return True
    return False


def write_std_record_to_file(std):
    with open(file_name, "a", newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['ID', 'Name', 'UnitMark', 'Grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(std)


def check_std_record_on_file(student_number):
    with open(file_name, 'rt', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)  # this function is returning a dictionary
        is_present = False
        for row in reader:
            if int(row['ID']) == student_number:
                is_present = True
                break
        return is_present

def add_student_data():
    global all_student_data
    student_data = {}
    student_number = int(input('Student Number: '))

    check = check_duplicate_student_number(student_number)
    if check:
        print(f'Student Number {student_number} already exists!')
        raise Exception('Student Number already exists')
    if student_number <= 0:
        raise ValueError('Student Number must be a positive integer')

    name = input('Name: ')
    unitMark = int(input('Unit Mark: '))

    if not 0 <= unitMark <= 100:
        raise ValueError('Unit Mark must be a positive integer')


    letter_grade = calculate_letter_grade(unitMark)

    student_data['ID'] = student_number
    student_data['Name'] = name
    student_data['UnitMark'] = unitMark
    student_data['Grade'] = letter_grade

    write_std_record_to_file(student_data)
    check_file = check_std_record_on_file(student_number)
    if check_file:
        all_student_data.append(student_data)
    else:
        print('Student Record Was not Written on the CSV File!')
        choice = int(input('Choose one of the following:\n '
                           '1. Cancel Operation\n'
                           '2. Exit Program'))
        if choice == 1:
            pass
        else:
            print('Exiting Program...')
            exit()



def search_student_data():
    choice = int(input('Choose the search option: \n'
                       '1. Based on Student Number\n'
                       '2. Based on Student Name\n'))
    if choice == 1:
        student_number = int(input('Student Number: '))
        for student_data in all_student_data:
            if student_data['ID'] == student_number:
                print(student_data)
                break
            else:
                print('Student data based on the student number was not found')
    elif choice == 2:
        student_name_str = input('Student Name(Full or partial): ')
        for student_data in all_student_data:
            if student_name_str in student_data['Name']:
                print(student_data)

    else:
        print('Wrong option is choose')

def show_grade_search_student():
    grade = input('Enter student to list student: ')
    for student_data in all_student_data:
        if student_data['Grade'] == grade:
            print(student_data)

def remove_student_data():
    global all_student_data
    student_number = int(input('Student Number: '))
    for student_data in all_student_data:
        if student_data['ID'] == student_number:
            all_student_data.remove(student_data)
            print(f'Student data removed with the ID {student_data["ID"]}')


def show_all_student_data():
    with open(file_name, 'rt', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)  # this function is returning a dictionary
        count = 1
        for row in reader:
            print(f'{count}. ID: {row["ID"]}, Name: {row["Name"]}, Unit Mark: {row["UnitMark"]}, Grade: {row["Grade"]}')


def read_all_student_data():
    global all_student_data
    global file_name
    with open(file_name, 'rt', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)  # this function is returning a dictionary
        count = 1
        for row in reader:
            student_data = {}
            student_data['ID'] = int(row['ID'])
            student_data['Name'] = row['Name']
            student_data['UnitMark'] = row['UnitMark']
            student_data['Grade'] = row['Grade']
            all_student_data.append(student_data)
            print(f'{count}. ID: {row["ID"]}, Name: {row["Name"]}, Unit Mark: {row["UnitMark"]}, Grade: {row["Grade"]}')


# file_name = input('Enter the student record file name: ')
file_name = 'all_student_data.csv'
read_all_student_data()

while True:
    choice = int(input('Choose one of the following options(1-5)\n'
                       '1. Add Student\n'
                       '2. Search Student\n'
                       '3. Show Student List Based on Grade\n'
                       '4. Delete Student\n'
                       '5. Show All Student List\n'
                       '6. Exit\n'))

    if choice == 1:
        try:
            add_student_data()
        except ValueError as e:
            print(f'{e}')
        except Exception as e:
            print(f'{e}')
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        show_all_student_data()
    elif choice == 6:
        print('You are exiting from the program.')
        break


