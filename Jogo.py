from jogador import jogadorHumano, randomcomputerplayer
import time
 
class Velha:
    def __init__(self):
        self.tabuleiro = [' ' for _ in range(9)] # Vamos usar uma lista simples pra 3x3
        self.current_winner = None

    def print_board(self):
        # isso apenas pega os rows
        for row in [self.tabuleiro[i*3:(i+1)*3]for i in range(3)]: 
            print('|' + '|'.join(row) + '|')
    

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (fala pra gente qual o numero correspondente pra cada caixa)
        numver_board = [[str(i)for i in range(j*3, (j+1)*3)]for j in range(3)]
        for row in numver_board:
            print('|'+'|'.join(row)+'|')

    def available_moves(self):
        return[i for i, spot in enumerate(self.tabuleiro)if spot == ' '] # todo comentario abaixo é só essa linha aqui
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #    # ['x', 'x', 'o'] ----> [(0,'x'),(1,'x'),(2,'o')]
        #    if x == ' ':
        #        moves.append(i)
        # return moves
    def quadrados_vazios(self):
        return ' ' in self.tabuleiro

    def num_empty_squares(self):
        return self.tabuleiro.count(' ')

    def movimento(self, square, letter):
        # Ser for um movimento valido, então faça (designar a letra pro quadrado)
        # return true. if invalido, return else
        if self.tabuleiro[square] == ' ':
            self.tabuleiro[square] = letter
            if self.vencedor(square, letter):
                self.current_winner = letter
            return True
        return False

    def vencedor(self, square, letter):
        # Vence se acertar 3 seguidas em qualquer lugar. Precisamos checar isso
        # Chegar a rolagem
        row_ind = square // 3
        row = self.tabuleiro[row_ind*3:(row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        # checa a coluna
        col_ind = square % 3
        column = [self.tabuleiro[col_ind+i*3]for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # checar as  diagonais
        # só se o quadrado for um numero (0, 2, 4, 6, 8)
        # Unicos movimentos possiveis pra vencer na diagonal
        if square % 2 == 0:
            diagonal1 = [self.tabuleiro[i] for i in [0, 4, 8]] # Esquerda pra direita diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.tabuleiro[i] for i in [2, 4, 6]] # Direita pra esquerda diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # se tudo isso falhar
        return False

def jogar(game, x_player, o_player, print_game=True):
    # Retorna o vencedor do game(a letra)! ou nenhum se for um empate 
    if print_game:
        game.print_board_nums()

    letter = 'X' # Letra 
    # iterar enquanto o game continua com quadrados vazios
    # (Sem se preocupar com o vencedor isso a gente só retorna
    # que quebra o loop)

    while game.quadrados_vazios():
        # Pega o movimento
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # Definindo a função para fazer o movimento
        if game.movimento(square, letter):
            if print_game:
                print(letter + ' Fez um movimento {}'.format(square))
                game.print_board()
                print('') # Só uma linha vazia

            if game.current_winner:
                if print_game:
                    print(letter + ' Ganhou!')
                return letter

            # Depois de fazer nosso movimento, nos precisamos alternar as letras
            letter = 'O' if letter == 'X' else 'X' # Muda o jogador

        # Break para melhor entendimento
        time.sleep(.8)
        
    if print_game:
        print('Empatou')

if __name__ == '__main__':
    x_player = jogadorHumano('X')
    o_player = randomcomputerplayer('O')
    t = Velha()
    jogar(t, x_player, o_player, print_game=True)