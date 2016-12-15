#task_7
def isSymmetric(A):
	for i in range(len(A)):
		assert(len(A) == len(A[i]))
		for j in range(i):
			if A[i][j] != A[j][i]:
				return False
	return True

n = int(input())
A = [input().split() for i in range(n)]
print('YES' if isSymmetric(A) else 'NO')