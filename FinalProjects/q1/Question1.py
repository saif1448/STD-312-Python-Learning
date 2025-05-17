
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

def add_student_data():
    global all_student_data
    student_data = {}
    student_number = int(input('Student Number: '))
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

    all_student_data.append(student_data)


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

while True:
    choice = int(input('Choose one of the following options(1-5)\n'
                       '1. Add Student\n'
                       '2. Search Student\n'
                       '3. Show Student List Based on Grade\n'
                       '4. Delete Student\n'
                       '5. Exit\n'))

    if choice == 1:
        try:
            add_student_data()
        except ValueError as e:
            print(f'{e}')
    elif choice == 2:
        search_student_data()
    elif choice == 3:
        show_grade_search_student()
    elif choice == 4:
        remove_student_data()
    elif choice == 5:
        print('You are exiting from the program.')
        break


