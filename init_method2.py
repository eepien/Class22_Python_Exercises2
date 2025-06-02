class Person:
    name = ""
    def __init__(self, name = "I have no name"):
        self.name = name

def main():
    smiley = Person()
    print("My name is ...", smiley.name)
    jt = Person ('James')
    print("My name is ...", jt.name)

main() #runs the main program defined above