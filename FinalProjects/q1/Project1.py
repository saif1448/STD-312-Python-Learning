
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
        print(all_student_data)
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        print('You are exiting from the program.')
        break


