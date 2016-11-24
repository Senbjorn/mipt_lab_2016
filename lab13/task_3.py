#task_3
import turtle
def cock(k, n):
	if n == 0:
		turtle.forward(k)
		return
	x = k
	cock(k / 3, n - 1)
	turtle.left(60)
	cock(k / 3, n - 1)
	turtle.right(120)
	cock(k / 3, n - 1)
	turtle.left(60)
	cock(k / 3, n - 1)

turtle.speed(1000)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
m = 5
k = 300
cock(k, m)
turtle.right(120)
cock(k, m)
turtle.right(120)
cock(k, m)
input()
