class Human:
    def __init__(self, name, age, id_num):
        self.name = name
        self.age = age
        self.id_num = id_num

    def breath(self):
        print(f'{self.name} is breathing...')
    def run(self):
        print(f'{self.name} is running')
    def walk(self):
        print(f'{self.name} is walking...')
    def eat(self):
        print(f'{self.name} is eating...')

class Student(Human):
    def __init__(self, name, degree_pgm, dept, age, id_num):
        super().__init__(name, age, id_num)
        self.name = name
        self.degree_pgm = degree_pgm
        self.dept = dept
    def listen(self):
        print(f'Student {self.name} is listening to lectures...')
    def question(self):
        print(f'Student {self.name} is asking a question...')

class Instructor(Human):
    def teach(self):
        print(f'Instructor {self.name} is teaching student ...')
    def grade(self):
        print(f'Instructor {self.name} is grading assignments...')


stud1=Student('Epie', 'BSc', "CSC", 32, 'CSC123')
stud1.breath()
stud1.listen()
stud1.question()

inst1 = Instructor('Einstein', 55, '576AZ')
inst1.eat()
inst1.teach()
inst1.grade()
