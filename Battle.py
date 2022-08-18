import random

# @review-note: This variable gets used as a global throughout the application.
#               Usage of global variables is very frowned upon for multiple reasons.
#               See: http://wiki.c2.com/?GlobalVariablesAreBad
game_on = True

# @review-note: Those look like constants. According to convention, constants should be named in UPPERCASE.
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
# @review-note: `ranks` seems to be identical to `tuple(values.keys())`. If this can not be omitted, I suggest
#               constructing `ranks` from `values.keys()` to prevent accidental errors.
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):
        # @review-note: A list comprehension could cut processing time and line numbers here.
        #               For example: `self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]`
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # @review-note: I think you were looking for `if isinstance(new_cards, list):` to check if
        #               multiple cards have been dealt ? Alternately you could always add cards with lists and
        #               not worry about the type.
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


def replay():
    global game_on
    # @review-note: I think this is overly complicated. Suggestion:
    #               `return game_on := input("Do you want to play again? Y or N: ").upper() == 'Y'`
    choice = input("Do you want to play again? Y or N: ").upper()
    if choice == 'Y':
        game_on = True
        return True
    else:
        game_on = False
        return False


def game_play():
    global game_on

    game_on = True

    player_one = Player("One")
    player_two = Player("Two")

    new_deck = Deck()
    new_deck.shuffle()

    # @review-note: I think you are dealing each player half of the deck here.
    #               This could be the rare occasion where a while loop would be preferred over a for loop.
    #               Dealing cards until the deck is empty.
    # @review-note: If you don't need the iteration variable of a for loop, use `_` to annotate that.
    #               See: https://www.datacamp.com/tutorial/role-underscore-python Section 2
    for x in range(int(len(new_deck.all_cards) / 2)):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    round_num = 0

    auto_play = 'n'

    while game_on:

        # @review-note: `if not game_on` does the same thing.
        #               See: https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/
        if game_on == False:
            break

        # @review-note: I just skimmed over the rest of the file. It gets very nested quickly, so I became slightly
        #               confused. Usually nesting should be avoided if possible. Instead split your logic in smaller
        #               methods and call them at the correct time. This increases maintainability and readability.

        # Otherwise, the game is still on!
        while auto_play not in ['a', 'y', 'd']:
            auto_play = input('Press "y" to play next round only or press "a" to auto play:  ')

            if auto_play == 'd':
                game_on = False
                print('Come again soon!')
                break

            while auto_play == 'a' or auto_play == 'y':
                round_num += 1

                print(f"Round {round_num}")

                # Check to see if a player is out of cards:
                if len(player_one.all_cards) == 0:
                    print("Player One out of cards! Game Over")
                    print("Player Two Wins!")
                    game_on = False
                    if replay():
                        game_play()
                        break
                    else:
                        print('Thanks for playing! Goodbye!')
                        auto_play = 'd'
                        break

                elif len(player_two.all_cards) == 0:
                    print("Player Two out of cards! Game Over")
                    print("Player One Wins!")
                    game_on = False
                    if replay():
                        game_play()
                        break
                    else:
                        print('Thanks for playing! Goodbye!')
                        auto_play = 'd'
                        break

                # Check to see if a player has enough cards to play:
                elif len(player_one.all_cards) < 3:
                    print("Player One out of cards! Game Over")
                    print("Player Two Wins!")
                    game_on = False
                    if replay():
                        game_play()
                        break
                    else:
                        print('Thanks for playing! Goodbye!')
                        auto_play = 'd'
                        break

                elif len(player_two.all_cards) < 3:
                    print("Player Two out of cards! Game Over")
                    print("Player One Wins!")
                    game_on = False
                    if replay():
                        game_play()
                        break
                    else:
                        print('Thanks for playing! Goodbye!')
                        auto_play = 'd'
                        break

                # Otherwise, the game is still on!

                #
                player_one_cards = [player_one.remove_one(), player_one.remove_one(), player_one.remove_one()]
                print('Player 1: 2 face down cards, ' + str(player_one_cards[-1]))

                player_two_cards = [player_two.remove_one(), player_two.remove_one(), player_two.remove_one()]
                print('Player 2: 2 face down cards, ' + str(player_two_cards[-1]))

                at_war = True

                while at_war:

                    if player_one_cards[-1].value > player_two_cards[-1].value:

                        # Player One gets the cards
                        player_one.add_cards(player_one_cards)
                        player_one.add_cards(player_two_cards)

                        # No Longer at "war" , time for next round
                        at_war = False
                        if auto_play == 'a':
                            continue
                        else:
                            auto_play = 'n'
                            break

                    # Player Two Has higher Card
                    elif player_one_cards[-1].value < player_two_cards[-1].value:

                        # Player Two gets the cards
                        player_two.add_cards(player_one_cards)
                        player_two.add_cards(player_two_cards)

                        # No Longer at "war" , time for next round
                        at_war = False
                        if auto_play == 'a':
                            continue
                        else:
                            auto_play = 'n'
                            break

                    elif player_one_cards[-1].value == player_two_cards[-1].value:
                        print('Battle!')
                        # This occurs when the cards are equal.

                        # Check to see if a player is out of cards:
                        if len(player_one.all_cards) < 5:
                            print("Player One unable to play war! Game Over at War")
                            print("Player Two Wins! Player One Loses!")
                            game_on = False
                            if replay():
                                game_play()
                            else:
                                print('Thanks for playing! Goodbye!')
                                auto_play = 'd'
                                break

                        elif len(player_two.all_cards) < 5:
                            print("Player Two unable to play war! Game Over at War")
                            print("Player One Wins! Player One Loses!")
                            game_on = False
                            if replay():
                                game_play()
                            else:
                                print('Thanks for playing! Goodbye!')
                                auto_play = 'd'
                                break

                        # Otherwise, we're still at war, so we'll add the next cards
                        else:
                            for num in range(5):
                                player_one_cards.append(player_one.remove_one())
                                player_two_cards.append(player_two.remove_one())
                            print('Player 1 cards: 4 facedown + ' + str(player_one_cards[-1]))
                            print('Player 2 cards: 4 facedown + ' + str(player_two_cards[-1]))
