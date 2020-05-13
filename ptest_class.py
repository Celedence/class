import unittest
from game_demo import Prot

class ProtTests(unittest.TestCase):
    def setUp(self):
        self.pickles = Prot("Pickles", exp= 50)

    def test_earned(self):
        self.pickles.earned()
        self.assertEqual(self.pickles.exp, 100)

    def test_say_name(self):
        self.pickles.say_name()
        self.assertEqual(self.pickles.name, "Pickles")
        

if __name__ == "__main__":
    unittest.main()
