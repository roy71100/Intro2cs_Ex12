__author__ = 'T8631461'
NUM_OF_COL = 7
NUM_OF_ROW = 6
import tkinter as tk

class board:
    def __init__(self, root):
        self._root = root
        self._canvas = tk.Canvas(root, width=1000 ,height=800)
        self._button = tk.Label(root)
        frame = tk.Frame(root)
        frame.pack(side = tk.BOTTOM)
        self._canvas.pack()
        self._places = []
        self._column_high = [0] * NUM_OF_COL
        self._button.pack()
        self.build_columns_buttons(frame)
        self.turn = 0

    def All(self):
        y = 555
        for i in range(6):
            x = 255
            self._places.append([])
            for j in range(7):
                self._places[i].append(self._canvas.create_oval(x,y,x+90,y+90))
                x += 100
            y -= 100

    def paint(self, row, column, color):
        self._canvas.itemconfig((self._places[row][column]), fill = color)

    def build_columns_buttons(self, label):
        for col in range(NUM_OF_COL):
            button = tk.Button(label,text = str(col+1), bd = 15,
                               command = self.buttons_press(col))
            button.grid(row = 0, column = col)

    def buttons_press(self,col):
        def add_to_column():
            self.paint(self._column_high[col], col, "red")
            self._column_high[col] += 1
        return add_to_column

root = tk.Tk()
x = board(root)
img = tk.PhotoImage(file = "board.png")
x._canvas.create_image(600, 400, image=img)
x.All()

root.mainloop()


