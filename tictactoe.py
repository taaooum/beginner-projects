import random

def SelectPlayer() -> str:
    print("How many players are playing, 1 or 2?")
    try:
        num_players = int(input())
        if num_players not in (1, 2):
            raise ValueError
    except ValueError:
        print("Invalid input! Please enter either 1 or 2.")
        return SelectPlayer()

    if num_players == 1:
        return "cpu"
    else:
        return "player"

def RandomChoice(available_fields) -> int:
    return random.choice(available_fields)

def SelectChoice(available_fields: list) -> int:
    position = 0
    try:
        position = int(input("What position do you want to place your marker (1-9)? "))
        if position not in available_fields:
            raise ValueError
    except ValueError:
        print("Invalid input or position already taken! Please try again.")
        return SelectChoice(available_fields)
    return position

def CheckWinner(player1 : dict, player2 : dict) -> dict:
    winner = None
    
    # Define winning combinations
    winning = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]              # Diagonals
    ]

    # Check if any winning combination matches player's or CPU's positions
    for combo in winning:
        if all(pos in player1['Fields'] for pos in combo):
            winner = player1
            break
        elif all(pos in player2['Fields'] for pos in combo):
            winner = player2
            break
    
    return winner

def PrintPiece(board : list, position : int, current_player : dict):
    # ' ' – A vacant cell
    # 'X' – A cell occupied by player X
    # 'O' – A cell occupied by player O
    symbol = ' ' 
    if current_player == player1:
        symbol = 'X' 
    else:
        symbol = 'O'
    
    # Update player's positions
    current_player['Fields'].append(position)
    
    row, col = PositionRowCol(position)
    board[row][col] = symbol

def PositionRowCol(position : int) -> int | int:
    row, col = 0, 0
    if position in (1, 2, 3):
        row = 4
    elif position in (4, 5, 6):
        row = 2
    elif position in (7, 8, 9):
        row = 0

    if position in (1, 4, 7):
        col = 0
    elif position in (2, 5, 8):
        col = 2
    elif position in (3, 6, 9):
        col = 4
    return row, col

def PrintBoard(board):
     for row in board:
        print("".join(row))

def PrintBoardSample():
    board = [
    ['7' ,'│' ,'8' ,'│' ,'9' ],
    ['─','┼','─','┼','─'] ,
    ['4', '│', '5', '│', '6'],
    ['─','┼','─','┼','─'] ,
    ['1', '│', '2', '│', '3']]
    print()
    for row in range(len(board)):
        for col in range(len(board)):
            print(board[row][col] , end= "")
        print()
    print()

def Game():
    board = [
    [' ' ,'│' ,' ' ,'│' ,' ' ],
    ['─','┼','─','┼','─'] ,
    [' ', '│', ' ', '│', ' '],
    ['─','┼','─','┼','─'] ,
    [' ', '│', ' ', '│', ' ']]

    available_fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    winner = None
    
    print("Lets play Tic-Tac-Toe together!")
    
    player2['Type'] = SelectPlayer()
    
    print("The rules are simple. The board is build as shown and you can choose between fields 1 to 9.")
    PrintBoardSample()
    
    first = random.choice([player1, player2])
    current_player = first

    while winner != player1 and winner != player2 and available_fields:
        if current_player['Type'] == "player":
            position = SelectChoice(available_fields)
        else:
            position = RandomChoice(available_fields)
        
        # Update available fields after the position is taken
        available_fields.remove(position)
        
        PrintPiece(board, position, current_player)
        # Print the board after the player's move
        PrintBoard(board)
        
        # Check for a winner after the player's move
        winner = CheckWinner(player1, player2)
        if winner:
            break  # Exit the loop if there's a winner
        
        # Switch to the other player
        current_player = player1 if current_player == player2 else player2 


    if winner == player1:
        print("Congratulations! You won!")
        player1['Points'] += 1
    else:
        print("You lost.")
        player2['Points'] += 1
    
    # Ask if players want to play the next round
    print("Do you want to play another round?")
    again_round = input("Enter 'y' for yes or any other key to exit: ")
    if again_round.lower() == 'y':
        Game()

player1 = {"Type" : "player", "Fields" : [], "Points" : 0}
player2 = {"Type" : "undefined", "Fields" : [], "Points" : 0}

Game()