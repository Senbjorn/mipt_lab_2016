#task_4
import turtle

def minkovskii(k, n):
	if n == 0:
		turtle.forward(k)
		return
	minkovskii(k / 4, n - 1)
	turtle.left(90)
	minkovskii(k / 4, n - 1)
	turtle.right(90)
	minkovskii(k / 4, n - 1)
	turtle.right(90)
	minkovskii(k / 4, n - 1)
	minkovskii(k / 4, n - 1)
	turtle.left(90)
	minkovskii(k / 4, n - 1)
	turtle.left(90)
	minkovskii(k / 4, n - 1)
	turtle.right(90)
	minkovskii(k / 4, n - 1)

turtle.speed(1000)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
minkovskii(500, 3)
input()