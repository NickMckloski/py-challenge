'''
The input is a single number: the number at which the game starts. Write a program that plays the Threes game, and
outputs a valid sequence of steps you need to take to get to 1. Each step should be output as the number you start at,
followed by either -1 or 1 (if you are adding/subtracting 1 before dividing), or 0 (if you are just dividing). The
last line should simply be 1.
'''

##Solution:

number = int(input("Enter a number to begin: "))

def divide():
    global number
    if number % 3 == 0:
        print(number, ' ', 0)
        number /= 3
    else:
        if (number + 1) % 3 == 0:
            print(number, ' ', '+1')
            number = (number + 1) / 3
        else:
            print(number, ' ', '-1')
            number = (number - 1) / 3

while number > 1:
    divide()

print(number)