from math import inf

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


def get_student_statics(student_data):
    avg_mark = 0
    sum_mark = 0
    student_count = len(student_data)
    failed_std_count = 0
    highest_mark = -inf
    lowest_mark = inf

    for student in student_data:
        mark = student[4]
        grade = student[5]
        sum_mark += mark
        if mark > highest_mark:
            highest_mark = mark
        if mark < lowest_mark:
            lowest_mark = mark

        if grade == 'F':
            failed_std_count += 1

    avg_mark = sum_mark / student_count
    return (avg_mark, highest_mark, lowest_mark, failed_std_count)

student_data = take_student_input_data()

avg_mark, highest_mark, lowest_mark, failed_std_count = get_student_statics(student_data)

student_grades = [(std[0],std[5]) for std in student_data]
#[(1001, 'P'), (1002, 'HD'), (1003, 'F')]
hd_grade_list = [std_id for std_id,grade in student_grades if grade == 'HD']

print(student_data)
print(f"Highest Mark: {highest_mark}, Lowest Mark: {lowest_mark}, Avg Mark: {avg_mark:.2f}")
print(f"Failed Student Count: {failed_std_count}")
print(f"HD Grade List: {hd_grade_list}")

# ls = []
# for std_id, std_grade in student_grades:
#     if std_grade == 'HD':
#         ls.append(std_id)