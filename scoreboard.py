from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        # Initialize the Scoreboard
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0  # Left player's score
        self.r_score = 0  # Right player's score
        self.update_scoreboard()

    def update_scoreboard(self):
        # Update and display the scores on the screen
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        # Increase the left player's score and update the scoreboard
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        # Increase the right player's score and update the scoreboard
        self.r_score += 1
        self.update_scoreboard()
