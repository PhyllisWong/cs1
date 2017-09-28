"""Game to play hangman."""
import random
import string


def load_word():
    """Read a text file with a list of words."""
    f = open('hangman_words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def draw_word(secret_word):
    """Input string and an array."""
    """Returns hint with letters guessed in place each turn. Ouput string."""

    word = ""
    for c in secret_word:
        word = word + " _ "
    return word


def update_board(secret_word, guessed_letters_arr):
    """Update the hint with correclty guessed letters."""
    word = ""

    for c in secret_word:
        if c in guessed_letters_arr:
            word += c
        else:
            word += " _ "
    return word


def is_guess_valid(guessed_letters_arr):
    """Get letter from user, validate it, input arr, output Bool."""
    user_guess = input('Guess a letter: ')
    # fix the str check
    if user_guess in string.ascii_letters.lower():
        if len(user_guess) == 1:
            if user_guess not in guessed_letters_arr:
                guessed_letters_arr.append(user_guess)
                return True
    else:
        return False


def is_word_guessed(secret_word_str, guessed_letters_arr):
    """Loop thru the secret_word, return true if all are in word."""
    # letter_counter = 0
    for c in secret_word_str:
        if c not in guessed_letters_arr:
            return False
    return True


def ask_to_play_again():
    """Ask user to play again, reset guessed_letters_arr."""
    global guessed_letters_arr
    play_again = input('Would you like to play again? y or n: ')
    if (play_again == 'y'):
        guessed_letters_arr = []
        hangman(secret_word)
    elif (play_again == 'n'):
        quit()
    else:
        ("Not a valid input.")
        ask_to_play_again()


def hangman(word_string):
    """Secret_word: string, the word to guess."""
    """At start of the game, give user hint."""
    """Ask user to guess one letter per round."""
    """User should receive feedback immediately after each guess"""
    """Update board w/partially guessed word and guessed letters."""
    guessed_letters_arr = []
    print("\n"+"Welcome to hangman."+"\n")
    secret_word = load_word()
    turns = len(secret_word) + 5
    # is_guess_valid, stay in loop until run out of turns
    while turns > 0:
        did_win = is_word_guessed(secret_word, guessed_letters_arr)
        if did_win is True:
            print("You win! Your word was " + secret_word)
            ask_to_play_again()
        update = update_board(secret_word, guessed_letters_arr)
        print(update + '\t\t' + str(guessed_letters_arr))
        print("\n"+"You have " + str(turns) + " tries to win.")
        take_guess = is_guess_valid(guessed_letters_arr)
        if take_guess is True:
            # store variable, update board
            turns -= 1
        else:
            print('Not a valid guess, try again.')
            is_guess_valid(guessed_letters_arr)
    if turns == 0:
        print("\n"+"Sorry, your secret word was: " + secret_word+"\n")
        ask_to_play_again()


# print(draw_word(load_word()))
secret_word = load_word()
hangman(secret_word)
