class Game:
    BOARD_COLUMNS = 7
    BOARD_ROWS = 6
    BOARD_PROTOCOL = {"empty": 0, "player 1": 1, 'player 2': 2}
    GAME_STATUS = {'running': None, '1 won': 1, '2 won': 2, 'tie': 0}
    TURNS = {1: 'player 1', 2: 'player 2'}

    def __init__(self):
        self.board = [
            [Game.BOARD_PROTOCOL['empty'] for i in range(Game.BOARD_COLUMNS)]
            for i in range(Game.BOARD_ROWS)]
        self.turn = 'player 1'
        self.status = Game.GAME_STATUS['running']

    def __str__(self):
        result = ''
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                result += str(self.board[i][j])
            result+= '\n'
        return  result

    def make_move(self, column):
        if self.is_legal(column):
            column_data = [row[column] for row in self.board]
            self.board[column_data.index(Game.BOARD_PROTOCOL['empty'])][
                column] = Game.BOARD_PROTOCOL[self.turn]
            self.next_turn()
        else:
            raise Exception("ilegal move", column)

    def get_winner(self):
        return self.status

    def get_player_at(self, row, col):
        if self.board[row][col] == 0:
            return None
        return self.board[row][col]

    def get_current_player(self):
        return Game.BOARD_PROTOCOL[self.turn]

    def is_legal(self, column):
        if self.board[column].count(Game.BOARD_PROTOCOL['empty']) <= 0:
            return False
        elif column > Game.BOARD_COLUMNS - 1:
            return False
        if self.status != Game.GAME_STATUS['running']:
            return False
        return True

    def next_turn(self):
        if Game.BOARD_PROTOCOL[self.turn] == 1:
            self.turn = Game.TURNS[2]
        if Game.BOARD_PROTOCOL[self.turn] == 2:
            self.turn = Game.TURNS[1]

g = Game()

print(g)