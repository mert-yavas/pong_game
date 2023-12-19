from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        # Initialize the Ball
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(position)
        self.x_move = 10  # Initial x-axis movement
        self.y_move = 10  # Initial y-axis movement
        self.speed_up = 0.1  # Initial speed

    def move(self):
        # Move the ball to a new position
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # Reverse the y-axis movement when bouncing off a wall
        self.y_move *= -1

    def bounce_x(self):
        # Reverse the x-axis movement and increase speed when bouncing off a paddle
        self.speed_up *= 0.9
        self.x_move *= -1

    def reset_position(self):
        # Reset the ball's position and speed when a player scores
        self.goto(0, 0)
        self.speed_up = 0.1
        self.bounce_x()
