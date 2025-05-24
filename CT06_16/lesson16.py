print("Hello from lesson 16")

# import turtle

# def drawShape(length, num_sides):
#     for i in range(num_sides):
#         t.forward(length)
#         t.left(360/ num_sides)

# drawShape(100, 4)

import turtle

def setup_screen(screenWidth, screenHeight):
    screen = turtle.Screen()
    screen.setup(width = screenWidth, height = screenHeight)
    return screen

def create_blue_ball():
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("blue")
    ball.penup()
    return ball

def move_ball(ball, dx, dy):
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

dx = 10
dy = 10

screenWidth = 300
screenHeight = 500
screen = setup_screen(screenWidth, screenHeight)
 
ball = create_blue_ball()

while True:
    move_ball(ball, dx, dy)

screen.mainloop()