from random import choice, randint

def hoar_sort(A):
	if len(A) <= 1:
		return A
	border = choice(A)
	L = []
	R = []
	M = []
	for x in A:
		if x > border:
			R.append(x)
		elif x < border:
			L.append(x)
		else:
			M.append(x)
	return hoar_sort(L) + M + hoar_sort(R)

A = [randint(0, 500) for i in range(10)]
print(*A)
B = hoar_sort(A)
print(*B)