#task_2
m1 = 0
m2 = 0
x = int(input())
while x != 0:
	if x > m1:
		m1, m2 = x, m1
	elif x > m2 and m1 != x:
		m2 = x
	x = int(input())
print(m2)