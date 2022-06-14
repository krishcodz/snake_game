import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.speed('fastest')
        self.color('blue')
        self.score = 0
        self.shapesize(0.5,0.5)
        self.refresh()
    def refresh(self):
        ran_corx=random.randint(-280,280)
        ran_cory=random.randint(-280,280)
        self.goto(ran_corx,ran_cory)