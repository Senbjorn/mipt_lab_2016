import turtle

turtle.shape('turtle')
n = 10
x = 0
y = 0
for i in range(n):
	turtle.forward(6 * (i + 2))
	turtle.left(90)
	turtle.forward(6 * (i + 2))
	turtle.left(90)
	turtle.forward(6 * (i + 2))
	turtle.left(90)
	turtle.forward(6 * (i + 2))
	x -= 3
	y -= 3
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.left(90)