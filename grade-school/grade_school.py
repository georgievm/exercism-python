class School:
    def __init__(self):
        self.register = {}
        self.add_history = []

    def add_student(self, name, grade):
        if result := (name not in self.get_names()):
            if self.register.get(grade):
                self.register[grade].append(name)
                self.register[grade].sort()
            else:
                self.register[grade] = [name]
        self.add_history.append(result)

    def roster(self):
        return [name for key in sorted(self.register) for name in self.register[key]]
    
    def grade(self, grade_number):
        return self.register.get(grade_number, [])

    def added(self):
        return self.add_history

    def get_names(self):
        return [j for i in self.register.values() for j in i]
