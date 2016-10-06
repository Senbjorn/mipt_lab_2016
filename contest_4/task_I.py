#task_I
x_1 = int(input())
x_2 = int(input())
b = False
n = 0
while x_2 != 0:
	if b and x_2 < x_1:
		b = False
		n += 1
	elif x_2 > x_1:
		b = True
	elif x_1 == x_2:
		b = False
	(x_1, x_2) = (x_2, int(input()))
print(n)