from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):  # Used to initialize the scoreboard on screen.
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()    # showing the updated scoreboard.

    def update_scoreboard(self):
        self.clear()    # making screen clear after every update to avoiding overwrite.
        self.write(f"Level = {self.level}", align="left", font=FONT)

    def increase_level(self):   # increment in score by 1.
        self.level += 1
        self.update_scoreboard()

    def game_over(self):    # Showing these text when player collide with any car.
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER!", align="center", font=FONT)
