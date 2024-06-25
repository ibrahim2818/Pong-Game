from turtle import Screen, Turtle
from ball import Ball
import time
from scoreboard import Scoreboard
from paddle import Paddle

sleeep_time= 0.1

screen= Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball= Ball()
scoreboard= Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(sleeep_time)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(r_paddle)<50 and ball.xcor()>320:
        ball.bounce_x()
        if sleeep_time>0.01:
            sleeep_time= sleeep_time *0.9

    if ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
        if sleeep_time>0.01:
            sleeep_time= sleeep_time*0.9
    
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
        sleeep_time= 0.1

    if ball.xcor()< -380:
        ball.reset_position()
        scoreboard.r_point()
        sleeep_time= 0.1
    




screen.exitonclick()
