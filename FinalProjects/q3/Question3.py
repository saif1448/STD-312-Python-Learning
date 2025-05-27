import csv
import os
import operator
import numpy as np
import matplotlib.pyplot as plt

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
        return 'N'


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
        # this function is returning a dictionary
        reader = csv.DictReader(csvfile)
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

    # write_std_record_to_file(student_data)
    check_file = check_std_record_on_file(student_number)

    if not check_file:
        print('Student Record Was not Written on the CSV File!')
        choice = int(input('Choose one of the following:\n '
                           '1. Cancel Operation\n'
                           '2. Continue Operation\n'
                           '3. Exit Program\n'
                           ))
        if choice == 1:
            pass
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
    count = 1
    for std in all_student_data:
        print(f'{count}. {std}')
        count += 1


def read_all_student_data():
    global all_student_data
    with open(file_name, 'rt', newline='', encoding='utf-8-sig') as csvfile:
        # this function is returning a dictionary
        reader = csv.DictReader(csvfile)
        count = 1
        for row in reader:
            student_data = {}
            student_data['ID'] = int(row['ID'])
            student_data['Name'] = row['Name']
            student_data['UnitMark'] = int(row['UnitMark'])
            student_data['Grade'] = row['Grade']
            all_student_data.append(student_data)
            print(
                f'{count}. ID: {row["ID"]}, Name: {row["Name"]}, Unit Mark: {row["UnitMark"]}, Grade: {row["Grade"]}')
            count += 1


def update_student():
    global all_student_data
    student_number = int(input('Student Number: '))
    is_std_found = False
    for i, std in enumerate(all_student_data):
        if student_number == int(std['ID']):
            is_std_found = True
            print(f'Current Student with ID:{student_number} is :--> {std}')
            choice = int(input('Choose one of the following:\n'
                               '1. Update Student Name\n'
                               '2. Update Student Mark\n'
                               '3. Cancel Operation\n'))  # we are performing this task extra

            if choice == 1:
                updated_name = input('Enter Updated Name: ')
                all_student_data[i]['Name'] = updated_name
            elif choice == 2:
                updated_mark = int(input('Enter Updated Mark: '))
                all_student_data[i]['UnitMark'] = updated_mark
                # if mark is changed, the grade will be changed also.
                updated_grade = calculate_letter_grade(updated_mark)
                all_student_data[i]['Grade'] = updated_grade
            elif choice == 3:
                break
            else:
                print("Wrong option is chosen! Try again!")
            break
    if not is_std_found:
        print(
            f'Student Data Not Found to be updated with ID:{student_number}!')


def write_all_std_data_to_file(write_file_path):
    with open(write_file_path, 'wt', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[
                                'ID', 'Name', 'UnitMark', 'Grade'])
        writer.writeheader()
        for std in all_student_data:
            writer.writerow(std)


def save_std_data_to_file():
    save_file_path = input('Enter the file path to save all student data: ')

    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_file_dir, save_file_path)

    if os.path.exists(file_path):
        print(f'There already a file exists with name {save_file_path}')
        choice = int(input('Choose one of the following:\n'
                           '1. Change file name\n'
                           '2. Overwrite existing file\n'
                           '3. Cancel Operation\n'))
        if choice == 1:
            save_file_path = input('Enter the new file path: ')
            write_all_std_data_to_file(save_file_path)
        elif choice == 2:
            write_all_std_data_to_file(save_file_path)
        elif choice == 3:
            pass
        else:
            print('Wrong option is chosen! Try again!')
    else:
        write_all_std_data_to_file(save_file_path)


def show_top_10_perc():
    """
    Identifies and returns names of top 10% performing students.

    Implementation:
    - Uses numpy percentile calculation
    - Handles ties at the cutoff point
    - Includes all students at the 90th percentile mark

    Returns:
        list: Names of students in top 10% by mark
    """
    all_std_marks = np.array([std['UnitMark'] for std in all_student_data])

    percentile_threshold = np.percentile(all_std_marks, 90)

    top_std_10_names = [std['Name']
                        for std in all_student_data if std['UnitMark'] >= percentile_threshold]

    return top_std_10_names


