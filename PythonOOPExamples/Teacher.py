from Department import Department

class Teacher:
    def __init__(self, teacher_id, teacher_name, teacher_contact_number, teacher_add, teacher_dept, teacher_schedule):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.teacher_contact_number = teacher_contact_number
        self.teacher_add = teacher_add
        self.teacher_dept = teacher_dept
        self.teacher_schedule = teacher_schedule

    def __str__(self):
        dept_name = self.teacher_dept.dept_name if isinstance(self.teacher_dept, Department) else self.teacher_dept
        return (f"[Teacher] ID: {self.teacher_id}, Name: {self.teacher_name}, "
                f"Contact: {self.teacher_contact_number}, Address: {self.teacher_add}, "
                f"Department: {dept_name}, Schedule: {self.teacher_schedule}")