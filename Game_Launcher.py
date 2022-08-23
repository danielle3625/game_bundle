# The game launcher provides a main menu screen to allow a user to choose their game, play chosen game multiple rounds

# Here, we import the other games, as separate modules
import Battle
import blackjack
import tic_tac_toe
import GuessingGame


while True:
    print('Welcome to the Game Launcher Interface full of spectacular newbie programmable games!')
    print('MAIN MENU: ')

    game_menu = {
        'Blackjack': '1',
        'Tic Tac Toe': '2',
        'War (Battle)': '3',
        'Guessing Game': '4',
        'Quit': '5'
    }

    for key, value in game_menu.items():
      # Use f string to left align and right align respective columns
      # I find it easier on my eyes this way, and enhancing readability
        print(f"{key+':': <14}" + f'{value: >4}')

    selection = 0

    # Use If-Elif clauses to clearly indicate when given game module is called,
    #   then the respective game_play() function is called.
    # Although longer code, the code is easily read in english instead of assigned by dictionary index
    # Implementing respective game_play() function per game allows for multiple rounds of each game to be played,
    #   and then allows user to return to main menu to select a different game without restarting game_launcher
    while selection not in game_menu.values():
        selection = input('Enter the number choice for your selection ')
    if selection == '1':
        blackjack.blackjack_play_game()
    elif selection == '2':
        tic_tac_toe.tictac_play_game()
    elif selection == '3':
        Battle.game_play()
    elif selection == '4':
        GuessingGame.gameplay()
    elif selection == '5':
        print('See you later! Come back soon!')

        break

