import argparse
parser = argparse.ArgumentParser(description="Takes an input and determines if it is even or odd")

parser.add_argument("num_in", type = int, help = 'Enter an Integer')
parser.add_argument("name", type = str, help = 'Enter your name')
argument = parser.parse_args()
num1 = argument.num_in
person1 = argument.name

if num1%2==0:
    print(f'{person1}, your input, {num1}, is even') #just a comment

else:
    print(f'{person1},your input, {num1}, is odd')