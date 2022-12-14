import random

word_list = ['grape', 'mango', 'pear', 'apple', 'strawberry']

word = random.choice(word_list)

def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f'{guess} is in the word')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')


def ask_for_input():
    while True:
        guess = input('Enter a letter: ')
        if guess.isalpha() and len(guess) == 1:
            print(f'{guess} Good guess!')
            break
        else:
            print ('Invalid letter. Please enter a single alphabetical character.')
    check_guess(guess)

ask_for_input()

