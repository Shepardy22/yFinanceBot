import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller import Controller

class TestController(unittest.TestCase):
    @patch('builtins.input', side_effect=['AAPL', '5d'])
    def test_start(self, mock_input):
        controller = Controller()
        controller.start()

if __name__ == '__main__':
    unittest.main()
