'''Game to play hangman.'''
import random


good_letters = 'abcdefghijklmnopqrstuvwxyz'
guessed_letters_arr = []
turns = 10


def load_word():
    """Read a text file with a list of words."""
    f = open('hangman_words.txt', 'r')
    wordsList = f.readlines()
    f.close()
    wordsList = wordsList[0].split(' ')
    secret_word = random.choice(wordsList)
    return secret_word


def draw_word(secret_word_str, guessed_letters_arr):
    """
    Input string and an array.
    Returns hint with letters guessed in place each turn. Ouput string.
    """
    word = ""

    for c in secret_word_str:
        if c in guessed_letters_arr:
            word = word + c
        else:
            word = word + " _ "
    return word


def take_user_guess(guessed_letters_arr):
    """Get letter from user, validate it, input arr, output string length 1."""
    user_guess = input('Guess a letter: ')
    global turns
    while turns > 0:
        if type(user_guess) == str and len(user_guess) == 1:
            if user_guess not in guessed_letters_arr:
                guessed_letters_arr.append(user_guess)
                turns -= 1
                return user_guess
    if turns == 0:
        print("Sorry, better luck next time.")
        ask_to_play_again()
    else:
        print('Not a valid guess, try again.')
        take_user_guess(guessed_letters_arr)

# def letters_guessed(char):
#     '''Collect all the guesses in an array, return array'''
#     collect_letters = []


def is_word_guessed(secret_word_str, guessed_letters_arr):
    """Loop thru the secret_word, return true if all are in word."""
    # letter_counter = 0
    for i in secret_word_str:
        if i not in guessed_letters_arr:
            return False
    return True


def getGuessedWord(letter, secret_word, good_letters):
    """
    SecretWord: string, the random word the user is trying to guess.
    LettersGuessed: list of letters that have been guessed so far.
    Returns: string, of letters and underscores. For letters in the word that.
    the user has guessed correctly, the string should contain the letter at the
    correct position. For letters in the word that the user has not yet guessed
    shown an _ (underscore) instead.
    """
    letters_in_word = []
    if letter in good_letters:
        letters_in_word.append(letter)
        # Figure out how to know what index each letter is at.
        pass


def getAvailableLetters(guessed_letters_arr, user_guess):
    """lettersGuessed: list of letters that have been guessed so far.
    Returns: string, comprised of letters that represents what letters have.
    Not yet been guessed.
    """
    # array of letters available to guess
    good_letters_arr = good_letters.split()
    guessed_letters_arr.append(user_guess)
    for c in good_letters:
        if c in guessed_letters_arr:
            good_letters_arr.remove(c)
            gl = "".join(guessed_letters_arr)
    return gl


# Out put game play to player in one print statement
def output_to_user(draw_word, guessed_letters_arr):
    draw_board = draw_word(secret_word_str, guessed_letters_arr)
    guesses = guessed_letters_arr
    print((draw_board) + '\t\t' + guesses + '\n\n')
# add new line and tab characters for formatting


def ask_to_play_again():
    play_again = input('Would you like to play again? y or n: ')
    if (play_again == 'y'):
        hangman(secret_word)
    elif (play_again == 'n'):
        quit()


def hangman(word_string):
    """
    SecretWord: string, the secret word to guess.
    Start up a game of Hangman in the command line.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to guess one letter per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    """
    # FILL IN YOUR CODE HERE...
    global secret_word, guessed_letters_arr
    print("Welcome to hangman, you get 5 tries to win.")
    secret_word = load_word()
    draw_board = draw_word(secret_word, guessed_letters_arr)
    take_user_guess(guessed_letters_arr)
    # output_to_user(draw_word, guessed_letters_arr)
    # take_user_guess()
    did_win = is_word_guessed(secret_word, guessed_letters_arr)
    guessed_letters = ''.join(guessed_letters_arr)
    print(draw_board + '\t\t' + guessed_letters)
    if did_win is False:
        take_user_guess(guessed_letters_arr)
        did_win = is_word_guessed(secret_word, guessed_letters_arr)
        guessed_letters = ''.join(guessed_letters_arr)
    elif did_win is True:
        you_win(did_win)
        return


secret_word = load_word()
hangman(secret_word)
