from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        # Initialize the Paddle
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        # Move the paddle up
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        # Move the paddle down
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
