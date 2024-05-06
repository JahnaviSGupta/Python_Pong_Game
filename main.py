import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


game_is_on= False

'''Screen'''
screen = Screen()
screen.bgcolor("Black")
screen.setup(height=600 , width= 800)
screen.tracer(0)
'''Create Paddle'''
left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))

'''Create the ball'''
ball = Ball()

'''Create the scoreboard'''
scoreboard = Scoreboard()

'''Move the Paddles'''
screen.listen()
'''left paddle'''
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
'''right paddle'''
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")


game_is_on= True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()


    '''ball touches the walls'''
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce_the_wall()

    '''ball touches the right paddle'''
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_the_paddle()

    '''ball touches the left paddle'''
    if ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_the_paddle()

    '''ball misses the right paddle'''
    if ball.xcor() > 380 and ball.distance(right_paddle) > 50:
        ball.ball_reset()
        scoreboard.increase_left_score()

    '''ball misses the left paddle'''
    if ball.xcor() < -380 and ball.distance(left_paddle) > 50:
        ball.ball_reset()
        scoreboard.increase_right_score()





screen.exitonclick()