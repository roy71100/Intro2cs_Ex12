class AI:
    def __init__(self, game, player):
        self.game = game
        self.number = player

    def find_legal_move(self, timeout=None):
        if self.game.get_winner() is None:
            for i in range(0, len(self.game[0])):
                if self.game.get_player_at(0, i) is None:
                    return i

        raise Exception("No possible AI moves")

    def get_last_found_move(self):
        pass
