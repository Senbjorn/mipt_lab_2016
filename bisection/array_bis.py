def upper_bound(A, key):
	left = -1
	right = len(A)
	while right - left > 1:
		middle = (left + right) // 2
		if A[middle] > key:
			right = middle
		else:
			left = middle
	return right

def lower_bound(A, key):
	left = -1
	right = len(A)
	while right - left > 1:
		middle = (left + right) // 2
		if A[middle] >= key:
			right = middle
		else:
			left = middle
	return right
B = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A = [2, 3, 4, 5, 5, 5, 5, 7, 7, 7, 7]
k = 2
print(upper_bound(A, k), lower_bound(A, k))