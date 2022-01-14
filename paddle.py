from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("orange")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x, 0)

    def move_up(self):
        curx = self.xcor()
        cury = self.ycor()
        self.goto(curx, cury + 20)

    def move_down(self):
        curx = self.xcor()
        cury = self.ycor()
        self.goto(curx, cury - 20)



