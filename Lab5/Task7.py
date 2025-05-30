
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

def take_student_input_data():
    all_student_data = []
    while True:
        student_data = []
        student_id = int(input('Student ID: '))
        if student_id <= 0:
            break
        q1 = int(input('Q1: '))
        q2 = int(input('Q2: '))
        final = int(input('Final: '))

        if not (is_mark_in_range(q1) and is_mark_in_range(q2) and is_mark_in_range(final)):
            print('Invalid marks entered. Marks should be in between 0 and 100.')
            continue

        total_mark = q1*0.20 + q2*0.30 + final*0.50
        total_mark = round(total_mark)
        letter_grade = calculate_letter_grade(total_mark)
        student_data.append(student_id)
        student_data.append(q1)
        student_data.append(q2)
        student_data.append(final)
        student_data.append(total_mark)
        student_data.append(letter_grade)

        all_student_data.append(student_data)

    return all_student_data


student_data = take_student_input_data()

print(student_data)


