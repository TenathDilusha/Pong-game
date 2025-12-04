from turtle import Screen, Turtle
from paddle import Slider
from ball import Ball
import time
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(800, 600)
my_screen.title("Pong Game")
my_screen.tracer(0)

left_slider = Slider(-350, 0)
right_slider = Slider(350, 0)

my_ball = Ball()
my_scoreboard = Scoreboard()

line = Turtle()
line.hideturtle()
line.color("white")
line.penup()
line.goto(0, 300)
while line.ycor() > -300:
    y = line.ycor()
    line.penup()
    line.goto(0, y - 10)
    y = line.ycor()
    line.pendown()
    line.goto(0, y - 10)
line.pendown()

my_screen.listen()
my_screen.onkey(right_slider.go_up, "Up")
my_screen.onkey(right_slider.go_down, "Down")
my_screen.onkey(left_slider.go_up, "w")
my_screen.onkey(left_slider.go_down, "s")

def play():
    my_scoreboard.write_score()
    game_on = True
    my_ball.move_speed = 0.1
    while game_on:
        my_screen.update()
        my_ball.move()
        time.sleep(my_ball.move_speed)

        if my_ball.xcor() > 380:
            game_on = False
            my_ball.ball_reset()
            my_scoreboard.l_score += 1
            play()

        if my_ball.xcor() < -380:
            game_on = False
            my_ball.ball_reset()
            my_scoreboard.r_score += 1
            play()

        if my_ball.ycor() > 280 or my_ball.ycor() < -280:
            my_ball.new_y *= -1

        if my_ball.xcor() > 320 and right_slider.distance(my_ball) < 50:
            my_ball.new_x *= -1
            if my_ball.move_speed > 0.03:
                my_ball.move_speed -= 0.02

        if my_ball.xcor() < -320 and left_slider.distance(my_ball) < 50:
            my_ball.new_x *= -1
            if my_ball.move_speed > 0.03:
                my_ball.move_speed -= 0.02

play()
my_screen.exitonclick()