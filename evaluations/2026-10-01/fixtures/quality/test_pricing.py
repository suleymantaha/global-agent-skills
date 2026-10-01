import unittest
from pricing import total_price

class PricingTests(unittest.TestCase):
    def test_three_items(self):
        self.assertEqual(total_price(7, 3), 21)

if __name__ == "__main__":
    unittest.main()
