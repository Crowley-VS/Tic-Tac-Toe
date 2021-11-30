from unittest import TestCase
from tic_tac_toe import Board
import utils

class TestTicTacToe(TestCase):
    def setUp(self) -> None:
        '''Initialize a board'''
        self.board = Board()
    def test_accept_move(self):
        '''Check whetther the board accepts move, raises excpetions when needed,
        and changed the value of the coordinate given.'''
        with self.assertRaises(utils.InvalidSign):
            for sign in ['0', 'H', 10, -11, 'x']:
                self.board.accept_move(1, 1, sign)
        with self.assertRaises(utils.InvalidCoordinate):
            for coordinate_row in range(5):
                for coordinate_col in range(3, 5):
                    self.board.accept_move(coordinate_row, coordinate_col, 'X')
        for sign in ['X', 'O']:
            for coordinate_row in range(3):
                for coordinate_col in range(3):
                    self.board.accept_move(coordinate_row, coordinate_col, sign)
                    value = self.board.coordinates[coordinate_row][coordinate_col]
                    self.assertEqual(value, sign)
    def test_check(self):
        '''Test if check algorithm determines the winner correctly'''
        for coordinate_row in range(3):
            for coordinate_col in range(3):
                self.board.accept_move(coordinate_row, coordinate_col, 'O')
            self.assertTrue(self.board.check('O'))
            self.board.clean()
        for coordinate_col in range(3):
            for coordinate_row in range(3):
                self.board.accept_move(coordinate_row, coordinate_col, 'O')
            self.assertTrue(self.board.check('O'))
            self.board.clean()
        for coordinate_row, coordinate_col in [[0,0], [1,1], [2,2]]:
            self.board.accept_move(coordinate_row, coordinate_col, 'O')
        self.assertTrue(self.board.check('O'))
        self.board.clean()
        for coordinate_row, coordinate_col in [[0,2], [1,1], [2,0]]:
            self.board.accept_move(coordinate_row, coordinate_col, 'O')
        self.assertTrue(self.board.check('O'))
        self.board.clean()
        for coordinate_row in range(3):
            for coordinate_col in range(2):
                self.board.accept_move(coordinate_row, coordinate_col, 'O')
            self.assertFalse(self.board.check('O'))
            self.board.clean()

