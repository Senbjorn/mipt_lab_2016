from random import randint
n = 10
#просто кол-во путей
A = [0] * (n + 1)
A[1] = 1
for i in range(2, n):
	A[i] = A[i - 1] + A[i - 2]
print(A[n])
#стоимость кратчайшего пути
price = [randint(5, 15) for i in range(n + 1)]
B = [0] * (n + 1)
B[1] = price[1]
B[0] = 16
Way = []
for i in range(2, n + 1):
	B[i] = price[i] + min(B[i - 1], B[i - 2])
print(*B)
path = [n]
pos = n
while path[-1] != 1:
	if B[pos - 1] > B[pos - 2]:
		path.append(pos - 2)
	else:
		path.append(pos - 1)
print(*path)
