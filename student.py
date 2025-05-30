class student:
    def __init__(self, name,id, marks):
        self.name = name
        self.id = id
        self.marks = marks

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"My student id is {self.id}")
        print(f"My score is {self.marks}")

participant = student("Marvin", "123AB", 20)

participant.introduce()