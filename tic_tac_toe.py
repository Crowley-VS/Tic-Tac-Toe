from utils import InvalidSign, InvalidCoordinate

class Board:
    '''A 3x3 board for playing tic-tac-toe that accepts moves from players.'''
    def __init__(self):
        '''Initialize a clean board.'''
        self.clean()
        self.nought = 'O'
        self.cross = 'X'
    def accept_move(self, coordinate_row, coordinate_col, sign):
        '''Place given sign into the corresponding coordinate.
        Coordinate is a string of 2 digits. 1st is a row, 2nd is a column.
        Sign is either 'X' or 'O' '''
        try:
            if sign not in ['X', 'O']:
                raise InvalidSign
            else:
                self.coordinates[coordinate_row][coordinate_col] = sign
        except IndexError:
            raise InvalidCoordinate
    def check(self, sign):
        '''Check whether someone won or not.'''
        for i in range(3):
            if self.coordinates[i][0] == self.coordinates[i][1] == self.coordinates[i][2] == sign:
                return True
            elif self.coordinates[0][i] == self.coordinates[1][i] == self.coordinates[2][i] == sign:
                return True
        if self.coordinates[0][0] == self.coordinates[1][1] == self.coordinates[2][2] == sign:
            return True
        elif self.coordinates[0][2] == self.coordinates[1][1] == self.coordinates[2][0] == sign:
            return True
        else:
            False
    def clean(self):
        '''Clean the board'''
        self.coordinates = [[' ', ' ', ' '],
                            [' ', ' ', ' '],
                            [' ', ' ', ' ']]