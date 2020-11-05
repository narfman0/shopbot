import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from shopbot import newegg


class TestNewegg(unittest.TestCase):
    @patch('shopbot.newegg.ActionChains')
    def test_attempt(self, ac):
        webdriver_mock = MagicMock()
        newegg._attempt(webdriver_mock, "url1", "search1")

    @patch('shopbot.newegg.webdriver')
    @patch('shopbot.newegg.settings')
    @patch('shopbot.newegg.ActionChains')
    def test_attempt_purchase(self, webdriver, settings, ac):
        settings.BREAKPOINT_ON_SUCCESS = False
        newegg.attempt_purchase()
