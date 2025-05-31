#Defines a class: State (variables) and behaviors (functions or methods)
from student import participant


class HumanBeing:
    def __init__(self,name:str,age:int,nationality:str, kids:list=[], attendance:set={}):
        print('Constructor called')
        self.name = name
        self.age = age
        self.nationality = nationality
        self.kids = kids
        self.attendance = attendance

    def introduce(self):
        print(f'Hello, my name is {self.name}')
        print(f'I am {self.age} years old')
        print(f'I am from {self.nationality}')
        print('***************')

    def __add__(self, other):
        return self.age + other.age

    #Static Method
    def increase_age(self, years_in:int):
        self.age +=years_in
        print(f"{years_in} years from now, {self.name} will be {self.age} years old.")

    def decrease_age(self, years_in: int):
        self.age -= years_in
        print(f"{years_in} years ago, {self.name} was {self.age} years old.")

    #Getter Methods
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

#Defnining an object of the class
person1 = HumanBeing('Epie', 30, 'Cameroon')
person2 = HumanBeing('Marvin', 25, 'Kenya')


#Calling the method of the class using the object
person1.introduce()
person2.introduce()
print(person1 + person2)
print(person1.age)
print(person1.get_name())
print(person1.increase_age(5))
print(person1.decrease_age(5))
HumanBeing.decrease_age(8)