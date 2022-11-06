DEFAULT_STUDENTS = 'Alice, Bob, Charlie, David, Eve, Fred, Ginny, Harriet, Ileana, Joseph, Kincaid, Larry'.split(', ')
PLANTS = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

class Garden:
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.garden = diagram.split('\n')
        self.students = sorted(students)
        
    def plants(self, student):
        start_pos = self.students.index(student) * 2
        letters = ''.join([self.garden[i][start_pos:start_pos+2] for i in range(2)])
        return [PLANTS[l] for l in letters]