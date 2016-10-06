#task_H
def flip(S, A, B):
	if A == 0:
		S[A: B + 1] = S[B:: -1]
	else:
		S[A: B + 1] = S[B: A - 1: -1]


L = list(map(int, input().split()))
S = [i for i in range(1, L[0] + 1)]
flip(S, L[1] - 1, L[2] - 1)
flip(S, L[3] - 1, L[4] - 1)
print(*S)