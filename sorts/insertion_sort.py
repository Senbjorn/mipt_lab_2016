from random import randint

def insertion_sort(A):
	for i in range(1, len(A)):
		val = A[i]
		j = i - 1
		while j >= 0 and A[j] > val:
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = val

A = [randint(0, 500) for i in range(10)]
print(*A)
insertion_sort(A)
print(*A)