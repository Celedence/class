import unittest
from game_demo import Prot

class ProtTests(unittest.TestCase):
    def test_earned(self):
        pickles = Prot("Pickles", exp= 50)
        pickles.earned()
        self.assertEqual(pickles.exp, 100)

    def test_say_name(self):
        pickles = Prot("Pickles", exp= 50)
        pickles.say_name()
        self.assertEqual(pickles.name, "Pickles")
        

if __name__ == "__main__":
    unittest.main()
