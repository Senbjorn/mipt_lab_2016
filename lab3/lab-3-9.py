import turtle
import math

def polydraw(n, a):
	df = 180 - 180 * (n - 2) / n
	for i in range(n):
		turtle.forward(a)
		turtle.left(df)
	return 0


turtle.shape('turtle')
a = 100
r = a / math.sin(180 / 3) / 2
n = 10
turtle.speed(2)
for i in range(n):
	m = i + 3
	turtle.left(90 - 180 * (m - 2) / m / 2)
	polydraw(m, a)
	turtle.right(180 - 180 * (m - 2) / m / 2)
	dr = a / math.sin(math.pi / (m + 1)) / 2 - a / math.sin(math.pi / m) / 2
	turtle.penup()
	turtle.forward(dr)
	turtle.pendown()
	turtle.left(90)