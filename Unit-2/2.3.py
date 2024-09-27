# README README README README README README README
# click on the 3 bars at the top left and go to fullscreen
import turtle

tima = turtle.Turtle()
tima.color('red', 'blue')
tima.shape('classic')

tima.penup() # we will discuss this command next week
tima.goto(0,125)
tima.write("Let's draw!")
# we will discuss this command next week

tima.pendown()
# write code to make a square below these comments
# use forward, back, left, right and goto commands only

colors = ['red', 'blue', 'green', 'yellow']
tima.pensize(4)

for i in range(4):
    tima.color(colors[i])
    tima.forward(50)
    tima.right(90)
    
# go to next area on the screen
tima.penup()
tima.goto(0,0)
tima.pendown()

# write code to make a triangle below these comments
# use forward, back, left, right and goto commands only
tima.pensize(10)
tima.color((0.5, 0, 1))

for i in range(3):
    tima.forward(50)
    tima.right(120)
    
# go to next area on the screen
tima.penup()
tima.goto(0,-125)
tima.pendown()

# write code to make a pentagon below these comments
# use forward, back, left, right and goto commands only
x = 2
tima.pensize(x)

for i in range(5):
    tima.forward(50)
    tima.right(72)
    x += 1
    
tima.pensize(x)
tima.penup()
tima.goto(-100, -100)
tima.write('Look at all those shapes!')

turtle.done()