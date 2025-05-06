class Department:
    def __init__(self, dept_id, dept_name):
        self.dept_id = dept_id
        self.dept_name = dept_name

    def __str__(self):
        return (f"[Department] ID: {self.dept_id}, Name: {self.dept_name}")