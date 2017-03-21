#task_7
def FloydWarshall(graph):
	n = len(graph)
	A = [[float('+inf') for j in range(n)] for i in range(n)]
	for i in range(n): #k = 0 изначально пути без промежуточных вершин (просто 1 ребро)
		A[i][i] = 0
		for v in graph[i]:
			A[i][v] = graph[i][v]
	for k in range(n): # на k-том шаге строится матрица A: A[i][j]k = кратчайший путь из i в j используя первые k вершин как промежуточные
		for i in range(n):
			for j in range(n):
				A[i][j] = min(A[i][j], A[i][k] + A[k][j])
	return A

n, m = tuple(map(int, input().split()))
graph = {i: {} for i in range(n)}
for j in range(m):
	a, b, w = tuple(map(int, input().split()))
	graph[a][b] = w
	graph[b][a] = w
A = FloydWarshall(graph)