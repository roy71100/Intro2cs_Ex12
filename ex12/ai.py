from random import randint
from . import game


class AI:
    """
    a class representing an AI object which plays 4 in a row.
    """

    def __init__(self, game):
        """
        the initializng method of the AI, which gets a game object.
        """
        self.game = game

    def find_legal_move(self, timeout=None):
        """
        a method which finds a legal move which the AI can do.
        """
        if self.game.get_winner() is None:
            guess = randint(0, game.Game.BOARD_COLUMNS - 1)
            while self.game.get_player_at(0, guess) is not None:
                guess = randint(0, game.Game.BOARD_COLUMNS - 1)
            return guess
        raise Exception("No possible AI moves")

    def get_last_found_move(self):
        pass
