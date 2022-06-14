import turtle as t
pos = [(0, 0), (-20, 0), (-40, 0)]
class Snake:


    def __init__(self):

        self.segments=[]
        self.create()

    def create(self):
        for i in pos:
            self.add_newseg(i)
    def add_newseg(self,pos):
        new_turt = t.Turtle('square')
        new_turt.color('white')
        new_turt.penup()
        new_turt.goto(pos)
        self.segments.append(new_turt)
    def extend(self):
        self.add_newseg((self.segments[-1].xcor(),self.segments[-1].ycor()))
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[i - 1].xcor()
            new_ycor = self.segments[i - 1].ycor()
            self.segments[i].goto(new_xcor, new_ycor)
        self.segments[0].fd(20)
    def right(self):
        if self.segments[0].heading() !=180:
            self.segments[0].setheading(0)
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)