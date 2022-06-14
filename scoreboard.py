from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-50,270)
        self.color('white')
        self.score=0
    def out(self):
        self.clear()
        self.write(f"SCORE : {self.score}",font=("Times New Roman", 16, "normal"))
    def gameover(self):
        self.penup()
        self.goto(-100,20)
        self.write(f"GAME OVER",font=("Arialblack", 20, "normal"))
        self.goto(-130,-20)
        self.write(f"YOUR SCORE IS :{self.score}",font=("Times New Roman", 20, "normal"))
        self.penup()
        self.goto(170,-270)
        self.color('red')

        self.write("GAME BY KRISHNA",font=("Times New Roman", 10, "normal"))
