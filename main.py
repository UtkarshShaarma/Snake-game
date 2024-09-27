import time
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)


    if snake.head.distance(food)< 15:
        food.ref()
        snake.extend()
        score.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.Game_over()
        game_is_on=False

    for segments in snake.segments:
        if segments ==snake.head:
            pass
        elif snake.head.distance(segments)<10:
            game_is_on = False
            score.Game_over()




    snake.move()





























screen.exitonclick()