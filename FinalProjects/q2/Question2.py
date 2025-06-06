"""
Student Record Management System (Question 2 Implementation)

This program implements a student record management system with file I/O capabilities.
Key Features:
1. Load student records from CSV file at startup
2. Maintain unique student numbers (no duplicates allowed)
3. Add new student records with validation
4. Update existing student records
5. Search students by number or name (partial match supported)
6. Display students by grade
7. Delete student records
8. Save records to CSV with file handling options

File Operations:
- Input: Reads initial student data from user-specified CSV file
- Output: Saves to CSV with options to:
    * Change filename if exists
    * Overwrite existing file
    * Cancel operation

Data Structure:
- Student records stored as dictionaries with fields:
    * Student_Number: Unique student number (integer)
    * Name: Student's full name (string)
    * UnitMark: Numeric mark 0-100 (integer)
    * Grade: Letter grade HD, D, C, P, F (string)

Required format for CSV files:
- Headers: Student_Number,Name,UnitMark,Grade
- Encoding: UTF-8 with BOM
"""

import csv
import os

all_student_data = []


def calculate_letter_grade(total_mark):
    """
    Converts numeric mark to Murdoch University grade letter.

    Parameters:
        total_mark (int): Student's numeric mark (0-100)

    Returns:
        str: Letter grade (HD, D, C, P, or F)
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


def check_duplicate_student_number(student_number):
    """
    Validates uniqueness of student numbers.

    Parameters:
    - student_number (int): Student Student_Number to check

    Returns:
    - bool: True if duplicate exists, False otherwise
    """
    for std in all_student_data:
        if std['Student_Number'] == student_number:
            return True
    return False


def write_std_record_to_file(std):
    with open(file_name, "a", newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['Student_Number', 'Name', 'UnitMark', 'Grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(std)


def check_std_record_on_file(student_number):
    with open(file_name, 'rt', newline='', encoding='utf-8-sig') as csvfile:
        # this function is returning a dictionary
        reader = csv.DictReader(csvfile)
        is_present = False
        for row in reader:
            if int(row['Student_Number']) == student_number:
                is_present = True
                break
        return is_present


def add_student_data():
    """
    Adds a new student record with duplicate checking.

    Features:
    - Validates student number uniqueness
    - Validates mark range (0-100)
    - Calculates grade automatically
    - Handles file write failures with options:
        1. Cancel operation
        2. Continue without saving
        3. Exit program

    Raises:
        ValueError: If student number <= 0 or mark not in 0-100
        Exception: If student number already exists
    """
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

    student_data['Student_Number'] = student_number
    student_data['Name'] = name
    student_data['UnitMark'] = unitMark
    student_data['Grade'] = letter_grade

    # write_std_record_to_file(student_data)
    check_file = check_std_record_on_file(student_number)
    print('Student Record Was not Written on the CSV File::')
    if not check_file:

        choice = int(input('Choose one of the following:\n'
                           '1. Cancel Operation\n'
                           '2. Continue Operation\n'
                           '3. Exit Program\n'
                           ))
        if choice == 1:
            print("The student record is not stored. Cancelling operation.")
        elif choice == 2:
            all_student_data.append(student_data)
        elif choice == 3:
            print('Exiting Program...')
            exit()
        else:
            print('Wrong option is chosen! Try again!')


def search_student_data():
    choice = int(input('Choose the search option: \n'
                       '1. Based on Student Number\n'
                       '2. Based on Student Name\n'))
    if choice == 1:
        student_number = int(input('Student Number: '))
        student_found = False
        for student_data in all_student_data:
            if student_data['Student_Number'] == student_number:
                student_found = True
                print(student_data)
                break
        if not student_found:
            print(f'Student data is not found for {student_number}!')

    elif choice == 2:
        student_name_str = input('Student Name(Full or partial): ')
        student_found = False
        for student_data in all_student_data:
            if student_name_str.lower() in student_data['Name'].lower():
                print(student_data)
                student_found = True

        if not student_found:
            print(f'Student was not found with given string {student_name_str}')

    else:
        print('Wrong option is choose')


def show_grade_search_student():
    """
    Lists all students with a specific grade.

    Input:
    - Grade (str): HD, D, C, P, or N

    Output:
    - Displays all matching student records
    """
    grade = input('Enter Grade Choice(HD, D, C, P, or N) to Filter Students Based on Grade: ')
    is_found = False
    for student_data in all_student_data:
        if student_data['Grade'] == grade:
            is_found = True
            print(student_data)
    if not is_found:
        print(f'No student is found for {grade}')


def remove_student_data():
    global all_student_data
    student_number = int(input('Student Number: '))
    for student_data in all_student_data:
        if student_data['Student_Number'] == student_number:
            all_student_data.remove(student_data)
            print(f'Student data removed with the Student_Number {student_data["Student_Number"]}')


def show_all_student_data():
    count = 1
    for std in all_student_data:
        print(f'{count}. {std}')
        count += 1


def read_all_student_data():
    """
    Loads initial student data from CSV file.

    Features:
    - Reads and validates CSV format
    - Converts string data to appropriate types
    - Stores records in memory for program operations
    - Displays loaded records with running count

    Required CSV format:
    - Headers: Student_Number,Name,UnitMark,Grade
    - Encoding: UTF-8 with BOM
    """
    global all_student_data
    with open(file_name, 'rt', newline='', encoding='utf-8-sig') as csvfile:
        # this function is returning a dictionary
        reader = csv.DictReader(csvfile)
        count = 1
        for row in reader:
            student_data = {}
            student_data['Student_Number'] = int(row['Student_Number'])
            student_data['Name'] = row['Name']
            student_data['UnitMark'] = int(row['UnitMark'])
            student_data['Grade'] = row['Grade']
            all_student_data.append(student_data)
            print(
                f'{count}. Student_Number: {row["Student_Number"]}, Name: {row["Name"]}, Unit Mark: {row["UnitMark"]}, Grade: {row["Grade"]}')


def update_student():
    """
    Updates existing student record by Student_Number.

    Features:
    - Allows updating name or mark separately
    - Recalculates grade if mark is changed
    - Validates input mark range
    - Provides option to cancel operation

    Display: Shows current record before update
    """
    global all_student_data
    student_number = int(input('Student Number: '))
    is_std_found = False
    for i, std in enumerate(all_student_data):
        if student_number == int(std['Student_Number']):
            is_std_found = True
            print(f'Current Student with Student_Number:{student_number} is :--> {std}')
            choice = int(input('Choose one of the following:\n'
                               '1. Update Student Name\n'
                               '2. Update Student Mark\n'
                               '3. Cancel Operation\n'))  # we are performing this task extra

            if choice == 1:
                updated_name = input('Enter Updated Name: ')
                all_student_data[i]['Name'] = updated_name
                print(f"Student Name Update for the student with Student Number:{all_student_data[i]['Student_Number']}")
            elif choice == 2:
                updated_mark = int(input('Enter Updated Mark: '))
                all_student_data[i]['UnitMark'] = updated_mark
                # if mark is changed, the grade will be changed also.
                updated_grade = calculate_letter_grade(updated_mark)
                all_student_data[i]['Grade'] = updated_grade
                print(f"Student Mark Update for the student with Student Number:{all_student_data[i]['Student_Number']}")
            elif choice == 3:
                print("Update Operation Cancelled!")
            else:
                print("Wrong option is chosen! Try again!")
            break
    if not is_std_found:
        print(
            f'Student Data Not Found to be updated with Student_Number:{student_number}!')


def write_all_std_data_to_file(write_file_path):
    with open(write_file_path, 'wt', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[
                                'Student_Number', 'Name', 'UnitMark', 'Grade'])
        writer.writeheader()
        for std in all_student_data:
            writer.writerow(std)


def save_std_data_to_file():
    """
    Saves all student records to CSV file.

    Features:
    - User specifies output filename/path
    - Handles existing file conflicts with options:
        1. Change filename
        2. Overwrite existing file
        3. Cancel operation
    - Preserves all record fields in CSV format
    """
    save_file_path = input('Enter the file name to save all student data: ')

    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_file_dir, save_file_path)

    if os.path.exists(file_path):
        print(f'There already a file exists with name {save_file_path}')
        choice = int(input('Choose one of the following:\n'
                           '1. Change file name\n'
                           '2. Overwrite existing file\n'
                           '3. Cancel Operation\n'))
        if choice == 1:
            save_file_path = input('Enter the new file name: ')
            write_all_std_data_to_file(save_file_path)
            print(f'Student Data has been saved to file with name {save_file_path}.csv')
        elif choice == 2:
            write_all_std_data_to_file(save_file_path)
            print(f'Student Data has been saved and overwritten to the file with name {save_file_path}.csv')
        elif choice == 3:
            print("File operation cancelled!")
        else:
            print('Wrong option is chosen! Try again!')
    else:
        write_all_std_data_to_file(save_file_path)


# must give the correct file name here
file_name = input('Enter the student record file name: ')

try:
    read_all_student_data()
    while True:
        choice = int(input('Choose one of the following options(1-5)\n'
                           '1. Add Student\n'
                           '2. Search Student\n'
                           '3. Show Student List Based on Grade\n'
                           '4. Delete Student\n'
                           '5. Update Student\n'
                           '6. Save All Student Data to File\n'
                           '7. Show All Student List\n'
                           '8. Exit\n'))

        if choice == 1:
            try:
                add_student_data()
            except ValueError as e:
                print(f'{e}')
                print('Student Number is not Valid')
            except Exception as e:
                print(f'{e}')
        elif choice == 2:
            search_student_data()
        elif choice == 3:
            show_grade_search_student()
        elif choice == 4:
            remove_student_data()
        elif choice == 5:
            update_student()
        elif choice == 6:
            save_std_data_to_file()
        elif choice == 7:
            show_all_student_data()
        elif choice == 8:
            print('You are exiting from the program.')
            break

except FileNotFoundError  as e:
    print(e.strerror)