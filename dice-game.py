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
        
        print("Turn of Player {}".format(currPlayer + 1))
        
        roll = RollDice()
        players[currPlayer].score += roll
        
        # If player rolls a 1, reset their score for the round to 0
        if roll == 1:
            print("You have rolled a 1 and lost with a score of 0!!!")
            players[currPlayer].score = 0
            currPlayer += 1
            continue
        
        print("You rolled a {number}: current score is {score}".format(number = roll,score = players[currPlayer].score))

        # Ask the player if they want to roll again
        print("Do you want to play again?")
        againTurn = input("y/n? ")
        
        # If the player chooses not to roll again, move to the next player's turn
        if againTurn != "y":
            print("Your score for this round is {}".format(players[currPlayer].score))
            currPlayer = currPlayer + 1

    # Finding the maximum score in the round
    max_score = max(player.score for player in players)

    # Check if there's a winner or if it's a tie
    winners = [player for player in players if player.score == max_score]

    if max_score == 0:
        print("Nobody wins!")
    else:
        print("The winner(s) of this round is: ")
        for winner in winners:
            print("Player {}".format(players.index(winner) + 1))
            winner.roundsWon += 1
    
    # Ask if players want to play the next round
    print("Do you want to play a next round?")   
    againRound = input("y/n? ")
    
    # If players choose not to play the next round, exit the loop
    if againRound != "y":
        break
    
    # Resteting the score of each player for next round
    for player in players:
        player.score = 0
    
    currPlayer = currPlayer % total_players

# Finding the maximum number of rounds won
max_rounds_won = max(player.roundsWon for player in players)

# Finding the winners of the game
winners = []
for player in players:
    if player.roundsWon == max_rounds_won:
        winners.append(player)

# Print winners of the game
if len(winners) == 1:
    winner_of_game = players.index(winners[0]) + 1
    won_rounds = winners[0].roundsWon
    print(f"The winner of this game is Player {winner_of_game}, who won {won_rounds} round(s)!")
else:
    print("It's a tie! The winners of this game are:")
    for winner in winners:
        print(f"Player {players.index(winner) + 1}")