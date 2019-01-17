__author__ = 'T8631461'
NUM_OF_COL = 7
NUM_OF_ROW = 6
X_START = 100
Y_START = 300
SIZE = 50
COLORS = {1: "red", 2: "blue", -1: "white"}
TIME_LEAP = 2000

import tkinter as tk
from . import game
from . import ai
from tkinter import messagebox


class GUI:
    """
        a class responsible for all the graphic interface of the game
    """

    def __init__(self, root):
        """Initialize the object (build the different part of the  interface)
        and start the event loop """
        self._game = game.Game()  # add a Game object that represents the game's logic
        self._root = root
        self._end_frame = tk.Frame(self._root)  # build end frame
        self._main_frame = tk.Frame(self._root)  # build the main frame of the game
        self._open_frame = tk.Frame(root)  # build the opening frame
        self.run = True
        self.open_buttons()  # start the game

    def players(self, frame, i):
        """this method build a window that allows the user to chose the
        the identity of one player"""
        title = tk.Label(frame, text="player " + str(i), font=("helvetica", 20))
        title.pack()
        h = tk.Button(frame, text="Human", command=self.player(0, i))
        h.pack()
        a = tk.Button(frame, text="AI", command=self.player(1, i))
        a.pack()

    def start_condition(self):
        """the method initialize the value of some member to
        there initial value"""
        self.turn = 1
        self.player_1 = -1
        self.player_2 = -1
        self._places = []
        self._column_high = [0] * NUM_OF_COL

    def players_option(self):
        """this method build a window that allows the user to chose the
        the identity of all the players"""
        frame_player_1 = tk.Frame(self._open_frame)  # chose player 1
        frame_player_1.pack()
        self.players(frame_player_1, 1)
        frame_player_2 = tk.Frame(self._open_frame)  # chose player 2
        frame_player_2.pack()
        self.players(frame_player_2, 2)

    def open_buttons(self):
        """this method build the opening screen of the game"""
        self._main_frame.destroy()
        self._end_frame.destroy()
        self._open_frame = tk.Frame(self._root)  # build frame
        self.start_condition()  # initialize members
        self._open_frame.pack()
        title = tk.Label(self._open_frame, text="FOUR IN A ROW",
                         font=("helvetica", 50))  # title
        title.pack()
        self.players_option()  # players choice

    def player(self, humans, players):
        """this function return the function that will
        be implemented if the button that allows the user to
        chose player is pressed"""

        def player():
            if players == 1:  # player 1
                if humans == 0:  # is a human
                    self.player_1 = 1
                else:  # is an Ai
                    self.player_1 = ai.AI(self._game)
            else:  # player 2
                if humans == 0:  # is a human
                    self.player_2 = 1
                else:
                    self.player_2 = ai.AI(self._game)  # is an ai
            if not self.player_1 == -1 and not self.player_2 == -1:
                # in case all the players have been chosen
                self.start_game()

        return player

    def start_game(self):
        """this method start the main game, all the players' actions in
        the game will happen in this function"""
        self.run = True
        self._main_frame.destroy()
        self._end_frame.destroy()
        self._open_frame.destroy()
        self._main_frame = tk.Frame()
        title = tk.Label(self._main_frame, text="FOUR IN A ROW",
                         font=("helvetica", 40))  # title
        title.pack()
        sub_frame_left = tk.Frame(self._main_frame)
        sub_frame_left.pack(side=tk.LEFT)
        self.turn = 1
        self.canvas = tk.Canvas(self._main_frame, width=500, height=400)
        self._results = tk.Label(sub_frame_left, text=str(self.turn) + " turn "
                                 , font=("helvetica", 40))
        self._results.pack(side=tk.TOP)
        frame = tk.Frame(self._main_frame)
        frame.pack(side=tk.BOTTOM)
        self.canvas.pack(side=tk.RIGHT)
        self._main_frame.pack()
        self.draw_circle()  # draw the "board"
        self._root.after(TIME_LEAP, self.ai_game)  # make ai moves
        self.build_columns_buttons(frame)  # build the game's button

    def ai_game(self):
        """this method will execute all the ai move, it will
        check if now is the turn of the ai and if it is play"""
        if type(self.player_1) is ai.AI and self.turn == 1 and self.run:
            col_new = self.player_1.find_legal_move()
            self.next_turn(col_new)
        if type(self.player_2) is ai.AI and self.turn == 2 and self.run:
            col_new = self.player_2.find_legal_move()
            self.next_turn(col_new)
        self._root.after(TIME_LEAP, self.ai_game)  # run the function again

    def draw_circle(self):
        """draws and add all the circle on the canvas that make the board """
        self.canvas.create_rectangle(90, 350, 450, 45, fill="green")
        y = Y_START
        for i in range(6):
            x = X_START
            self._places.append([])
            for j in range(7):
                self._places[i].append(self.canvas.create_oval(x, y, x + 40, y + 40))
                x += SIZE
            y -= SIZE

    def paint(self, row, column):
        """paint a given place in the board (based on the turn)"""
        self.canvas.itemconfig((self._places[row][column]),
                               fill=COLORS[self.turn])

    def build_columns_buttons(self, label):
        """build the game's buttons that give the user
        to add disk to the board"""
        for col in range(NUM_OF_COL):
            button = tk.Button(label, text=str(col + 1), bd=15,
                               command=self.buttons_press(col))
            button.grid(row=0, column=col)

    def buttons_press(self, col):
        """return the function that will be execute when the user press
        a button in order to add a disk to the game"""

        def add_to_column():
            if (self.turn == 1 and type(self.player_1) == int) or \
                    (self.turn == 2 and type(self.player_2)
                     == int) and self.run:
                self.next_turn(col)  # add a disk to the right column and make a
                # full move

        return add_to_column

    def next_turn(self, col):
        try:
            self._game.make_move(col)  # "update" the gae that a move
            # was done
            self.paint(self._column_high[col], col)  # paint the right place
            self._column_high[col] += 1  # change the column high
            self.turn = self._game.get_current_player()
            self._results.configure(text=str(self.turn) + " turn ")
            winner, list_of_cord = self._game.get_winner_helper()  # check if the
            # game ended and how
            if not winner is None:
                self.turn = -1
                if winner == 0:
                    self._results.configure(text="game ended in tie")
                else:
                    self._results.configure(text="the winner is: " +
                                                 str(winner))
                    for i in list_of_cord:
                        self.paint(NUM_OF_ROW - i[1] - 1, i[0])  #
                        # paint win sequence
                self.end_option()
        except Exception as e:  # illegal move
            messagebox.showerror("Error", str(e))

    def end_option(self):
        """end the game , gives the user the option to another game
        or to start a game with different setting"""
        self.clear()
        self._end_frame = tk.Frame(self._root)
        end_message = tk.Label(self._end_frame, text
        ="would you want to change something?"
                               , font=("helvetica", 20))
        self._end_frame.pack()
        end_message.pack()
        yes = tk.Button(self._end_frame, text="Yes", command=self.open_buttons)
        yes.pack()
        no = tk.Button(self._end_frame, text="No", command=self.start_game)
        no.pack()
        self.init_ai()

    def init_ai(self):
        """update to ai after a new game is started"""
        if type(self.player_1) == ai.AI:
            self.player_1 = ai.AI(self._game)
        if type(self.player_2) == ai.AI:
            self.player_2 = ai.AI(self._game)

    def clear(self):
        """clear the game board in the end of a game"""
        self.run = False
        self._game = game.Game()
        self._column_high = [0] * NUM_OF_COL
