'''
You are to write a function that displays the numbers from 1 to an input parameter n, one per line,
except that if the current number is divisible by 3 the function should write “Fizz” instead of the number,
if the current number is divisible by 5 the function should write “Buzz” instead of the number, and if the
current number is divisible by both 3 and 5 the function should write “FizzBuzz” instead of the number.
'''

# Solution:

n = int(input("Enter a number to stop at: "))

for i in range(1, n):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

