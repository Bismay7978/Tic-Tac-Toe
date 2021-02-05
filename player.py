import random
from time import sleep
import math


class Player:
    def __init__(self, later, name, player_ID):
        self.later = later
        self.name = name
        self.player_ID = player_ID

    def get_move(self, game):
        pass


class Computer(Player):

    def __init__(self, later, name='Basic Computer'):
        super().__init__(later, name, 1)

    def get_move(self, game):
        sleep(1.5)
        return random.choice(game.available_moves())


class Human_player(Player):
    def __init__(self, later, name):
        super().__init__(later, name, 2)

    def get_move(self, game):
        val = None
        # moves = [i+1 for i in game.available_moves]
        while not val:
            print(f"Your symbol is {self.later}")
            val = input(
                f"Choose {self.name} from this available moves {sorted(game.available_moves())}\n")
            try:
                val = int(val)
                if val < 1 or val > 9:
                    raise ValueError
            except ValueError:
                print("Invalid input try again")
                val = None
        return val


class SuperComputer(Player):

    def __init__(self, later, name='AI Computer'):
        super().__init__(later, name, 3)

    # it is a MINMAX algorithm which maximizes the wining chance of Super computer while minimizes the wining chance other player
    def perfect_move(self, game, player):
        other_player = 'X' if player == 'O' else 'O'
        # base case if we have the current winer then or the game tie then it return the associate score
        if game.current_winer:
            # the score for winer identifies that if the player is super computer then it is positive else for other player it gives negative value. The main use is to calculate the best move for the super computer
            return {'position': None, 'score': game.num_of_available_moves()+1 if game.current_winer == self.later else -1*(game.num_of_available_moves()+1)}
        elif not game.num_of_available_moves():
            # if the game is tai then return score 0 for all player
            return {'position': None, 'score': 0}
        # initialize the best move for different player
        if player == self.later:
            # if the player is super computer then best move should be maximize for increase the chance of wining the super computer
            best_move = {'position': None, 'score': -math.inf}
        else:
            # if the player is other than super computer then best move should be minimize for increase the chance of wining the super computer
            best_move = {'position': None, 'score': math.inf}
        for move in game.available_moves():
            # make a posible move form available move by current player
            game.make_move(move, player)
            # recursivly call the method to calculate the best move of both player
            temp_move = self.perfect_move(game, other_player)
            temp_move['position'] = move
            # finding the best move for both player
            # it checks best move for super computer by checking max score
            if player == self.later and temp_move['score'] > best_move['score']:
                best_move = temp_move
            # it checks best move for other player by checking min score
            elif player != self.later and temp_move['score'] < best_move['score']:
                best_move = temp_move
            # reset all moves(Back tracking)
            game.bord[move-1] = ' '
            # reset current winer to none
            game.current_winer = None
        return best_move

    def get_move(self, game):
        if game.num_of_available_moves() == 9:
            return random.choice(game.available_moves())
        return self.perfect_move(game, self.later).get('position')
