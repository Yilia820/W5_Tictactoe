import unittest
import W5_logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', 'None', 'O'],
            ['None', 'X', 'None'],
            ['None', 'O', 'X'],
        ]
        board1 = [
            ['O', 'None', 'X'],
            ['None', 'O', 'None'],
            ['None', 'X', 'O'],
        ]
        board2 = [
            ['X', 'None', 'O'],
            ['None', 'X', 'None'],
            ['None', 'O', 'O'],
        ]
        self.assertEqual(W5_logic.get_winner(board), 'X')
        self.assertEqual(W5_logic.get_winner(board1), 'O')
        self.assertEqual(W5_logic.get_winner(board2), 'None')
        self.assertEqual(W5_logic.other_player("O"), 'X')
        self.assertEqual(W5_logic.other_player("X"), 'O')
    # TODO: Test all functions from logic.py!


if __name__ == '__main__':
    unittest.main()

