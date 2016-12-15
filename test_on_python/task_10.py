#task_10
import random as r

def random_point():
	return [r.randint(-20, 20) for i in range(6)]

def solve(a, b, c):
	if a != 0:
		d = b ** 2 - 4 * a * c
		if d >= 0:
			return [(-b - d ** 0.5) / 2 / a, (-b + d ** 0.5) / 2 / a]
		return ['none']
	elif b != 0:
		return [c / b]
	elif c != 0:
		return ['none']
	else:
		return ['inf']
def number(G):
	if len(G) == 0:
		return 0
	if G[0] == 'inf' or G[0] == 'none':
		return 0
	k = 0
	for i in G:
		if i >= 0:
			k += 1
	return k

def inter(A):
	F = []
	i = 0
	while i < len(A):
		if A[i][0] == 'inf':
			A.pop(i)
		else:
			i += 1
	for w in A[0]:
		flag = True
		for L in A:
			if not w in L:
				flag = False
				break
		if flag:
			F.append(w)
	return F

def number_of_lines(a1, b1, c1, a2, b2, c2, a3, b3, c3):
	G1 = solve(a1, b1, c1)
	G2 = solve(a2, b2, c2)
	G3 = solve(a3, b3, c3)
	if G1[0] == 'inf' and G2[0] == 'inf' and G3[0] == 'inf':
		return -1
	elif G1[0] == 'inf' or G2[0] == 'inf' or G3[0] == 'inf':
		# print(inter([G1, G2, G3]))
		return number(inter([G1, G2, G3]))
	elif G2[0] != 'none' and G1[0] != 'none' and G3[0] != 'none':
		# print(inter([G1, G2, G3]))
		return number(inter([G1, G2, G3]))
	else:
		return 0
def main(A):
	B1R = [A[1][i] - A[0][i] for i in range(3)]
	B1V = [A[1][i] - A[0][i] for i in range(3, 6)]
	B2R = [A[2][i] - A[0][i] for i in range(3)]
	B2V = [A[2][i] - A[0][i] for i in range(3, 6)]
	# print(B1R, B2R)
	# print(B1V, B2V)
	a1 = B1V[1] * B2V[2] - B2V[1] * B1V[2]
	b1 = B1V[1] * B2R[2] + B2V[2] * B1R[1] - B1V[2] * B2R[1] - B2V[1] * B1R[2]
	c1 = B1R[1] * B2R[2] - B1R[2] * B2R[1]
	a2 = B1V[1] * B2V[0] - B2V[1] * B1V[0]
	b2 = B1V[1] * B2R[0] + B2V[0] * B1R[1] - B1V[0] * B2R[1] - B2V[1] * B1R[0]
	c2 = B1R[1] * B2R[0] - B1R[0] * B2R[1]
	a3 = B1V[0] * B2V[2] - B2V[0] * B1V[2]
	b3 = B2V[2] * B1R[0] + B1V[0] * B2R[2] - B1V[2] * B2R[0] - B2V[0] * B1R[2]
	c3 = B1R[0] * B2R[2] - B1R[2] * B2R[0]
	R1 = [a1, b1, c1]
	R2 = [a2, b2, c2]
	R3 = [a3, b3, c3]
	return number_of_lines(*R1, *R2, *R3)	

# A = [list(map(int, input().split())) for i in range(3)]
# [-16, -15, 17, 8, -11, 3] [-16, -15, 17, -14, -12, 10] [-15, -15, 20, 0, 11, -1] 1
# [-3, -1, -7, -18, 19, 4] [-18, 18, -8, 6, 15, 10] [6, 14, -2, -18, 13, 3] 2
# [11, 15, 0, 20, -10, 1] [-3, 15, 0, -5, -10, 0] [-10, 15, 0, -4, -19, -15] 2
# print('')
# print(R1, R2, R3, solve(*R1), solve(*R2), solve(*R3))
out = open('result.txt', 'w')
A = [random_point() for i in range(3)]
n = main(A)
while n != -1:
	A = [random_point() for i in range(3)]
	n = main(A)
print(*A, n, file = out)
out.close()