import unittest 
from activities import eat, nap, is_funny, laugh

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(
            eat("carrots", is_healthy=True),
            "I'm eating carrots, because they are good"
        )
    def test_eat_unhealthy(self):
            self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, YOLO"
        )

    def test_short_nap(self):
        self.assertEqual(
            nap(1),
            "im feeling refreshed after 1 hour nap"
        )

    def test_long_nap(self):
        self.assertEqual(
            nap(3),
            "Im feeling more tired"
        )

    def test_is_funny_tim(self):
        """tim should not be funny"""
        self.assertEqual(is_funny("tim"),False)

    def test_is_funny_anyone_else(self):
        """anyone else but time should be funny"""
        self.assertTrue(is_funny("blue"), "blue is funny"),
        self.assertTrue(is_funny("babes"), "babes is funny"),
        self.assertTrue(is_funny("annabelle"), "annabelle is funny")
        
    def test_laugh(self):
        self.assertIn(laugh(), ('lol', 'ha', 'tehe'))


if __name__ == "__main__":
    unittest.main()

# python3 test.py -v,
# adding -v command gives test function names
#  verbose 