import unittest

from gamebundle import tic_tac_toe

    #None of these tests are working and I don't know why
class TestTicTacToe(unittest.TestCase):

    def test_win_check(self):
        board = ['x'] * 10
        mark = ['x']
        self.assertTrue((board[7] == mark and board[8] == mark and board[9] == mark) or
    #across middle
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    #across bottom
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    #column 1
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    #column 2
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    #column 3
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    #diag 1
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    #diag 2
    (board[1] == mark and board[5] == mark and board[9] == mark))
        

     # This seems redundant because it's dependent on user input   
    def test_player_choice(self):
        self.assertIn(tic_tac_toe.player_choice(), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        
    def test_computer_choice(self):
        self.assertIn(tic_tac_toe.computer_choice(), [1, 2, 3, 4, 5, 6, 7, 8, 9])
    