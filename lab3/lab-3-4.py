import turtle

turtle.shape('turtle')
n = 100
df = 180 - 180 * (n - 2) / n
for i in range(n):
	turtle.forward(5)
	turtle.left(df)
