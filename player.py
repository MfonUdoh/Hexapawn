from game_state import *

import label
import minimax


class Player(object):
    def __init__(self, color):
        self.color = color

    def make_move(self, state):
        state.draw_board()


class BotPlayer(object):
    def __init__(self, color):
        self.color = color
        self.solver = minimax.Minimax(self.color)

    def make_move(self, state):
        move, score = self.solver.minimax(state)
        return move


class HumanPlayer(object):
    def __init__(self, color):
        self.color = color

    def make_move(self, state):
        state.draw_board()
        print('Make a move, sir')

        pawn = None
        valid = False
        final_pos = None
        while not valid:
            print('Begin by selecting a pawn in a row and column')
            row = eval(input('Select a row: '))
            col = eval(input('Select a column: '))
            if (row in range(3)) and (col in range(3)):
                pawn = state.get_pawn(row, col, self.color)
                if pawn is not None:
                    valid = True
            print('Select a final position for the pawn')
            row = eval(input('Select a row: '))
            col = eval(input('Select a column: '))
            for moveset in state.get_available_moves():
                if repr(Move(pawn, Position(row, col))) == repr(moveset):
                    final_pos = Position(row, col)
                    valid = True
                    break
                else:
                    valid = False
            if valid == False:
                print ("Move not valid, try again.")

        return Move(pawn, final_pos)
