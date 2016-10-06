#task_I
def mdist(A):
	m = 0
	for i in range(len(A)):
		for j in range(i + 1, len(A)):
			m1 = ((A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2)
			if m1 > m:
				m = m1
	return m

n = int(input())
A = [list(map(int, input().split())) for i in range(n)]
print(mdist(A) ** 0.5)