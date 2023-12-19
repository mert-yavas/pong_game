from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the game screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # Turn off automatic screen updates

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))  # Right paddle
l_paddle = Paddle((-350, 0))  # Left paddle
ball = Ball((0, 0))  # Game ball
scoreboard = Scoreboard()  # Scoreboard

# Set up keyboard controls
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.speed_up)  # Control ball speed
    screen.update()  # Manually update the screen
    ball.move()  # Move the ball

    # Detect collision with the top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when the right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

    # Detect when the left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()

# Close the game screen on click
screen.exitonclick()
