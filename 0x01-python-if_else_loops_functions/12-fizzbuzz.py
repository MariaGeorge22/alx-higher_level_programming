#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        printed = i
        if i % 3 == 0 and i % 5 == 0:
            printed = 'FizzBuzz'
        elif i % 3 == 0:
            printed = 'Fizz'
        elif i % 5 == 0:
            printed = 'Buzz'
        print('{}'.format(printed), end=" ")
