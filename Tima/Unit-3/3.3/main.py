import turtle

x = turtle.Turtle()
x.shape('classic')
x.penup()
x.goto(-200, 200)

input1 = input('How many world cups has Brazil won? ')
if str(input1) == '5':
    x.write('Correct! Brazil has won 5 world cups!')
else:
    x.write("Incorrect! Your answer was " + input1 + ", but Brazil has won 5 world cups!")
    
x.goto(-50, 0)
x.color('red')
input2 = input('How many world cups has Argentina won? ')

if str(input2) == '3':
    x.write('Correct! Argentina has won 3 world cups!')
else:
    x.write("Incorrect! Your answer was " + input2 + ", but Argentina has won 3 world cups!")
    
x.goto(-200, -200)
x.color('blue')
input3 = input('How many world cups has Germany won? ')

if str(input3) == '4':
    x.write('Correct! Germany has won 4 world cups!')
else:
    x.write("Incorrect! Your answer was " + input3 + ", but Germany has won 4 world cups!")
    
turtle.done()
