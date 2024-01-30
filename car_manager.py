from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []      # Making list to add all the random cars.
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        a = random.randint(1, 6)
        if a == 1:      # Applying condition to slow down to process of generating random cars.
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))    # Assigning the random color to the random cars.
            car.shapesize(1, 2)     # size of car in ratios (height* width)
            random_y = random.randint(-260, 260)    # To generate random cars we only need to generate random position of y-axis.
            car.goto(300, random_y)
            self.all_cars.append(car)       # adding these random cars in all_cars list.

    def car_move(self):     # Used to making car move in backward direction, because the starting position of cars is from + y-axis.
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):     # When player reached the destination successfully, then increase the moving distance of cars.
        self.car_speed += MOVE_INCREMENT
