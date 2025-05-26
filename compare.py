from operator import truediv
from selectors import SelectSelector

#number = input("Enter a number:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = enumerate(numbers)
for count,number in numbers:
    print(number, count)
    number = int(number)
    if number%2 == 0:
        print(f'{number}, is even')
    else:
        print(f'{number} is odd')



