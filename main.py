from turtle import Turtle, Screen

import time

#Global Variables

screen= Screen()
screen.setup(width=600, height=600)
starting_positions=[(0,0),(-20,0),(-40,0)]
snakes=[]

#Controls for movement.

def go_up():
  
  snake.setheading(90)
  snake.forward(20)  

def go_down():
  
  snake.setheading(270)
  snake.forward(20)

def go_left():
  
  snake.setheading(180)
  snake.forward(20)

def go_right():
  
  snake.setheading(0)
  snake.forward(20)

    
    
# Functions to control the snake.


class Snake:
  def __init__(self):
    self.segments=[]
    self.init_snake(starting_positions)
    
  def init_snake(self,starting_positions):
    for position in starting_positions:
      next_snake=Turtle()
      next_snake.penup()
      next_snake.goto(position)
      next_snake.shape("square")
      snakes.append(next_snake)
  
  def move(self,snakes):
    for seg in range(length-1,0,-1):
      new_x=snakes[seg-1].xcor()
      new_y=snakes[seg-1].ycor()
      snakes[seg].goto(new_x,new_y)
      snakes[0].forward(20)
      snakes[0].left(90)
    
snake=Snake()
  



game_is_on=True
while game_is_on:
  length=len(snakes)
  screen.update()
  time.sleep(0.1)
  snake.move(snakes)
  
    
    
screen.listen()

screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")


screen.exitonclick()

