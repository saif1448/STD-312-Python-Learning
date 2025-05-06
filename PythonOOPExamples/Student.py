
class Student:

    # constructor
    def __init__(self, id, name, add, contact_number, grade, department):
        self.id = id  # property fields ---> instance variable
        self.name = name
        self.add = add
        self.contact_number = contact_number
        self.grade = grade
        self.department = department

    #to string method
    def __str__(self):
        return f"name: {self.name}\nid: {self.id}\ngrade: {self.grade}\ndepartment: {self.department} "

    def check_if_honored_student(self):
        if self.grade == "HD":
            print("Honored")
        else:
            print("Not Honored")
