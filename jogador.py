import math
import random

class player():
    def __init__(self, letter):
        # letter é X ou O
        self.letter = letter


    def get_move(self, game):
        pass

class randomcomputerplayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
class jogadorHumano(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\' vez. Escolha um campo(0-8):')
            # Noa vamos checar se isso é o valor correto quando tentamos castar
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, than yay!
            except ValueError:
                print ('Invalid square. Try again.')
        
        return val