#task_G
x_1 = int(input())
x_2 = int(input())
m = 1
t = 1
while True:
	if x_1 == x_2:
		t += 1
	elif x_1 != x_2:
		if t > m:
			m = t
		t = 1
	if x_2 == 0:
		break
	(x_1, x_2) = (x_2, int(input()))
print(m)