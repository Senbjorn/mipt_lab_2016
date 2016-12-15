#task_6
import turtle
	
def dragon(k, n, f):
	if n == 0:
		turtle.forward(k)
		return
	dragon(k / 2 ** 0.5, n - 1, True)
	if f:
		turtle.right(90)
	else:
		turtle.left(90)
	dragon(k / 2 ** 0.5, n - 1, False)

def dragon1(k, n, f):
	if n == 0:
		turtle.forward(k)
		return
	dragon1(k / 2, n - 1, True)
	if f:
		turtle.right(90 if n % 2 == 0 else -90)
	else:
		turtle.left(90 if n % 2 == 0 else -90)
	dragon1(k / 2, n - 1, False)

turtle.screensize(2000, 2000)
turtle.shape('turtle')
# turtle.tracer(100000,0)
# turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
dragon1(400, 10, False)
# turtle.update()
print("end")
input()
