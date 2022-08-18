# GENERAL REVIEW NOTES
# THIS SECTION IS FOR NOTES THAT APPLY TO THE WHOLE PROJECT
#
# - Do not push .idea and venv directories. For the venv part you want a `requirements.txt` file
#   See https://learnpython.com/blog/python-requirements-file/
#   The .idea can be omitted generally. It should be added to a .gitignore
#   See https://www.freecodecamp.org/news/gitignore-what-is-it-and-how-to-add-to-repo/
#
# - Missing Typehints. Typehints are a great addition to projects of any size. Not only make it your code more readable,
#   it also allows your IDE to spot potential errors for you. Same goes for return type annotations.
#
# - Lack of comments. There are not many comments in your code. I occasionally had a difficult time understanding what
#   something does and why it does what it does. Writing good documentation is a high skill.

import Battle
import blackjack
import tic_tac_toe
import GuessingGame

# @review-note: This variable does never change, so it doesnt need to exist. You can use `while True:` below instead.
main_menu = True

while main_menu:
    print('Welcome to the Game Launcher Interface full of spectacular newbie programmable games!')
    print('MAIN MENU: ')
    # @review-note: If you would use a list of dictionaries here, with the respective functions as value, you could
    #               trim the big if-else tree below by 95%
    game_menu = {
        'Blackjack': '1',
        'Tic Tac Toe': '2',
        'War (Battle)': '3',
        'Guessing Game': '4',
        'Quit': '5'
    }

    for key, value in game_menu.items():
        # @review-note: This seems very overly complicated, the `\t` character would do the same thing:
        #               For example: `print(f'{value}:\t{key}')`
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
        # @review-note: It is best practice to end a program with `exit()` and an exit code. Usually zero for when
        #               everything went fine, and 1 to 255 for any errors.
        break

