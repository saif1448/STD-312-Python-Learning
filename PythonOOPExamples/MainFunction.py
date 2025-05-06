from Student import Student
from Teacher import Teacher
from Department import Department
from Course import Course

cse_dept = Department(dept_name="CSE", dept_id="0101")

cse_teacher_1 = Teacher(teacher_id=1001, teacher_dept=cse_dept, teacher_add="kajsd, asd", teacher_name="ABCD", teacher_schedule=None, teacher_contact_number="0191")

basic_python = Course(course_name="Basic Python", course_id="CSPY0101", course_credit=1.5, course_coordinator=cse_teacher_1, course_fees=2000, course_duration=4)

std_1 = Student(id="CS10101", department=cse_dept, add="qweqwe, qwe", name="PQYR", grade=None, contact_number="0123")


print(std_1)