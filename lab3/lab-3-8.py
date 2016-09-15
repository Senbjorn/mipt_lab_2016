import turtle
import math

turtle.shape('turtle')
m = 20
p = 5
n = 1000
turtle.speed(100)
for i in range(n):
	turtle.forward(m)
	turtle.left(90)
	turtle.forward(m)
	turtle.left(90)
	turtle.forward(m + p)
	turtle.left(90)
	turtle.forward(m + p)
	m += 2 * p
	turtle.left(90)