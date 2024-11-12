import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard



screen = Screen()
screen.setup(height= 600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)




r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()

score = Scoreboard()

screen.onkeypress(r_paddle.move_up,"Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 325 and ball.distance(r_paddle) < 60 or ball.xcor() < -325 and ball.distance(l_paddle) < 60:
        ball.bounce_x()
    if ball.xcor() > 390:
        ball.x_move *= -1
        ball.y_move = -5
        ball.home()
        ball.move_speed = 0.1
        score.left_score += 1
    if ball.xcor() < -390:
        ball.x_move *= -1
        ball.y_move = 5
        ball.home()
        ball.move_speed = 0.05
        score.right_score += 1
    score.show_score()




screen.exitonclick()