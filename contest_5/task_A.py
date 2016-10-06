#task_A
s = input()
x, y = 0, 0
while s != 'Treasure!':
	A = s.split()
	if A[0] == 'North':
		y += int(A[1])
	elif A[0] == 'South':
		y -= int(A[1])
	elif A[0] == 'West':
		x -= int(A[1])
	elif A[0] == 'East':
		x += int(A[1])
	s = input()
print(x, y)