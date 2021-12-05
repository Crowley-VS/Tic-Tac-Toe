from tic_tac_toe import Board, Bot
from random import choice, randint
import sys
from utils import Draw, InvalidCoordinate, PreoccupiedCell, Victory

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
    def run(self):
        '''Display a menu and respond to choices.'''
        while True:
            self.render_menu()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print('{0} is not a valid choice'.format(choice))
    def render_menu(self):
        '''Display a menu'''
        print('Tic-Tac_Toe\n')
        print('1: Start a game')
        print('2: Quit')
    def render_board(self):
        '''Display a board'''
        i=0 #counter that determines whether to print the last line or not to, also used as a display coordinate
        print('  {0}'.format('   '.join(['0', '1', '2'])))
        for row in self.board.coordinates:
            if i!=2:
                print('{0} {1}'.format(i, ' | '.join(row)))
                print('  {0}'.format('-'*9))
            else:
                print('{0} {1}'.format(i, ' | '.join(row)))
            i+=1
    def player_move(self, sign_pl):
        '''Accept a move from player, respond to the coordinates given.
        Render a board after accepting the move.'''
        while True:
            print('It\'s your turn.')
            self.render_board()
            coordinate_row = input('Enter the row coordinate: ')
            coordinate_col = input('Enter the column coordinate: ')
            try:
                self.board.accept_move(coordinate_row, coordinate_col, sign_pl)
            except InvalidCoordinate:
                print('Please enter valid coordinates!')
            except PreoccupiedCell:
                print('Cell you\'re trying to make your move to is already occupied!')
            else:
                print('You\'ve made your move.')
                self.render_board()
                break
    def bot_move(self, sign_bot):
        '''Accept a move from a bot. Render a board after accepting the move.'''
        self.bot.move(sign_bot)
        print('Bit\'s made its move.')
        self.render_board()
    def start_game(self):
        '''Initiate a new game, clean the board, assign sings to a player and a bot.'''
        self.board.clean()
        sign_pl, sign_bot = self.choose_sign()
        print('Your sign is {0}, Bot\'s sign is {1}'.format(sign_pl, sign_bot))
        while True:
            try:
                self.player_move(sign_pl)
                self.board.check(sign_pl)
                self.bot_move(sign_bot)
                self.board.check(sign_bot)
            except Victory as v:
                if v.sign == sign_pl:
                    print('Congratulations! You\'ve won!')
                else:
                    print('Sorry. Bot\'s won.')
                break
            except Draw:
                print('It\'s a draw!')
                break
    def choose_sign(self):
        signs = ['X', 'O']
        return signs.pop(randint(0, 1)), signs.pop()
    def quit(self):
        print('Goodbye!')
        sys.exit(0)
if __name__ == '__main__':
    Menu().run()