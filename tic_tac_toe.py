from utils import Draw, InvalidSign, InvalidCoordinate, PreoccupiedCell, Victory
from random import choice
class Board:
    '''A 3x3 board for playing tic-tac-toe that accepts moves from players.'''
    def __init__(self):
        '''Initialize a clean board.'''
        self.clean()
        self.nought = 'O'
        self.cross = 'X'
    def accept_move(self, coordinate_row, coordinate_col, sign):
        '''Place the given sign into the corresponding coordinate.
        Coordinate is a string of 2 digits. 1st is a row, 2nd is a column.
        Sign is either 'X' or 'O'. If there's already something in
        the given cell, then raise an exception'''
        try:
            if sign not in ['X', 'O']:
                raise InvalidSign
            else:
                coordinate_row = int(coordinate_row)
                coordinate_col = int(coordinate_col)
                if self.coordinates[coordinate_row][coordinate_col] != ' ':
                    raise PreoccupiedCell
                self.coordinates[coordinate_row][coordinate_col] = sign
        except IndexError:
            raise InvalidCoordinate
        except ValueError:
            raise InvalidCoordinate
    def check(self, sign):
        '''Check whether someone won or not.'''
        for i in range(3):
            if self.coordinates[i][0] == self.coordinates[i][1] == self.coordinates[i][2] == sign:
                raise Victory(sign)
            elif self.coordinates[0][i] == self.coordinates[1][i] == self.coordinates[2][i] == sign:
                raise Victory(sign)
        if self.coordinates[0][0] == self.coordinates[1][1] == self.coordinates[2][2] == sign:
            raise Victory(sign)
        elif self.coordinates[0][2] == self.coordinates[1][1] == self.coordinates[2][0] == sign:
            raise Victory(sign)
        elif self.determine_unocuppied_cells() == []: #if we checked all cases before, and the board is full, then it's a draw
            raise Draw(sign)
    def determine_unocuppied_cells(self):
        '''Rerurn a list of all coordinates of the possible moves.'''
        moves = []
        for row_i in range(3):
            for col_i in range(3):
                if self.coordinates[row_i][col_i] == ' ':
                    moves.append((row_i, col_i))
        return moves
    def clean(self):
        '''Clean the board'''
        self.coordinates = [[' ', ' ', ' '],
                            [' ', ' ', ' '],
                            [' ', ' ', ' ']]
class Bot:
    '''Represents a robot that plays against the player'''
    def __init__(self, board):
        self.board = board
    def move(self, sign):
        '''Make a random move.'''
        move = choice(self.board.determine_unocuppied_cells())
        coordinate_row = move[0]
        coordinate_col = move[1]
        self.board.accept_move(coordinate_row, coordinate_col, sign)
