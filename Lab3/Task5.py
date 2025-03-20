
total_marks = 0
all_mark_count = 0
hd_grade_mark_count = 0
d_grade_mark_count = 0
c_grade_mark_count = 0
p_grade_mark_count = 0
n_grade_mark_count = 0
fail_std_percentage = 0.0

# first we need to calculate the sum of all the entered marks
# 2nd, we need to count how many marks are given as input
# we need to count individual counting of HD, D, C, P and N grades
# finally, we need to find the percentile of failed students

while True:
    mark = input("Enter mark: ")
    if mark == "end":
        break
    mark_num = float(mark)
    all_mark_count += 1

    #total_mark = 0
    # mark_num = 5
    # total_mark = total_mark + mark_num ----> short hand/ assignment operator ---> total_mark += mark_num
    # total_mark = 0 + 5 = 5

    #total_mark = 5
    #mark_num = 10
    #total_mark = total_mark + mark_num = 5 + 10 =  15

    #total_mark = 15
    #mark_num = 8
    #total_mark = 15 + 8 = 23
    total_marks += mark_num

    #this condition is for HD_grade
    if mark_num >= 80:
        hd_grade_mark_count += 1
    #this condition is for D grde
    elif mark_num >= 70:
        d_grade_mark_count += 1
    #this condition is for C grade
    elif mark_num >= 60:
        c_grade_mark_count += 1
    #this condition is for P grade
    elif mark_num >= 50:
        p_grade_mark_count += 1
    #the else is for the F grade
    else:
        n_grade_mark_count += 1


fail_std_percentage = n_grade_mark_count/total_marks*100

print(f"Total students counting {all_mark_count}")
# print(f"All mark sum {total_marks}")
print(f"The number of HD grade students: {hd_grade_mark_count}")
print(f"The number of D grade students: {d_grade_mark_count}")
print(f"The number of C grade students: {c_grade_mark_count}")
print(f"The number of P grade students: {p_grade_mark_count}")
print(f"The number of N grade students: {n_grade_mark_count}")


print(f"{fail_std_percentage:.1f}% of students failed the unit")


# total_student_count = 78
#
# failed_student_percentile = 39.1123123
#
# # The total number of students is 78 among them 39.1% have been failed
#
# output_str = f"The total number of students is {total_student_count} among them {failed_student_percentile:.1f} have been failed"
#
# print(output_str)