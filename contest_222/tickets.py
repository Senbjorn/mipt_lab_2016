import random

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
# abc = [list(map(int, input().split())) for i in range(n)]
# n = 3000
abc = [[random.randint(1, 21), random.randint(1, 21), random.randint(1, 21)] for i in range(n)]
print("n = ", n)
# for i in range(n):
# 	print(*abc[i])
# brut_s
# m = sum([abc[i][0] for i in range(n)])
# brut_force(n, [])
# print("brut_ans = ", m)
# brut_e
A = [[0 for i in range(4)] for i in range(n)]
#begining
A[0][0] = abc[0][0]
#filling
for i in range(1, n):
	for j in range(4):
		if j <= i:
			if j == 0:
				A[i][j] = abc[i][0] + min([A[i - 1][k] for k in range(4) if A[i - 1][k] != 0])
			if j == 1:
				A[i][j] = min(abc[i][0] + A[i - 1][0], A[i - 1][0] - abc[i - 1][0] + abc[i - 1][1])
			if j == 2:
				A[i][j] = min(abc[i][0] + A[i - 1][1], A[i - 2][0] - abc[i - 2][0] + abc[i - 2][2])
			if j == 3:
				A[i][j] = min([A[i - 1][k] + abc[i][0] for k in range(2, 4) if A[i - 1][k] != 0])
#getting answer
# for i in range(n):
# 	print(*A[i])
print("ans = ", min([A[n - 1][k] for k in range(4) if A[i - 1][k] != 0]))