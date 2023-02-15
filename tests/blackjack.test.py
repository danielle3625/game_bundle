import unittest
from gamebundle import blackjack

class TestBlackjack(unittest.TestCase):
    def test_deck_shuffled(self):
        deck: deck = blackjack.Deck()
        cards_pre_shuffle = [str(card) for card in deck.all_cards]
        deck.shuffle()
        self.assertNotEqual(cards_pre_shuffle, [str(card) for card in deck.all_cards])

    def deal_returns_single_card(self):
        deck: deck = blackjack.Deck()
        self.assertEqual(52, deck.all_cards)
        one_card = blackjack.deal()
        self.assertEqual(1, len(one_card))
        self.assertEqual(51, len(deck.all_cards))

    def test_player_hand(self):
        player: player = blackjack.Hand()
        self.assertEqual(0, player)
        deck: deck = blackjack.Deck()
        player = player.blackjack.hand.add_card(blackjack.deck.deal())
        self.assertEqual(1, player)

