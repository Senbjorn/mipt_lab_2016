import turtle
import math

turtle.shape('turtle')
m = 0.01
n = 1000
turtle.speed(100)
for i in range(n):
	turtle.forward(m)
	turtle.left(1)
	m += 0.001