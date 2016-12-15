
def sort(A, N):
	n = len(A)
	for i in range(0, n - 1):
		for j in range(1, n - i):
			if A[j - 1] > A[j]:
				A[j - 1], A[j] = A[j], A[j - 1]
				N[A[j]] += 1
				N[A[j - 1]] += 1

def sort1(A):
	n = len(A)
	for i in range(0, n - 1):
		for j in range(1, n - i):
			if A[j - 1] > A[j]:
				A[j - 1], A[j] = A[j], A[j - 1]

A = list(map(int, input().split()))
N = dict()
for i in range(len(A)):
	if A[i] not in N:
		N[A[i]] = 0
sort(A, N)
A = list(N.keys())
sort1(A)
for i in range(len(A)):
	print(str(A[i]) + ":" + str(N[A[i]]), end = " ")