import turtle
import math

def cdraw(r):
	n = 100
	a = math.sin(math.pi / n) * 2 * r
	df = 360 / n
	for i in range(n):
		turtle.forward(a)
		turtle.left(df)
	return 0


turtle.shape('turtle')
n = 10
turtle.speed(1000)
df = 360 / n
for i in range(n):
	cdraw(50)
	turtle.right(df) 
