
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

    def test_repr(self):
        """repr should return a string of the form value"""
        self.assertEqual(repr(self.card), "A of Hearts")

class DeckTest(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """decks should have a cards attr"""
        self.assertTrue(isinstance(self.deck.cards,list))
        self.assertEqual(len(self.deck.cards),52)

    def test_repr(self):
        """repr should return a string of the form deck"""
        self.assertEqual(repr(self.deck),"Deck of 52 cards")

    def test_count(self):
        """should return a count of the number of cards"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_suffic_cards(self):
        """deal should deal the number of cards specified"""
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_deal_insufficient(self):
        """_deal should deal the number of cards left in a deck"""
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_no_card(self):
        """should throw a value error if the deck is empty"""
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_card(self):
        """should deal a single card from deck"""
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        """should deal number of cards passed into it"""
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards),20)
        self.assertEqual(self.deck.count(), 32)

    def test_shuffle_full_deck(self):
        """shuffle should shuffle the deck if the deck if full"""
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)

    def test_shuffle_not_full_deck(self):
        """should throw a value error if the deck isnt full"""
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()



    









if __name__ == "__main__":
    unittest.main()