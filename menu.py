from tic_tac_toe import Board, Bot
from random import choice, randint
class Menu:
    '''Display a menu and respond to answers.
    Initiate a game when needed.'''
    def __init__(self):
        self.board = Board()
        self.bot = Bot(self.board)
        self.choices = {
            '1': self.start_game,
            '2': self.quit
        }
    def render_menu(self):
        print('Tic-Tac_Toe\n')
        print('1: Start a game')
        print('2: Quit')
    def render_board(self):
        i=0 #counter that determines whether print the last line or not, also used as a display coordinate
        print('  {0}'.format('   '.join(['0', '1', '2'])))
        for row in self.board.coordinates:
            if i!=2:
                print('{0} {1}'.format(i, ' | '.join(row)))
                print('  {0}'.format('-'*9))
            else:
                print('{0} {1}'.format(i, ' | '.join(row)))
            i+=1
    def start_game(self):
        sign_pl, sign_bot = self.choose_sign()
        print('Your sign is {0}, Bot\'s sign is {1}'.format(sign_pl, sign_bot))
        while True:
            self.render_board()
            coordinate_row = input('Enter the row coordinate: ')
            coordinate_col = input('Enter the column coordinate: ')
            self.board.accept_move(coordinate_row, coordinate_col, sign_pl)
    def choose_sign(self):
        signs = ['X', 'O']
        return signs.pop(randint(0, 1)), signs.pop()
    def quit(self):
        pass
if __name__ == '__main__':
    Menu().start_game()