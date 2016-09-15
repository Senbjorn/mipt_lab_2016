import turtle
import time
def star(n, a):
	if n % 2 == 0:
		print('invalid input')
		return
	df = 360 / n * (n // 2 + 1)
	for i in range(n):
		turtle.forward(a)
		turtle.left(df)
	return
turtle.speed(10000)
star(5, 150)
time.sleep(2)

