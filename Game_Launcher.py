import Battle
import blackjack
import tic_tac_toe
import GuessingGame

main_menu = True

while main_menu:
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
        print(f"{key+':': <14}" + f'{value: >4}')

    selection = 0

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

