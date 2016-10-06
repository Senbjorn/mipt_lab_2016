#task_6
n = int(input())
A = list(map(int, input().split()))
for i in range(len(A)):
	s = 0
	for j in range(len(A)):
		if A[j] < A[i]:
			s += 1
	if s == n // 2:
		print(A[i])
		break
