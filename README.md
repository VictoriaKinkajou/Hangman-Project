# Hangman-Project

This is the first project for my AiCore data science course.

### About the game
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### Milestone_1

The code in this milestone:
- defines the list of possible words for the game 
- randomly selects a word from the list
- prompts the user to enter a letter 
- checks that the input is a single letter

Uses Python3, importing random for word selection.

### Milestone_2

In this milestone, I have defined the functions ask_for_input and check_guess.
ask_for_input asks the user to guess a letter and checks that the input is valid.
check_guess converts the input to lowercase, then checks to see if the letter is in the secret word.

### Milestone_3

I have added code to print underscores representing the unguessed characters of the mystery word. These are replaced with correctly guessed letters. If the player guesses a letter that is not in the mystery word, the player loses one life.

### Milestone_4

The complete Hangman game! 
The <mark>play_game</mark> function creates a new instance of the Hangman class, randomly chooses a mystery word from the list, sets lives to 5, and calls the ask_for_input function.
The <mark>ask_for_input</mark> function asks the player to guess a letter, with checks to make sure the input is a single alphabetical character, and calls the check_guess function.
The <mark>check_guess</mark> function checks to see if the guessed letter is in the mystery word. If it is, the word is printed with the unguessed characters showing as underscores e.g. guess = "a" prints: "_ a _ a _ a". If the guessed letter is not in the mystery word, the player loses a life.
The game continues until all the letters are guessed and the player wins, or the lives have run out and the player loses.


