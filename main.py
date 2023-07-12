from turtle import Turtle, Screen



screen= Screen()
screen.setup(width=600, height=600)
snake = Turtle()
snake.shape("square")
  # snake.shapesize(stretch_wid=1, stretch_len=3)
snake.penup()
move=0
snake_length=3
snakes=[]

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
    
    

      
def add_segment(snake_length,snakes):
  for i in range(snake_length):
    next_snake=snake.clone()
    current_position=snake.pos()
    next_snake.goto(current_position)
    snakes.append(next_snake)

def update_segments(snakes):
  for segment in snakes:
    segment.goto(snake.pos())

def update_positions(snakes):
  main_position=snake.pos()
  
  
add_segment(snake_length)
    
screen.listen()

screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")


screen.exitonclick()

