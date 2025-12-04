from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.new_x = 8
        self.new_y = 8
        self.move_speed = 0.1
    def move(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x + self.new_x, y + self.new_y)

    def ball_reset(self):
        self.goto(0,0)
        self.new_x *= -1
