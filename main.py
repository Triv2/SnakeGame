from turtle import Turtle, Screen



screen= Screen()
screen.setup(width=600, height=600)
snake = Turtle()
snake.shape("square")
  # snake.shapesize(stretch_wid=1, stretch_len=3)
snake.penup()
move=0
snake_length=10

def go_up():
    snake.setheading(90)
    snake.forward(20)
    create_tail(move,snake_length)
    

def go_down():
    snake.setheading(270)
    snake.forward(20)
    create_tail(move,snake_length)
   

def go_left():
    snake.setheading(180)
    snake.forward(20)
    create_tail(move,snake_length)
    

def go_right():
    snake.setheading(0)
    snake.forward(20)
    create_tail(move,snake_length)
      
def create_tail(move,snake_length):
  move+=1
  if move>=snake_length:
    snake.clear()
  else:
    snake.stamp()
    
screen.listen()

screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

screen.exitonclick()

