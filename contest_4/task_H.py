#task_H
x_1 = int(input())
x_2 = int(input())
m = 1
t0 = 1
t1 = 1
b = False
while True:
	if x_1 < x_2 and x_2 != 0:
		t0 += 1
	else:
		if t0 > m:
			m = t0
		t0 = 1
	if x_1 > x_2 and x_2 != 0:
		t1 += 1
	else:
		if t1 > m:
			m = t1
		t1 = 1
	if x_2 == 0:
		break
	(x_1, x_2) = (x_2, int(input()))
print(m)