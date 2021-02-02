import random
from time import sleep


class Player:
    def __init__(self, later, name):
        self.later = later
        self.name = name

    def get_move(self, game):
        pass


class Computer(Player):
    def __init__(self, later, name):
        super().__init__(later, name)

    def get_move(self, game):
        sleep(3)
        return random.choice(game.available_moves)


class Human_player(Player):
    def __init__(self, later, name):
        super().__init__(later, name)

    def get_move(self, game):
        val = None
        # moves = [i+1 for i in game.available_moves]
        while not val:
            print("Your symbol is X")
            val = input(
                f"Choose {self.name} from this available moves {game.available_moves}\n")
            try:
                val = int(val)
                if val < 1 or val > 9:
                    raise ValueError
            except ValueError:
                print("Invalid input try again")
                val = None
        return val
