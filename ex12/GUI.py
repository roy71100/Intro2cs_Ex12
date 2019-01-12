__author__ = 'T8631461'
NUM_OF_COL = 7
NUM_OF_ROW = 6
COLORS = {1: "red", 2: "blue"}

import tkinter as tk
import ex12.game as game
from tkinter import messagebox

class board:
    def __init__(self, root):
        self._game = game.Game()
        self._root = root
        #self._open_frame = tk.Frame(root)
        #self.open_buttons(self._open_frame)
        self._title = tk.Label(root,text = "FOUR IN A ROW", font = ("helvetica", 40))
        self._title.pack()
        self._main_frame = tk.Frame()
        self._sub_frame_left = tk.Frame(self._main_frame)
        self._sub_frame_left.pack(side = tk.LEFT)
        self.turn = 1
        self.status = str(self.turn) + " turn "
        self._canvas = tk.Canvas(self._main_frame, width=500 ,height=400)
        self._results = tk.Label(self._sub_frame_left,text = self.status, font = ("helvetica", 20))
        self._results.pack(side = tk.TOP)
        frame = tk.Frame(root)
        frame.pack(side = tk.BOTTOM)
        self._canvas.pack(side = tk.RIGHT)
        self._places = []
        self._column_high = [0] * NUM_OF_COL
        self._main_frame.pack()
        self.All()
        self.build_columns_buttons(frame)

    #def open_buttons(self, frame):

    def All(self):
        rec = self._canvas.create_rectangle(90,350,450, 45, fill ="green")
        y = 300
        for i in range(6):
            x = 100
            self._places.append([])
            for j in range(7):
                self._places[i].append(self._canvas.create_oval(x,y,x+40,y+40))
                x += 50
            y -= 50

    def paint(self, row, column):
        self._canvas.itemconfig((self._places[row][column]),
                                fill = COLORS[self.turn])

    def build_columns_buttons(self, label):
        for col in range(NUM_OF_COL):
            button = tk.Button(label,text = str(col+1), bd = 15,
                               command = self.buttons_press(col))
            button.grid(row = 0, column = col)

    def buttons_press(self, col):
        def add_to_column():
            try:
                self._game.make_move(col)
                self.paint(self._column_high[col], col)
                self._column_high[col] += 1
                self.turn = self._game.get_current_player()
                self._results.configure(text = str(self.turn) + " turn ")
                if not self._game.get_winner() is None:
                    self._results.configure(text = "the winner is: " + str(self._game.get_winner()))
                    self.clear()
            except Exception:
                messagebox.showerror("Error", "Error message")
        return add_to_column

    def clear(self):
        for j in range(NUM_OF_ROW):
            for i in self._places[j]:
                self._canvas.itemconfig(i, fill = "white")
        self._game = game.Game()
        self._column_high = [0] * NUM_OF_COL
        self.turn = 1

root = tk.Tk()
x = board(root)
root.mainloop()


