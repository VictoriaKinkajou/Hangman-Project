import random

word_list = ['grape', 'mango', 'pear', 'apple', 'strawberry']

word = random.choice(word_list)

guess = input('Enter a letter: ')
print(guess)
if guess.isalpha() and len(guess) == 1:
    print('Good guess!')
else:
    print ('Oops! That is not a valid input')
print(f'your letter: {guess}')
