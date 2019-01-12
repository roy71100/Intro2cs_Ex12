import tkinter as tki
import random

CANVAS_SIZE = 500
BALL_SIZE = 20
STEP_SIZE = 5

class MyApp:
    def __init__(self,parent):
        self._parent = parent

        # add a canvas to draw on
        self._canvas = tki.Canvas(parent, width=CANVAS_SIZE,
                                  height=CANVAS_SIZE,
                                  highlightbackground='black')
        self._canvas.pack()

        # add a button
        button = tki.Button(parent, text="Add", command=self._add_ball)
        button.pack()
        self._balls = []
        self._move()

    def _add_ball(self):
        x = random.randrange(CANVAS_SIZE-BALL_SIZE)
        y = random.randrange(CANVAS_SIZE-BALL_SIZE)
        self._balls.append(self._canvas.create_oval(x, y, x+BALL_SIZE, y+BALL_SIZE))

    def _move(self):
        for ball in self._balls:
            x1,y1,x2,y2 = self._canvas.coords(ball)
            dx = int((random.random()-0.5)*2*STEP_SIZE)
            dy = int((random.random()-0.5)*2*STEP_SIZE)
            if x1+dx<0 or x2+dx>CANVAS_SIZE:
                dx = 0

            if y1+dy<0 or y2+dy>CANVAS_SIZE:
                dy = 0
            self._canvas.move(ball,dx,dy)

        self._parent.after(10,self._move)

root = tki.Tk()
MyApp(root)
root.mainloop()

