import unittest

from gamebundle.Battle import Deck, Player, Card


class TestBattle(unittest.TestCase):
    def test_decks_gets_shuffled_correctly(self) -> None:
        # Make new Deck
        deck: Deck = Deck()
        # Make list of all Cards as strings
        cards_before_shuffle = [str(card) for card in deck.all_cards]
        # Shuffle Deck
        deck.shuffle()
        # Assert that the cards are now ordered differently
        self.assertNotEqual(cards_before_shuffle, [str(card) for card in deck.all_cards])

    def test_deal_one_works_as_expected(self) -> None:
        # Make new Deck
        deck: Deck = Deck()
        # Assert that it should contain 52 cards
        self.assertEqual(52, len(deck.all_cards))
        # Deal one card
        dealt_card = deck.deal_one()
        # Assert that the dealt card is now no longer in the deck
        self.assertNotIn(dealt_card, deck.all_cards)
        # Assert that the deck has now one card less
        self.assertEqual(51, len(deck.all_cards))

    def test_player_receives_card_correctly(self) -> None:
        # Create new player
        player: Player = Player("TEST_PLAYER")
        # Assert that the new player has no cards
        self.assertFalse(player.all_cards)

        # Create a new Card
        card_to_be_given = Card("Hearts", "Two")
        # Give the player the card as a single object
        player.add_cards(card_to_be_given)

        # Assert player has now one card
        self.assertEqual(1, len(player.all_cards))
        # Assert that the card given is now in the players "hand"
        self.assertIn(card_to_be_given, player.all_cards)
        # Assert that the only card in the players hand is identical to the given one
        self.assertEqual(card_to_be_given, player.all_cards[0])

        # Make another Card
        another_card_to_be_given = Card("Hearts", "Nine")
        # Add card as a list of objects
        player.add_cards([another_card_to_be_given])
        # Assert player has now two cards
        self.assertEqual(2, len(player.all_cards))
        # Assert that the card given is now in the players "hand"
        self.assertIn(another_card_to_be_given, player.all_cards)
        # Assert that the second card in the players hand is identical to the given one
        self.assertEqual(another_card_to_be_given, player.all_cards[1])


if __name__ == "__main__":
    unittest.main()
