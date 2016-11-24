#task_2
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
cock(500,5)
