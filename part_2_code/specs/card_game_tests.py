import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Hearts", 8)
        self.card2 = Card("Spades", 1)
        self.card3 = Card("Clubs", 5)
        self.cards = [self.card1, self.card2, self.card3]


    def test_check_for_ace(self):
        ace = CardGame.check_for_ace(self.card2)
        self.assertEqual(True, ace)

    def test_highest_card(self):
        highest_card = CardGame.highest_card(self.card1, self.card2)
        self.assertEqual(self.card1, highest_card)

    def test_cards_total(self):
        total = CardGame.cards_total(self.cards)
        self.assertEqual("You have a total of 14", total)
