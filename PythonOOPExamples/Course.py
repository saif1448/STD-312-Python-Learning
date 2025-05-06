from Teacher import Teacher
class Course:
    def __init__(self, course_id, course_name, course_coordinator, course_duration, course_credit, course_fees):
        self.course_id = course_id
        self.course_name = course_name
        self.course_coordinator = course_coordinator
        self.course_duration = course_duration
        self.course_credit = course_credit
        self.course_fees = course_fees

    def __str__(self):
        coordinator_name = self.course_coordinator.teacher_name if isinstance(self.course_coordinator,
                                                                              Teacher) else self.course_coordinator
        return (f"[Course] ID: {self.course_id}, Name: {self.course_name}, "
                f"Coordinator: {coordinator_name}, Duration: {self.course_duration}, "
                f"Credit: {self.course_credit}, Fees: {self.course_fees}")