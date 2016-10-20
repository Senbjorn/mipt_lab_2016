#task_5
import codecs
file = codecs.open('input5.txt', 'r', 'utf-8')
L = file.readlines()
D = {}
for i in range(len(L)):
	A = L[i].split()
	for j in range(2, len(A)):
		if not A[j] in D:
			D[A[j]] = [A[0]]
		elif not A[0] in D[A[j]]:
			D[A[j]].append(A[0])
n = int(input())
for i in range(n):
	print(*D[input()])

