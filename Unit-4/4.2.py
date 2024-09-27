import turtle

tima = turtle.Turtle()
tima.color('red', 'blue')
tima.shape('turtle')

ryan = turtle.Turtle()
ryan.color('red', 'blue')
ryan.shape('classic')

maaz = turtle.Turtle()
maaz.color('red', 'blue')
maaz.shape('arrow')

tima.penup()
ryan.penup()
maaz.penup()

def moveTurtle(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

moveTurtle(tima, 0, 125)
tima.write("Let's draw!")

colors = ['red', 'blue', 'green', 'yellow']

def draw_square():
    tima.begin_fill()
    tima.pensize(4) 
    
    for i in range(4):
        tima.color(colors[i])
        tima.forward(50)
        tima.right(90)
    tima.end_fill()
    tima.penup()

moveTurtle(maaz, 0, 0)

def draw_triangle():
    maaz.pensize(10)
    maaz.color((.5, 0, .5))
    maaz.begin_fill()
    for i in range(3):
        maaz.forward(50)
        maaz.right(120)
    maaz.end_fill()
    maaz.penup()
    
moveTurtle(ryan, 0, -100)
    
def draw_circle():
    ryan.begin_fill()
    x = 2
    ryan.pensize(x)
    for i in range(5):
        ryan.forward(50)
        ryan.right(72)
        x += 1
        ryan.pensize(x)
    ryan.end_fill()
    ryan.pensize(1)
    ryan.penup()
    ryan.goto(-150, 100)
    ryan.pendown()
    ryan.begin_fill()
    ryan.circle(15)
    ryan.end_fill()
    ryan.penup()
    ryan.goto(-100, -100)
    ryan.write('Look at all those shapes!')
    
draw_square()
draw_triangle()
draw_circle()

turtle.done()