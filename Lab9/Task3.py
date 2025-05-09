
class Student:
    def __init__(self, name, mark_list):
        self.name = name
        self.mark_list = mark_list

    def addMark(self, mark):
        self.mark_list.append(mark)

    def average(self):
        mark_list_len = len(self.mark_list)
        all_mark_sum = sum(self.mark_list)
        return all_mark_sum/mark_list_len

    def get_letter_grade(self, mark):
        if mark >= 80:
            return 'HD'
        elif mark >= 70:
            return 'D'
        elif mark >= 60:
            return 'C'
        elif mark >= 50:
            return 'P'
        else:
            return 'F'

    def getGrades(self):
        # grades = []
        # for mark in self.mark_list:
        #     grade = self.get_letter_grade(mark)
        #     grades.append(grade)
        grades = [self.get_letter_grade(mark) for mark in self.mark_list]
        return grades

    def __str__(self):
        return f"Name: {self.name}\nAverage Mark: {self.average():.2f}\nGrades: {self.getGrades()}"


std_1 = Student('ABCD', [80,50,74,90])

std_2 = Student('PQRS', [70,40,80,55])

std_1.addMark(60)
std_1.addMark(77)
std_1.addMark(47)

std_2.addMark(87)
std_2.addMark(38)
std_2.addMark(69)

print(std_1)
print(std_2)


