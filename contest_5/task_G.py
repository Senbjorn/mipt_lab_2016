#task_G
def check(A):
	for i in range(8):
		for j in range(i + 1, 8):
			if abs(A[i][0] - A[j][0]) == abs(A[i][1] - A[j][1]):
				return False
			if A[i][0] == A[j][0] or A[i][1] == A[j][1]:
				return False
	return True

A = list()
for i in range(8):
	A.append(list(map(int, input().split())))
if check(A):
	print('NO')
else:
	print('YES')