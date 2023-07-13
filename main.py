from turtle import Turtle, Screen

#Global Variables

screen= Screen()
screen.setup(width=600, height=600)
snake = Turtle()
snake.shape("square")
snake.penup()
move=0
snake_length=3
snake_moves=[]
snakes=[]

#Controls for movement.

def go_up():
    save_moves(snake,snake_moves)
    snake.setheading(90)
    snake.forward(20)
    update_snakes(snake_moves,snakes)
    
    

def go_down():
    save_moves(snake,snake_moves)
    snake.setheading(270)
    snake.forward(20)
    update_snakes(snake_moves,snakes)
    
   

def go_left():
    save_moves(snake,snake_moves)
    snake.setheading(180)
    snake.forward(20)
    update_snakes(snake_moves,snakes)

def go_right():
    save_moves(snake,snake_moves)
    snake.setheading(0)
    snake.forward(20)
    update_snakes(snake_moves,snakes)
    
    
# Functions to control the snake.
      
def add_segment(snakes):
    next_snake=snake.clone()
    current_position=snake.pos()
    next_snake.goto(current_position)
    snakes.append(next_snake)



def update_snakes(snake_moves,snakes):
  if len(snake_moves)>snake_length:
    del snake_moves[0]
  else:
    add_segment(snakes)
  

def save_moves(snake,snake_moves):
  current_x=snake.xcor()
  current_y=snake.ycor()
  current_position=(current_x, current_y)
  snake_moves.append(current_position)


  
  

    
screen.listen()

screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")


screen.exitonclick()

