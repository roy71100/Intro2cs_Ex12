class Game:
    BOARD_COLUMNS = 7
    BOARD_ROWS = 6
    BOARD_PROTOCOL = {"empty": 0, "player 1": 1, 'player 2': 2}
    GAME_STATUS = {'running': None, 'player 1': 1, 'player 2': 2, 'tie': 0}
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
            result += '\n'
        return result

    def make_move(self, column):
        if self.is_legal(column):
            column_data = [row[column] for row in self.board]
            self.board[(len(column_data) - 1) - column_data[::-1].index(
                Game.BOARD_PROTOCOL['empty'])][
                column] = Game.BOARD_PROTOCOL[self.turn]
            self.next_turn()
        else:
            raise Exception("illegal move.")

    def get_winner(self):
        # check rows
        for i in range(Game.BOARD_ROWS ):
            seq = self.return_sequence(1, 0, 0, i)

            for p in Game.BOARD_PROTOCOL.keys():
                if p != "empty":
                    if seq.count(Game.BOARD_PROTOCOL[p]) >= 4:
                        self.status = Game.GAME_STATUS[p]
                        return self.status
        # check columns
        for i in range(Game.BOARD_COLUMNS ):
            seq = self.return_sequence(0, 1, i, 0)

            for p in Game.BOARD_PROTOCOL.keys():
                if p != "empty":
                    if seq.count(Game.BOARD_PROTOCOL[p]) >= 4:
                        self.status = Game.GAME_STATUS[p]
                        return self.status
        # check diagonal /
        for i in range(Game.BOARD_COLUMNS - 3):
            seq = self.return_sequence(1, -1, i, Game.BOARD_ROWS - 1)
            for p in Game.BOARD_PROTOCOL.keys():
                if p != "empty":
                    if seq.count(Game.BOARD_PROTOCOL[p]) >= 4:
                        self.status = Game.GAME_STATUS[p]
                        return self.status
        for i in range(Game.BOARD_ROWS-2, 2, -1):
            seq = self.return_sequence(1, -1, 0, i)
            for p in Game.BOARD_PROTOCOL.keys():
                if p != "empty":
                    if seq.count(Game.BOARD_PROTOCOL[p]) >= 4:
                        self.status = Game.GAME_STATUS[p]
                        return self.status

        # check diagonal \
        for i in range(Game.BOARD_COLUMNS-1,2,-1):
            seq = self.return_sequence(-1, -1, i, Game.BOARD_ROWS - 1)
            print("diag1: {}".format(seq))
            for p in Game.BOARD_PROTOCOL.keys():
                if p != "empty":
                    if seq.count(Game.BOARD_PROTOCOL[p]) >= 4:
                        self.status = Game.GAME_STATUS[p]
                        return self.status

        for i in range(Game.BOARD_ROWS-2, 2, -1):
            seq = self.return_sequence(-1, -1, Game.BOARD_COLUMNS-1, i)
            print("diag: {}".format(seq))
            for p in Game.BOARD_PROTOCOL.keys():
                if p != "empty":
                    if seq.count(Game.BOARD_PROTOCOL[p]) >= 4:
                        self.status = Game.GAME_STATUS[p]
                        return self.status

    def return_sequence(self, delta_x, delta_y, x, y):
        seq = []
        while (
                    (Game.BOARD_COLUMNS - 1 >= x >= 0) and (
                                0 <= y <= Game.BOARD_ROWS-1)):
            seq.append(self.board[y][x])
            x += delta_x
            y += delta_y
        return seq

    def get_player_at(self, row, col):
        if col <= Game.BOARD_COLUMNS - 1:
            if row <= Game.BOARD_ROWS - 1:
                if self.board[row][col] == 0:
                    return None
                return self.board[row][col]
        raise Exception("illegal location.")

    def get_current_player(self):
        return Game.BOARD_PROTOCOL[self.turn]

    def is_legal(self, column):
        if column > Game.BOARD_COLUMNS - 1:
            return
        column_data = [row[column] for row in self.board]
        if column_data.count(Game.BOARD_PROTOCOL['empty']) <= 0:
            return False
        if self.status != Game.GAME_STATUS['running']:
            return False
        return True

    def next_turn(self):
        if Game.BOARD_PROTOCOL[self.turn] == 1:
            self.turn = Game.TURNS[2]
        elif Game.BOARD_PROTOCOL[self.turn] == 2:
            self.turn = Game.TURNS[1]


