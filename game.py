from player import Human_player, Computer
from os import system


class tictactoe:
    def __init__(self):
        self.bord = [' ' for _ in range(9)]
        self.current_winer = None
        self.available_moves = [i+1 for i, _ in enumerate(self.bord)]

    def playing_again(self):
        self.bord = [' ' for _ in range(9)]
        self.current_winer = None
        self.available_moves = [i+1 for i, _ in enumerate(self.bord)]

    def print_bord(self):
        for row in [self.bord[j*3:(j+1)*3] for j in range(3)]:
            print('| '+str.join(' | ', row)+' |')

    @staticmethod
    def print_num_bord():
        for row in [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]:
            print('| '+str.join(' | ', row)+' |')

    def check_winer(self, square: int, later: str):
        row_index = (square-1)//3
        row = self.bord[row_index*3:(row_index+1)*3]
        if all([(later == row_item) for row_item in row]):
            return True
        column_index = (square-1) % 3
        column = [self.bord[column_index+(i*3)] for i in range(3)]
        if all([(later == column_item) for column_item in column]):
            return True
        if (square-1) % 2 == 0:
            l_diagonal = [self.bord[4*i] for i in range(3)]
            if all([later == l_diagonal_item for l_diagonal_item in l_diagonal]):
                return True
            r_diagonal = [self.bord[2*i] for i in range(1, 4)]
            if all([later == r_diagonal_item for r_diagonal_item in r_diagonal]):
                return True
        return False

    def num_of_available_moves(self):
        return len(self.available_moves)

    def make_move(self, square: int, later: str):
        if self.bord[square-1] == ' ':
            self.bord[square-1] = later.upper()
            self.available_moves.remove(square)
            if self.check_winer(square, later):
                self.current_winer = later.upper()
            return True
        else:
            print("The move has been used try another available move")

        return False


def play(game, x_player, y_player, print_bord=True):
    system('cls')
    plr = x_player
    game.print_num_bord()
    while game.num_of_available_moves():
        if plr == x_player:
            square = x_player.get_move(game)
        else:
            square = y_player.get_move(game)
        if game.make_move(square, plr.later):
            if print_bord:
                system('cls')
                print(f"{plr.later} player make move to {square}")
                game.print_num_bord()
                print()
                game.print_bord()
        else:
            continue
        if game.current_winer:
            print(f"The {game.current_winer} player win the match")
            return
        plr = x_player if plr == y_player else y_player


if __name__ == '__main__':
    t = tictactoe()
    x_player = Human_player('X')
    y_player = Computer('O')
    while True:
        play(t, x_player, y_player)
        play_again = input("You want to play again (Y/N)\n")
        if play_again.upper() == 'Y':
            t.playing_again()
        else:
            exit(0)
