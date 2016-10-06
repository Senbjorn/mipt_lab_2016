#task_C
A = input().split()
B = A[0].split(':')
if (A[1] == 'a.m.'):
	B[0] = str(int(B[0]) % 12)
	if len(B[0]) == 1:
		B[0] = '0' + B[0]
else:
	B[0] = str(int(B[0]) % 12 + 12)
print(':'.join(B))