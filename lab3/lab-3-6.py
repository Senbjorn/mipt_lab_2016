import turtle

turtle.shape('turtle')
n = 8
r = 100
df = 180 - 180 * (n - 2) / n
for i in range(n):
	turtle.forward(r)
	turtle.stamp()
	turtle.left(180)
	turtle.forward(r)
	turtle.left(180 + df)