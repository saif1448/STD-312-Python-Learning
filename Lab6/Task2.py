
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

def is_mark_in_range(mark):
    if not 0 <= mark <= 100:
        return False
    else:
        return True

def print_student_data(student_data):
    print( f'Name: {student_data["Name"]} '
          f'StudentID: {student_data["ID"]} '
          f'\nQ1: {student_data["Q1"]} '
          f'\nQ2: {student_data["Q2"]} '
          f'\nFinal: {student_data["Final"]} '
          f'\nUnitMark: {student_data["UnitMark"]} '
          f'\nGrade: {student_data["Grade"]}')

def take_student_input_data():
    all_student_data = []
    while True:
        student_data = {}
        student_id = int(input('Student ID: '))
        if student_id <= 0:
            break

        if not 1000<=student_id<=2000:
            print("Incorrect Student ID")
            continue

        name = input('Name: ')
        q1 = int(input('Q1: '))
        q2 = int(input('Q2: '))
        final = int(input('Final: '))

        if not (is_mark_in_range(q1) and is_mark_in_range(q2) and is_mark_in_range(final)):
            print('Invalid marks entered. Marks should be in between 0 and 100.')
            continue

        total_mark = q1*0.20 + q2*0.30 + final*0.50
        total_mark = round(total_mark)
        letter_grade = calculate_letter_grade(total_mark)

        student_data['ID'] = student_id
        student_data['Name'] = name
        student_data['Q1'] = q1
        student_data['Q2'] = q2
        student_data['Final'] = final
        student_data['UnitMark'] = total_mark
        student_data['Grade'] = letter_grade

        all_student_data.append(student_data)

    return all_student_data


student_data = take_student_input_data()

for student in student_data:
    print_student_data(student)


# print(student_data)


