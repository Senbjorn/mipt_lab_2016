import turtle
import math

def cdraw(radius, width, fill, fcolor, pcolor, p, f):
	turtle.fillcolor(fcolor)
	turtle.pencolor(pcolor)
	turtle.width(width)
	if fill:
		turtle.begin_fill()
	n = 100
	a = math.sin(math.pi / n) * 2 * radius
	df = 360 / n
	for i in range(f):
		turtle.forward(a)
		if p:
			turtle.left(df)
		else:
			turtle.right(df)
	if fill:
		turtle.end_fill()
	turtle.fillcolor('black')
	turtle.pencolor('black')
	turtle.width(1)
	return 0
def line(length, width, color):
	turtle.width(width)
	turtle.pencolor(color)
	turtle.forward(length)
	turtle.pencolor('black')
	turtle.width(1)
def go(x, y):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()

turtle.shape('turtle')
turtle.speed(10000)
cdraw(100, 1, True, 'yellow', 'black', True, 100)
go(50, 120)
cdraw(16, 1, True, 'blue', 'black', True, 100)
go(-50, 120)
cdraw(16, 12, True, 'black', 'white', True, 100)
go(0, 125)
turtle.right(90)
line(30, 13, 'black')
go(70, 70)
turtle.right(180 * 10 / 100)
turtle.penup()
cdraw(75, 15, False, 'red', 'red', False, 5)
turtle.pendown()
cdraw(75, 15, False, 'red', 'red', False, 30)