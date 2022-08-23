import os
import random


def clearscreen():
    """
    Clear the console.
    So you only see current board with updated moves
    """
    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('cls')
    else:
        # Fallback for other operating systems.
        # Print a simple divider
        print('-----')
        print('-----')


def display_board(board):
    """
    Print out updated board per last move - only show most recent board
    """

    clearscreen()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('_____')


def player_input():
    """
    Select which Player is X and which Player is O
    Output = (player 1 marker, Player 2 marker)
    """
    
    player1 = ''
    
    while player1.upper() not in ['X', 'O']:
        player1 = input('Player 1, Please choose X or O: ')
        
        if player1.upper() not in ['X', 'O']:
            print('Sorry, you must choose between X or O only!')
        else:
            break

    if player1.upper() == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return player1.upper(), player2.upper()


def place_marker(board, marker, position):
    """
    Places mark on board
    """
    board[position] = marker


def win_check(board, mark):
    """
    Checks to see if there are three marks in a row
    """

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    #across middle
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    #across bottom
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    #column 1
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    #column 2
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    #column 3
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    #diag 1
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    #diag 2
    (board[1] == mark and board[5] == mark and board[9] == mark))


def choose_first():
    """
    Decide who goes first
    """
    flip = random.randint(0, 1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    """
    Checks that a space has not been taken already
    """
    
    if board[position] == ' ':
        return True


def full_board_check(board):
    """
    Checks if all spaces are taken
    """
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# In[8]:


def player_choice(board):
    """
    Ask for next move
    """
    position = 0
    
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        try:
            position = int(input('Choose your next position: (1-9) '))
        except ValueError:
            print('You must enter an integer!')
    return position


def computer_choice(board):
    """
    Generate computer player move
    """
    position = 0
    
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = random.randint(1, 9)
        
    return position


def replay():
    choice = input("Do you want to play again? Y or N: ").upper()
    if choice == 'Y':
        return True
    else:
        return False


def tictac_play_game():
    """
    Create a function to call game play via game launcher
    """
    print('Welcome to Tic Tac Toe!')

    while True:
        # Reset the board to all blank spaces

        new_board = [' '] * 10
        player1_marker, player2_marker = player_input()

        turn = choose_first()
        print("Let's Play! " + turn + "  will go first")

        play_game = 'initiate_the_while_loop_below'

        while play_game.upper() not in ['N', 'Y']:
            play_game = input('Are you ready to play? Enter Yes or No.')

        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            #Player1's turn
            if turn == 'Player 1':

                display_board(new_board)
                board_position = player_choice(new_board)
                place_marker(new_board, player1_marker, board_position)

                if win_check(new_board, player1_marker):
                    display_board(new_board)
                    print('Congrats! Player 1 is the winner!')
                    break
                else:
                    if full_board_check(new_board):
                        print('There are no winners today')
                        break
                    else:
                        turn = 'Player 2'

            # Player2's turn.
            else:
                display_board(new_board)
                board_position = computer_choice(new_board)
                place_marker(new_board, player2_marker, board_position)

                if win_check(new_board, player2_marker):
                    display_board(new_board)
                    print('Congrats! Player 2 is the winner!')
                    break
                else:
                    if full_board_check(new_board):
                        print('There are no winners today')
                        break
                    else:
                        turn = 'Player 1'
                        
        if not replay():
            break
