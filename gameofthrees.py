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