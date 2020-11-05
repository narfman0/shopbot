import unittest
from shopbot.shopbot import logic


class Testshopbot(unittest.TestCase):
    def test_shopbot(self):
        self.assertEqual("Hello World!", logic())
