from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

snake_name = Snake()
snake_name.create_snake()

food = Food()
scoreboard = Scoreboard()



screen.listen()

screen.onkey(snake_name.up, "Up")
screen.onkey(snake_name.down, "Down")
screen.onkey(snake_name.left, "Left")
screen.onkey(snake_name.right, "Right")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake_name.move()

    if snake_name.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()


screen.exitonclick()
































