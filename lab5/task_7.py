#task_7
A = list(map(int, input().split()))
s = 0
n = 0
for i in range(len(A)):
	if i > 0:
		s += A[i]
		n += 1
		if A[i] != 2 and A[i - 1] == 2:
			s -= 2
			n -= 1
	else:
		n += 1
		s += A[i]
print(int(s / n))