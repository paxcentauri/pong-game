from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("DarkBlue")
screen.tracer(0)
# right_paddle = Turtle("square")
# right_paddle.color("chartreuse")
# right_paddle.penup()
# right_paddle.shapesize(stretch_len=1, stretch_wid=5)
# right_paddle.goto(350, 0)
right = Paddle(350)
left = Paddle(-350)
scoreboard = Scoreboard()
ball = Ball()
screen.listen()
# screen.update() this does not allow me to move the paddle up and down
screen.onkey(key="Up", fun=right.move_up)
screen.onkey(key="Down", fun=right.move_down)
screen.onkey(key="w", fun=left.move_up)
screen.onkey(key="s", fun=left.move_down)
game_is_on = True
while game_is_on is True:
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # Detect collision with right paddle
    if (ball.xcor() > 320 and ball.distance(right) <= 50) or (ball.xcor() < -320 and ball.distance(left) <= 50):
        ball.bounce_paddle()
        ball.move_speed = 0.9*ball.move_speed
    else:
        if ball.xcor() > 380 and ball.distance(right) > 50:
            scoreboard.lpoint()
            scoreboard.clear()
            scoreboard.score()
            ball.home()
            time.sleep(3)
            ball.x_move = -10
            ball.y_move = -10
            ball.move_speed = 0.1
        elif ball.xcor() < -380 and ball.distance(left) > 50:
            scoreboard.rpoint()
            scoreboard.clear()
            scoreboard.score()
            ball.home()
            time.sleep(3)
            ball.x_move = 10
            ball.y_move = 10
            ball.move_speed = 0.1
    screen.update()  # this however allows me to move the paddle up and down.
screen.exitonclick()
