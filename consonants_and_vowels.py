'''
Your task is to create a program that generates a random word given a pattern of consonants (c) and vowels (v).
Input Description:
Any string of the letters c and v, uppercase or lowercase.
Output Description:
A random lowercase string of letters in which consonants (bcdfghjklmnpqrstvwxyz) occupy the given 'c' indices and vowels (aeiou) occupy the given 'v' indices.
'''

# Solution:

import random

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

def main():
    string = input('Enter a string of c\'s, v\'s, C\'s, or V\'s: ')
    good = set('cvCV')
    if set(string) <= good:
        new_string = []
        for char in string:
            if char == 'c' or char == 'v':
                new_string.append(random.choice(consonants))
            if char == 'C' or char == 'V':
                new_string.append(random.choice(vowels).upper())
        print(''.join(new_string))
    else:
        print('entered string not valid')

if __name__ == "__main__":
    main()
