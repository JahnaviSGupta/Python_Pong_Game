from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.goto(0,0)
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_the_wall(self):
        self.y_move *= -1

    def bounce_the_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.move()
        self.bounce_the_paddle()

