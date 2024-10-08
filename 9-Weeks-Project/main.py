import turtle
import math
import random

screen = turtle.Screen()
screen.reset()
screen.setworldcoordinates(-100,-100,100,100) 

tina = turtle.Turtle()
tina.penup()

# ------------------------------------------------------DAY 1
# START-----------------------------------------------------

def draw_square(xPos, yPos, turt, n):
    turt.goto(xPos, yPos)
    turt.pendown()
    turt.begin_fill()
    for i in range(4):
        turt.forward(n)
        turt.right(90)
    turt.end_fill()
    turt.penup()
    return n*n

def draw_circle(xPos, yPos, turt, r):
    turt.goto(xPos, yPos)
    turt.pendown()
    turt.begin_fill()
    turt.circle(r)
    turt.end_fill()
    turt.penup()
    return math.pi * r * r

def draw_reg_pentagon(xPos, yPos, turt, n):
    turtle.goto(xPos, yPos)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(n)
        turtle.right(72)
    turtle.end_fill()
    turtle.penup()
    return 1/4 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * n * n

def draw_triangle(xPos, yPos, turt, n):
    turt.goto(xPos, yPos)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(n)
        turtle.right(120)
    turtle.end_fill()
    turtle.penup()  
    return 1/4 * math.sqrt(3) * n * n 


def draw_reg_hexagon(xPos, yPos, turt, n):
    turt.goto(xPos, yPos)
    turt.pendown()
    turt.begin_fill()
    for i in range(6):
        turt.forward(n)
        turt.right(60)
    turt.end_fill()
    turt.penup()
    return 3/2 * math.sqrt(3) * n * n
    
def draw_reg_decagon(xPos, yPos, turt, n):
    turt.goto(xPos, yPos)
    turt.pendown()
    turt.begin_fill()
    for i in range(10):
        turt.forward(n)
        turt.right(36)
    turt.end_fill()
    turt.penup()
    return 1/4 * math.sqrt(10 + 2 * math.sqrt(5)) * n * n

# -------------------------------------------------------DAY 1
#END------------------------------------------------------

# ------------------------------------------------------DAY 2
#START-----------------------------------------------------

def draw_shape(shape, xPos, yPos, size):
    """
    match shape: # this would've been so much better :/
        case 'square':
            draw_square(xPos, yPos, tina, size)
        case 'circle':
            draw_circle(xPos, yPos, tina, size)
        case 'triangle':
            draw_triangle(xPos, yPos, tina, size)
        case 'pentagon':
            draw_reg_pentagon(xPos, yPos, tina, size)
        case 'hexagon':
            draw_reg_hexagon(xPos, yPos, tina, size)
        case 'decagon':
            draw_reg_decagon(xPos, yPos, tina, size) 
        default:
            tina.write("Invalid shape")    
            """
    tina.color(random.random(), random.random(), random.random())
    
    shapes_area = 0
    
    if shape == 'square':
        draw_square(xPos, yPos, tina, size)
        shapes_area = size * size
    elif shape == 'circle':
        draw_circle(xPos, yPos, tina, size)
        shapes_area = math.pi * size * size
    elif shape == 'triangle':
        draw_triangle(xPos, yPos, tina, size)
        shapes_area = 1/4 * math.sqrt(3) * size * size
    elif shape == 'pentagon':
        draw_reg_pentagon(xPos, yPos, tina, size)
        shapes_area = 1/4 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * size * size
    elif shape == 'hexagon':
        draw_reg_hexagon(xPos, yPos, tina, size)
        shapes_area = 3/2 * math.sqrt(3) * size * size
    elif shape == 'decagon':
        draw_reg_decagon(xPos, yPos, tina, size)
        shapes_area = 1/4 * math.sqrt(10 + 2 * math.sqrt(5)) * size * size
    else: 
        tina.write("Invalid shape")
    return shapes_area

ushape = turtle.textinput("Shape Input", "What shape would you like to input?")
ux = turtle.numinput("X position", "What x value do you want tina to go to?", 0, -400, 400)
uy = turtle.numinput("Y position", "What y value do you want tina to go to?", 0, -400, 400)

prompt = "What size do you want your " + str(ushape) + " to be?"
usize = turtle.numinput("Size", prompt, 0, 0, 100)

draw_shape(ushape, ux, uy, usize)

tina.goto(-60, -80)
tina.write("The area of the shape is: " + str(draw_shape(ushape, ux, uy, usize)))

turtle.done()