def show_bottom_10_perc():
    """
    Identifies and returns names of bottom 10% performing students.

    Implementation:
    - Uses numpy percentile calculation
    - Handles ties at the cutoff point
    - Includes all students at the 10th percentile mark

    Returns:
        list: Names of students in bottom 10% by mark
    """
    all_std_marks = np.array([std['UnitMark'] for std in all_student_data])

    percentile_threshold = np.percentile(all_std_marks, 10)

    bottom_10_std_names = [
        std['Name'] for std in all_student_data if std['UnitMark'] <= percentile_threshold]

    return bottom_10_std_names


def show_mark_bar_chart():
    """
    Displays bar chart of student mark distribution.

    Features:
    - Mark ranges: 0-44, 45-49, 50-59, 60-69, 70-79, 80-89, 90-100
    - Shows count of students in each range
    - Includes:
        * Title
        * Labeled axes
        * Value labels on bars
        * Grid lines for readability
    """
    all_std_marks = np.array([std['UnitMark'] for std in all_student_data])
    mark_range = ["0-44", "45-49", "50-59",
                  "60-69", "70-79", "80-89", "90-100"]

    range_count = [
        np.sum((all_std_marks >= 0) & (all_std_marks <= 44)),
        np.sum((all_std_marks >= 45) & (all_std_marks <= 49)),
        np.sum((all_std_marks >= 50) & (all_std_marks <= 59)),
        np.sum((all_std_marks >= 60) & (all_std_marks <= 69)),
        np.sum((all_std_marks >= 70) & (all_std_marks <= 79)),
        np.sum((all_std_marks >= 80) & (all_std_marks <= 89)),
        np.sum((all_std_marks >= 90) & (all_std_marks <= 100)),
    ]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(mark_range, range_count, color='#90EE90', edgecolor='black')
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height,  # x, y position
                 str(height),  # text to show
                 ha='center', va='bottom')
    plt.title("Student Marks Distribution by Mark Bracket")
    plt.xlabel("Mark Brackets")
    plt.ylabel("Number of Students")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def show_grade_pie_chart():
    """
    Displays pie chart of grade distribution.

    Features:
    - Shows distribution of grades (HD, D, C, P, F)
    - Includes:
        * Percentage labels
        * Color coding
        * Title
        * Legend
    - Calculates percentages based on total enrollment
    """
    grade_list = ['HD', 'D', 'C', 'P', 'N']
    grade_std_count = [0, 0, 0, 0, 0]
    for std in all_student_data:
        if std['Grade'] == 'HD':
            grade_std_count[0] += 1
        elif std['Grade'] == 'D':
            grade_std_count[1] += 1
        elif std['Grade'] == 'C':
            grade_std_count[2] += 1
        elif std['Grade'] == 'P':
            grade_std_count[3] += 1
        else:
            grade_std_count[4] += 1

    total_student = len(all_student_data)

    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

    plt.figure(figsize=(8, 5))
    plt.pie(x=grade_std_count, labels=grade_list,
            startangle=90, autopct='%1.0f%%', colors=colors)
    plt.title('Student Grade Distribution')
    plt.show()


# must give the correct file name here
file_name = input('Enter the student record file name: ')
# file_name = 'std_data.csv'
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
                           '8. Show Top 10% Student Names\n'
                           '9. Show Bottom 10% Student Names\n'
                           '10. Show Student Marks Bar Chart\n'
                           '11. Show Student Grade Pie Chart\n'
                           '12. Exit\n'))

        if choice == 1:
            try:
                add_student_data()
            except ValueError as e:
                print(f'{e}')
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
            top_10_names = show_top_10_perc()
            print("*" * 20)
            print("Top 10% Student Names:")
            print("-" * 20)
            for i, name in enumerate(top_10_names):
                print(f'{i + 1}. {name}')
            print("*" * 20)
        elif choice == 9:
            print("*" * 20)
            print("Bottom 10% Student Names:")
            print("-" * 20)
            bottom_10_names = show_bottom_10_perc()
            for i, name in enumerate(bottom_10_names):
                print(f'{i + 1}. {name}')
            print("*" * 20)
        elif choice == 10:
            show_mark_bar_chart()
        elif choice == 11:
            show_grade_pie_chart()
        elif choice == 12:
            print('You are exiting from the program.')
            break

except FileNotFoundError as e:
    print(e)
