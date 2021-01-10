class School:
    def __init__(self):
        self.schooling = dict()

    def add_student(self, name, grade):
        self.schooling[name] = grade

    def roster(self):
        return [k for k, v in sorted(self.schooling.items(), key=lambda x: (x[1],x[0]))]

    def grade(self, grade_number):
        return [k for k, v in sorted(self.schooling.items(), key=lambda x: x[0]) if v is grade_number]