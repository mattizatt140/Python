# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import os
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    wordProgress = []
    for i in secretWord:
        if i not in lettersGuessed:
            wordProgress.append('_ ')
        elif i in lettersGuessed:
            wordProgress.append(i)
    return ''.join(wordProgress)


def getAvailableLetters(lettersGuessed):
    availableLetters = []
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            availableLetters.append(i)
    return ''.join(availableLetters)
    

def hangman(secretWord):
    over = False
    guesses = 8
    lettersGuessed = []
    availableLetters = []
    for i in string.ascii_lowercase:
        availableLetters.append(i)

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long")
    
    while not over:
        print("-------------------")
        print("You have", guesses, "guesses left")
        print("Available letters:", ''.join(availableLetters))
        guess = input("Please guess a letter: "); guess = guess.lower()

        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
         
        elif guess in secretWord:
            lettersGuessed.append(guess)
            availableLetters.remove(guess)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))

        else:
            guesses -= 1
            lettersGuessed.append(guess)
            availableLetters.remove(guess)
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))

        if guesses == 0:
            over = True
            print("-------------------")
            print("Sorry, you ran out of guesses. The word was", secretWord)
        elif isWordGuessed(secretWord, lettersGuessed):
            over = True
            print("-------------------")
            print("Congradulations, you won!")

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
