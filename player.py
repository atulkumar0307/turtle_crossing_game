from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):     # Used to initialize the body of player as turtle shape.
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()      # calling function to make the player on starting position.

    def go_up(self):        # Used to move the player with UP key.
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_to_start(self):      # Used to make the player on starting position.
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):        # Detect if player reached the final position or not.
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
