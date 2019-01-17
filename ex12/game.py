class Game:
    """
    the Game class representing a game of 4 in a row.
    """
    BOARD_COLUMNS = 7
    BOARD_ROWS = 6
    BOARD_PROTOCOL = {"empty": 0, "player 1": 1, 'player 2': 2}
    GAME_STATUS = {'running': None, 'player 1': 1, 'player 2': 2, 'tie': 0}
    TURNS = {1: 'player 1', 2: 'player 2'}

    def __init__(self):
        """
        the initializing method for the game class. creates a gamr object
        containing a board, turn and status attribute.
        """
        self.board = [
            [Game.BOARD_PROTOCOL['empty'] for i in range(Game.BOARD_COLUMNS)]
            for i in range(Game.BOARD_ROWS)]
        self.turn = 'player 1'
        self.status = Game.GAME_STATUS['running']

    def __str__(self):
        """
        a method for printing the state of the board for debugging.
        """
        result = ''
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                result += str(self.board[i][j])
            result += '\n'
        return result

    def make_move(self, column):
        """
        a method receiving a column number, updating the board status if its
        legal. otherwise, raising an exception "illegal move.".

        """
        if self.is_legal(column):
            column_data = [row[column] for row in self.board]
            self.board[(len(column_data) - 1) - column_data[::-1].index(
                Game.BOARD_PROTOCOL['empty'])][
                column] = Game.BOARD_PROTOCOL[self.turn]
            self.next_turn()
        else:
            raise Exception("illegal move.")

    def get_winner(self):
        """
        a method which checks whether there is a winner, and return the answer:
        1 - player one won, 2- player two won, 0 - tie, None - still running.
        :return:
        """
        status, coord = self.get_winner_helper()
        self.status = status
        return status

    def get_winner_helper(self):
        """
        a method which checks whether there is a winner, and return the answer:
        1 - player one won, 2- player two won, 0 - tie, None - still running.
        if there is a winner, it also returns the coordinates of the winning
        streak, otherwise, return None.
        winner: status, [coordinates]
        tie/running: status, None
        """
        # check rows
        for i in range(Game.BOARD_ROWS):
            seq = self.return_sequence(1, 0, 0, i)
            for p in Game.BOARD_PROTOCOL.keys():
                if p != "empty":
                    result, coord = check_4_in_a_row(seq,
                                                     Game.BOARD_PROTOCOL[p])
                    if result:
                        return Game.GAME_STATUS[p], coord

        # check columns
        for i in range(Game.BOARD_COLUMNS):
            seq = self.return_sequence(0, 1, i, 0)
            for p in Game.BOARD_PROTOCOL.keys():
                if p != "empty":
                    result, coord = check_4_in_a_row(seq,
                                                     Game.BOARD_PROTOCOL[p])
                    if result:
                        return Game.GAME_STATUS[p], coord

        # check diagonal /
        for i in range(Game.BOARD_COLUMNS - 3):
            seq = self.return_sequence(1, -1, i, Game.BOARD_ROWS - 1)
            for p in Game.BOARD_PROTOCOL.keys():
                if p != "empty":
                    result, coord = check_4_in_a_row(seq,
                                                     Game.BOARD_PROTOCOL[p])
                    if result:
                        return Game.GAME_STATUS[p], coord

        for i in range(Game.BOARD_ROWS - 2, 2, -1):
            seq = self.return_sequence(1, -1, 0, i)
            for p in Game.BOARD_PROTOCOL.keys():
                if p != "empty":
                    result, coord = check_4_in_a_row(seq,
                                                     Game.BOARD_PROTOCOL[p])
                    if result:
                        return Game.GAME_STATUS[p], coord

        # check diagonal \
        for i in range(Game.BOARD_COLUMNS - 1, 2, -1):
            seq = self.return_sequence(-1, -1, i, Game.BOARD_ROWS - 1)
            for p in Game.BOARD_PROTOCOL.keys():
                if p != "empty":
                    result, coord = check_4_in_a_row(seq,
                                                     Game.BOARD_PROTOCOL[p])
                    if result:
                        return Game.GAME_STATUS[p], coord

        for i in range(Game.BOARD_ROWS - 2, 2, -1):
            seq = self.return_sequence(-1, -1, Game.BOARD_COLUMNS - 1, i)
            for p in Game.BOARD_PROTOCOL.keys():
                if p != "empty":
                    result, coord = check_4_in_a_row(seq,
                                                     Game.BOARD_PROTOCOL[p])
                    if result:
                        return Game.GAME_STATUS[p], coord

        # checking whether its a tie.
        if len((filter(lambda x: x == Game.BOARD_PROTOCOL['empty'],
                           [item for sublist in self.board for item in
                            sublist]))) == 0:
            return Game.GAME_STATUS['tie'], None

        # game still running
        return Game.GAME_STATUS['running'], None

    def return_sequence(self, delta_x, delta_y, x, y):
        """
        a method receiving a direction (represented by delta_x and delta_y) and
        a starting position, and return a list of values encountered upon
        advancing that direction in the board matrix:
        [value,coordinates] when coordinates = (x,y).
        """
        seq = []
        while (
                    (Game.BOARD_COLUMNS - 1 >= x >= 0) and (
                                0 <= y <= Game.BOARD_ROWS - 1)):
            seq.append([self.board[y][x], (x, y)])
            x += delta_x
            y += delta_y
        return seq

    def get_player_at(self, row, col):
        """
        a method receiving a position on the matrix, and returns which player
        is on that position: 1- player one, 2- player 2, 0- empty. the method
        raise an exception if an illegal place was reached, "illegal location".
        """
        if col <= Game.BOARD_COLUMNS - 1:
            if row <= Game.BOARD_ROWS - 1:
                if self.board[row][col] == 0:
                    return None
                return self.board[row][col]
        raise Exception("illegal location.")

    def get_current_player(self):
        """
        a method returning the current player who suppose to play up next.
        """
        return Game.BOARD_PROTOCOL[self.turn]

    def is_legal(self, column):
        """
        a method receiving a column and returning whether a new disc
        can be placed there.
        """
        if column > Game.BOARD_COLUMNS - 1:
            return False
        column_data = [row[column] for row in self.board]
        if column_data.count(Game.BOARD_PROTOCOL['empty']) <= 0:
            return False
        if self.status != Game.GAME_STATUS['running']:
            return False
        return True

    def next_turn(self):
        """
        a method returning the player who plays the next turn.
        """
        if Game.BOARD_PROTOCOL[self.turn] == 1:
            self.turn = Game.TURNS[2]
        elif Game.BOARD_PROTOCOL[self.turn] == 2:
            self.turn = Game.TURNS[1]


def check_4_in_a_row(list, value):
    """
    a method receiving a list with values and cordinates, return True if there
    are 4 elemments in a row with the specified value, and their coordinates.
    False and None otherwise
    """
    coordinates = []
    count = 0
    for e in list:
        if e[0] == value:
            count += 1
            coordinates.append(e[1])
            if count >= 4:
                return True, coordinates
        else:
            count = 0
            coordinates = []
    return False, None
