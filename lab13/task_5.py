#task_5
import turtle

def levi(k, n):
	if n == 0:
		turtle.forward(k)
		return
	turtle.left(45)
	levi(k / 2 ** 0.5, n - 1)
	turtle.right(90)
	levi(k / 2 ** 0.5, n - 1)
	turtle.left(45)


turtle.speed(1000)
turtle.penup()
turtle.goto(-150, -100)
turtle.pendown()
levi(300, 10)
input()