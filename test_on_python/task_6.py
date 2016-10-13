#task_6
n = int(input())
s = 0
day = 0
a_1 = 1
a_0 = 0
while s < n:
	a_1, a_0 = a_1 + a_0, a_1
	day += 1
	s += a_0
print(day)