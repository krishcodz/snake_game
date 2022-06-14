import turtle as t
import time
import snake
import food
from scoreboard import Score
screen=t.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
my_snake=snake.Snake()
food=food.Food()
score=Score()
screen.listen()
screen.onkey(my_snake.up,"Up")
screen.onkey(my_snake.down,"Down")
screen.onkey(my_snake.right,"Right")
screen.onkey(my_snake.left,"Left")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()
    score.out()
    if my_snake.segments[0].distance(food) < 15:
        food.refresh()
        score.score += 1
        my_snake.extend()
    if my_snake.segments[0].xcor() > 290 or my_snake.segments[0].xcor() < -290 or my_snake.segments[0].ycor() > 290 or my_snake.segments[0].ycor() < -290 :
        score.gameover()
        game_is_on=False
    for i in my_snake.segments[1::]:
        if my_snake.segments[0].distance(i) < 10 :
            score.gameover()
            game_is_on = False
screen.exitonclick()