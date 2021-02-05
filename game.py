from player import Human_player, Computer, SuperComputer
from os import system
from random import choice
from time import sleep


class tictactoe:
    def __init__(self):
        self.bord = [' ' for _ in range(9)]
        self.current_winer = None

    def available_moves(self):
        # return a list of available moves
        return [i+1 for i, _ in enumerate(self.bord) if _ == ' ']

    def playing_again(self):
        self.bord = [' ' for _ in range(9)]
        self.current_winer = None

    def print_bord(self):  # printing the game bord
        for row in [self.bord[j*3:(j+1)*3] for j in range(3)]:
            print('| '+str.join(' | ', row)+' |')

    @staticmethod
    def print_num_bord():  # printing the number bord for help in identify the square
        for row in [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]:
            print('| '+str.join(' | ', row)+' |')

    def check_winer(self, square: int, later: str):  # To check the winner of the game
        row_index = (square-1)//3
        row = self.bord[row_index*3:(row_index+1)*3]
        # if any row have laters are same as current mover then current mover is winner
        if all([(later == row_item) for row_item in row]):
            return True
        column_index = (square-1) % 3
        column = [self.bord[column_index+(i*3)] for i in range(3)]
        # if any column have laters are same as current mover then current mover is winner
        if all([(later == column_item) for column_item in column]):
            return True
        if (square-1) % 2 == 0:  # here we check for diagonal for evaluat the winner
            l_diagonal = [self.bord[4*i] for i in range(3)]
            if all([later == l_diagonal_item for l_diagonal_item in l_diagonal]):
                return True
            r_diagonal = [self.bord[2*i] for i in range(1, 4)]
            if all([later == r_diagonal_item for r_diagonal_item in r_diagonal]):
                return True
        return False

    def num_of_available_moves(self):
        return len(self.available_moves())

    def make_move(self, square, later):
        if self.bord[square-1] == ' ':
            self.bord[square-1] = later.upper()
            if self.check_winer(square, later):
                self.current_winer = later
            return True
        else:
            print("The move has been used try another available move")

        return False

    def play(self, x_player, o_player, print_bord=True):
        system('cls')
        plr = choice((x_player, o_player))
        if plr == x_player:
            print(f"The {x_player.name} going to move first")
        else:
            print(f"The {o_player.name} going to move first")
        sleep(2)
        system('cls')
        self.print_num_bord()
        while self.num_of_available_moves():
            if plr == x_player:
                square = x_player.get_move(self)
            else:
                square = o_player.get_move(self)
            if self.make_move(square, plr.later):
                if print_bord:
                    system('cls')
                    print(f"{plr.name} make move to {square}")
                    self.print_num_bord()
                    print()
                    self.print_bord()
            else:
                continue
            if self.current_winer:
                print(
                    f"The {x_player.name if x_player.later == self.current_winer else o_player.name} win the match")
                return
            plr = x_player if plr == o_player else o_player
        if not self.current_winer:
            print("The game is tie")


def setup_player(name, symbol):
    x_player = object
    o_player = object
    print('Choose other player from this list of player')
    print("1.Basic Computer\n2.AI Computer\n3.Human\n4.Exit")
    is_valid_choice = False
    while not is_valid_choice:
        choice = input("Enter your choice\n")
        try:
            choice = int(choice)
            if choice == 1:
                is_valid_choice = True
                if symbol == 'X':
                    x_player = Human_player(symbol, name)
                    o_player = Computer('O')
                else:
                    x_player = Computer('X')
                    o_player = Human_player(symbol, name)
            elif choice == 2:
                is_valid_choice = True
                if symbol == 'X':
                    x_player = Human_player(symbol, name)
                    o_player = SuperComputer('O')
                else:
                    x_player = SuperComputer('X')
                    o_player = Human_player(symbol, name)
            elif choice == 3:
                is_valid_choice = True
                other_player_name = input("Enter the name of other player\n")
                if symbol == 'X':
                    x_player = Human_player(symbol, name)
                    o_player = Human_player('O', other_player_name)
                else:
                    x_player = Human_player('X', other_player_name)
                    o_player = Human_player(symbol, name)
            elif choice == 4:
                exit(0)
            else:
                print("Please choose from the option")
        except ValueError:
            print('Invalid input')
    return x_player, o_player


if __name__ == '__main__':
    t = tictactoe()  # create an instance of tictactoe class
    name = input("Enter your good name\n")
    symbol = input("Enter your symbol ( X | O )\n").upper()
    while not (symbol.isalpha() and (symbol == 'X' or symbol == 'O')):
        print("You have enter incorrect symbol please try agin")
        symbol = input("Enter your symbol ( X | O )\n").upper()
    while True:
        x_player, o_player = setup_player(name, symbol)
        t.play(x_player, o_player)
        play_again = input(
            "You want to play again press 'Y' or to exit press any key\n")
        if play_again.upper() == 'Y':
            t.playing_again()
        else:
            exit(0)
