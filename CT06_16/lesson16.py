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
    ball.color('blue')

screenWidth = 300
screenHeight = 500
screen = setup_screen(screenWidth, screenHeight)
 
screen.mainloop()