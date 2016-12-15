from random import randint

def choise_sort(A):
	for i in range(0, len(A)):
		for j in range(i + 1, len(A)):
			if A[i] > A[j]:
				A[i], A[j] = A[j], A[i]

A = [randint(0, 10) for i in range(10)]
print(*A)
choise_sort(A)
print(*A)