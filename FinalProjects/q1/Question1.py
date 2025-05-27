all_student_data = []


def calculate_letter_grade(total_mark):
    """
    Converts a numeric mark to a letter grade based on Murdoch University's grading system.

    Parameters:
    - total_mark (int): Student's numeric mark (0-100)

    Returns:
    - str: Letter grade (HD, D, C, P, or F)

    Grade Boundaries:
    - HD (High Distinction): >= 80
    - D (Distinction): 70-79
    - C (Credit): 60-69
    - P (Pass): 50-59
    - F (Fail): < 50
    """
    if total_mark >= 80:
        return 'HD'
    elif total_mark >= 70:
        return 'D'
    elif total_mark >= 60:
        return 'C'
    elif total_mark >= 50:
        return 'P'
    else:
        return 'N'


def add_student_data():
    """
    Adds a new student record to the system.

    Input Requirements:
    - Student Number (int): Positive integer
    - Name (str): Student's full name
    - Unit Mark (int): 0-100

    Validation:
    - Checks if student number is positive
    - Validates unit mark range (0-100)

    Throws:
    - ValueError: If input validation fails
    """
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
    """
    Searches for student records using two methods:
    1. By student number (exact match)
    2. By name (partial match)

    Features:
    - Case-sensitive name search
    - Displays full record if found
    """
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
            if student_name_str.lower() in student_data['Name'].lower():
                print(student_data)

    else:
        print('Wrong option is choose')


def show_grade_search_student():
    """
    Lists all students with a specific grade.

    Input:
    - Grade (str): HD, D, C, P, or F

    Output:
    - Displays all matching student records
    """
    grade = input('Enter student to list student: ')
    for student_data in all_student_data:
        if student_data['Grade'] == grade:
            print(student_data)


def remove_student_data():
    """
    Removes a student record based on student number.

    Input:
    - Student Number (int)

    Output:
    - Confirmation message if record is deleted
    """
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
