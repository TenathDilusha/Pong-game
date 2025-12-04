from turtle import Turtle

class Slider(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def go_up(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x, y + 20)

    def go_down(self):
        y = self.ycor()
        x = self.xcor()
        self.goto(x, y - 20)