#task_6
import turtle

def dragon(k, n):
	if n == 0:
		turtle.forward(k)
		return
	dragon(k / 2, n - 1)
	
	turtle.pendown()

turtle.speed(1000)
turtle.penup()
turtle.goto(-150, -100)
turtle.pendown()
dragon(300, 2)
input()
