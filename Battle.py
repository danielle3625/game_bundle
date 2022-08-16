import random

game_on = True

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
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
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


def replay():
    global game_on

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

    for x in range(int(len(new_deck.all_cards) / 2)):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    round_num = 0

    auto_play = 'n'

    while game_on:

        if game_on == False:
            break

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
