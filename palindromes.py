'''
Write a program that detects whether or not a particular input is a valid palindrome.
'''

# Solution:

string = input("Enter a string to check: ")

palindrome = True
for i, char in list(enumerate(string[::-1])):
    print(i, char, string[i])
    if not char == string[i]:
        palindrome = False

print('Palindrome: ', palindrome)

