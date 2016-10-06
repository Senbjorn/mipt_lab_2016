#task_F
z = int(input())
n = 0
m = 0
while z != 0:
	if m < z:
		m = z
		n = 1
	elif m == z:
		n += 1
	z = int(input())
print(n)