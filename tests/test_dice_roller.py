import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import Dice_Roller


class TestDiceRoller(unittest.TestCase):
    def test_main_roll_then_exit(self):
        with patch("builtins.input", side_effect=["roll", "n", "exit"]):
            try:
                Dice_Roller.main()
            except SystemExit:
                pass

    def test_main_exit_directly(self):
        with patch("builtins.input", return_value="exit"):
            try:
                Dice_Roller.main()
            except SystemExit:
                pass

    def test_main_invalid_then_exit(self):
        with patch("builtins.input", side_effect=["invalid", "exit"]):
            try:
                Dice_Roller.main()
            except SystemExit:
                pass

    def test_roll_dice_output_range(self):
        for _ in range(100):
            val = Dice_Roller.randint(1, 6)
            self.assertIn(val, range(1, 7))

    def test_color_class(self):
        self.assertTrue(Dice_Roller.color.BOLD)
        self.assertTrue(Dice_Roller.color.END)


if __name__ == "__main__":
    unittest.main()
