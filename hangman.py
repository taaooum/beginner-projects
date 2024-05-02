# Hangman Game

# The database is a words.txt file that stores all possible words.
# You need to ensure that the words.txt file exists and contains a list of words separated by newline characters.

import random

# Returns a randomly chosen word from the database.
def ChooseWord(path):
    try:
        file = open(path, "r")
        database = file.readlines()
        file.close()
        return random.choice(database).strip().lower()
    except Exception as e:
        print("An error occurred while accessing the database:", e)
        return None

# Returns a updated number of remaining attempts/lives and the status of correctness.
def CheckAwnser(lifes, correct, lastInput, allInputs, awnser):
    found_letter = False
    if len(lastInput) > 1:
        if lastInput == awnser:
            print("Hurray! Your choice {} is the correct answer!!".format(lastInput))
            correct = True
            return lifes, correct
        else:
            print("Sorry! Your choice {} is not the answer!".format(lastInput))
            return lifes - 1, correct
    else:
        for i in awnser:
            if lastInput == i:
                print(i, end=" ")
                found_letter = True
            elif i in allInputs:
                print(i, end=" ")
            else: 
                print("_", end=" ")
    
        if found_letter:
            if set(awnser).issubset(set(allInputs)):
                print("Hurray! Your choice {} is the correct answer!!".format(lastInput))
                correct = True
            return lifes, correct
        else:
            return lifes - 1, correct

# The main game function that orchestrates the gameplay.
def Game():

    lifes = 10                          # The number of remaining attempts/lives.
    letters = []                        # A list containing all previous user inputs.
    awnser = ChooseWord(path).lower()   # The correct answer word.
    correct = False                     # A boolean flag indicating whether the game has been won.
    
    # Print placeholders for each letter of the answer word.
    for i in awnser:
        print("_", end=" ")

    # Main game loop
    while lifes and not correct:
        print("\nYou have {} lifes left!".format(lifes))
        
        # Get user input for guessing a character or word.
        choice = input("Choose a character or word you want to try! ").lower()
        
        # Check if the user input has been already guessed.
        if choice in letters and choice in valid:
            continue
        
        letters += choice
        
        # Check the correctness of the user's input.
        lifes, correct = CheckAwnser(lifes, correct, choice, letters, awnser)
    if not lifes:
        print("The awnser was {} ! Mabye next time...".format(awnser))
  
# Valid characters that the user can guess.
valid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Path to the database file containing the list of words.
path = "beginner-projects/resources/hangman-database.txt"

# Start the game.
print("\nLet's play Hangman! Try to beat me! You have 10 lives.")
Game()