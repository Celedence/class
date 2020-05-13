
from card import Card
from card import Deck
import unittest

class CardTest(unittest.TestCase):
    def setUp(self):
        self.card = Card("A", "Hearts")

    def test_init(self):
        """cards should have a suit and value"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")



if __name__ == "__main__":
    unittest.main()