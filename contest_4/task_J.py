#task_J
y_1 = int(input())
y_2 = int(input())
b = False
c = True
x_1 = 0
x_2 = 0
i = 0
r = 0
while y_2 != 0:
	if b and y_2 < y_1:
		b = False
		(x_1, x_2) = (i, x_1)
		if x_1 * x_2 != 0 and c:
			r = x_1 - x_2
			c = False
		if x_1 - x_2 < r and not c:
			r = x_1 - x_2
	elif y_2 > y_1:
		b = True
	elif y_1 == y_2:
		b = False
	(y_1, y_2) = (y_2, int(input()))
	i += 1
print(r)