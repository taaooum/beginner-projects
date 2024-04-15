# Dice Game Documentation:
# This game involves multiple rounds where each player takes turns rolling a dice.
# The score for each player accumulates as they roll the dice, but if a player rolls a 1, their score for the round becomes 0 and the turn moves to the next player.
# The player decides when to stop rolling, except when they roll a 1.
# At the end of each round, the player with the highest score wins the round.
# The game continues until the players decide not to play the next round.
# The player who wins the most rounds is declared the winner of the game.

import random

class Player:
    def __init__(self):
        self.score = 0
        self.roundsWon = 0

# Function to roll a dice
def RollDice():
    min = 1
    max = 6
    return random.randint(min, max)

playerCount = 0
players = []

# Input validation for the number of players
total_players = 0
while total_players <= 0:
    total_players = int(input("How many players are there? "))
    if total_players <= 0:
        print("Please enter a positive number of players.")

# Creating instances for each player
while playerCount < total_players:
    player = Player()  # Create a new instance of the Player class
    players.append(player)  # Add the player instance to the list
    playerCount += 1

print("Ok let's start the game!")

currPlayer = 0 

while True:
    
    while currPlayer < len(players):
        
        print("Turn of Player " + str(currPlayer + 1))
        
        roll = RollDice()
        players[currPlayer].score += roll
        
        # If player rolls a 1, reset their score for the round to 0
        if roll == 1:
            print("You have rolled a 1 and lost with a score of 0!!!")
            players[currPlayer].score = 0
            currPlayer += 1
            continue
        
        print("You rolled a " + str(roll) + ": current score is " + str(players[currPlayer].score))

        # Ask the player if they want to roll again
        print("Do you want to play again?")
        againTurn = input("y/n? ")
        
        # If the player chooses not to roll again, move to the next player's turn
        if againTurn != "y":
            print("Your score for this round is " + str(players[currPlayer].score))
            currPlayer = currPlayer + 1

    # Finding the winner of the round
    winnerRound = max(players, key=lambda x: x.score)
    if(winnerRound.score == 0):
        print("nobody wins!")
    else:
        print("The winner of this round is Player " + str(players.index(winnerRound) + 1))
        winnerRound.roundsWon += 1 

    # Ask if players want to play the next round
    print("Do you want to play a next round?")   
    againRound = input("y/n? ")
    
    # If players choose not to play the next round, exit the loop
    if againRound != "y":
        break
    
    currPlayer = currPlayer % total_players

# Finding the winner of the game
winnerGame = max(players, key=lambda x: x.roundsWon)
print("The winner of this game is Player " + str(players.index(winnerGame) + 1) + ", who won " + str(winnerGame.roundsWon) +" rounds!")