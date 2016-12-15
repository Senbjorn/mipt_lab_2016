def brut_force(n, A):
	global m
	if n == 0:
		t = sum([0 if A[i] == 0 else abc[i][A[i] - 1] for i in range(len(A))])
		if m > t:
			m = t
		return
	if n >= 3:
		B = list(A)
		B.extend([3, 0 , 0])
		brut_force(n - 3, B)
	if n >= 2:
		B = list(A)
		B.extend([2, 0])
		brut_force(n - 2, B)
	if n >= 1:
		B = list(A)
		B.extend([1])
		brut_force(n - 1, B)


n = int(input())
abc = [list(map(int, input().split())) for i in range(n)]
m = sum([abc[i][0] for i in range(n)])
brut_force(n, [])
print(m)