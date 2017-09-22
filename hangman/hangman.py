import random


def loadWord():
    '''Reads a text file with a list of words.'''
    f = open('words.txt', 'r')
    wordsList = f.readlines()
    f.close()
    wordsList = wordsList[0].split(' ')
    secretWord = random.choice(wordsList)
    return secretWord


def take_user_guess():
    '''Get letter from user, output a character'''
    letter_guessed = input('guess a letter')
    return letter_guessed


def letters_guessed(char):
    '''Collect all the guesses in an array, return array'''
    collect_letters = []
    collect_letters.append(char)
    return collect_letters


def is_word_guessed(secretWord_str, letters_guessed_arr):
    '''Loop thru the secret_word, return true if all are in word'''
    letter_counter = 0
    for i in secretWord_str:
        if secretWord_str[i] not in letters_guessed_arr:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up a game of Hangman in the command line.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to guess one letter per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    # FILL IN YOUR CODE HERE...


secretWord = loadWord()
hangman(loadWord())
