import turtle
import math

turtle.shape('turtle')
dphi =  0.1
phi = 0
k = 2
radius = 0
n = 10000
turtle.speed(10000)
turtle.left(90)
for i in range(n):
	x = radius * math.cos(phi)
	y = radius * math.sin(phi)
	turtle.goto(x, y)
	phi += dphi
	turtle.left(180 / math.pi * dphi)
	radius = k * phi