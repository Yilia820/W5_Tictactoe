import unittest
import logic

class Testlogic(unittest.TestCase):

    def test_get_winner(self):
        board=[
            ['x',None,'0']
            [None,'x',None],
            [None,'0','x']
      ]