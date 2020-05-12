import unittest 
from activities import eat, nap

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

if __name__ == "__main__":
    unittest.main()