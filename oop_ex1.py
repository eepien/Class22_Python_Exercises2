#Defines a class: State (variables) and behaviors (functions or methods)
class HumanBeing:
    def __init__(self,name,age,nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def introduce(self):
        print(f'Hello, my name is {self.name}')
        print(f'I am {self.age} years old')
        print(f'I am from {self.nationality}')
        print('***************')

#Defnining an object of the class
person1 = HumanBeing('Epie', 30, 'Cameroon')
person2 = HumanBeing('Marvin', 25, 'Kenya')

#Calling the method of the class using the object
person1.introduce()
person2.introduce()