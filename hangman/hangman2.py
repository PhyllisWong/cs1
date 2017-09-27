"""Play simple hangman game."""
import random

# set the secret word
# creates a variable with an empty value
# determine number of turns


def load_word():
    """Read a text file with a list of words."""
    f = open('hangman_words.txt', 'r')
    wordsList = f.readlines()
    f.close()
    wordsList = wordsList[0].split(' ')
    secret_word = random.choice(wordsList)
    return secret_word


def take_user_guess(string):
    """Get letter from user, validate it, input arr, output string length 1."""
    user_guess = input('Guess a letter: ')
    if len(user_guess) == 1:
        if type(user_guess) == str:
            if user_guess not in string:
                return user_guess
    else:
        print("Not a valid guess, try again.")
        take_user_guess(string)


def hangman():
    """Call all subfunctions from the main function."""
    secret_word = load_word()
    guesses = ''
    turns = 10

# loop keeps the game in play until no more turns
    while turns > 0:
        failed = 0
        for c in secret_word:
            if c in guesses:
                secret_word += c
            else:
                secret_word = secret_word + " _ "
                failed += 1
        if failed == 0:
            print('You won!')
            break
# ask the user to guess a character, validates the guess
    guess = take_user_guess(guesses)
# set the players guess to guesses
    guesses += guess
# if the guess is not found in the secret word
    if guess not in secret_word:
        turns -= 1
        print("Wrong")
        print("You have " + turns + " more guesses")
        if turns == 0:
            print("Sorry, better luck next time")


hangman()
