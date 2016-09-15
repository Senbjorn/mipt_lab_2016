import turtle
import math

def cdraw(r, p):
	n = 100
	a = math.sin(math.pi / n) * 2 * r
	df = 360 / n
	for i in range(n // 2):
		turtle.forward(a)
		if p:
			turtle.left(df)
		else:
			turtle.right(df)
	return 0


turtle.shape('turtle')
n = 10
turtle.speed(1000)
for i in range(n):
	cdraw(50, True)
	cdraw(20, True)
