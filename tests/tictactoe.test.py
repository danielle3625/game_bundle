import unittest
from gamebundle import tic_tac_toe

    #None of these tests are working and I don't know why
class TestTicTacToe(unittest.TestCase):

    def test_win_check(self):
        board = ['x'] * 10
        mark = 'x'
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
                
if __name__ == "__main__":
    unittest.main()
    