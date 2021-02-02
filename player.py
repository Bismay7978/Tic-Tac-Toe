import random


class Player:
    def __init__(self, later):
        self.later = later

    def get_move(self, game):
        pass


class Computer(Player):
    def __init__(self, later):
        super().__init__(later)

    def get_move(self, game):
        return random.choice(game.available_moves)


class Human_player(Player):
    def __init__(self, later):
        super().__init__(later)

    def get_move(self, game):
        val = None
        # moves = [i+1 for i in game.available_moves]
        while not val:
            val = input(
                f"Choose {self.later} player from this available moves {game.available_moves}\n")
            try:
                val = int(val)
                if val < 1 or val > 9:
                    raise ValueError
            except ValueError:
                print("Invalid input try again")
                val = None
        return val
