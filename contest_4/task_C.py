#task_C
x_1 = int(input())
x_2 = int(input())
k = 0
while x_2 != 0:
	if (x_1 < x_2):
		k += 1
	(x_2, x_1) = (int(input()), x_2)
print(k)