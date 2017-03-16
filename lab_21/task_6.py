#task_6.py

def FloydWarshall(graph):
	n = len(graph)
	A = [[float('+inf') for j in range(n)]for i in range(n)]
	for i in range(n):
		A[i][i] = 0
		for v in graph[i]:
			A[i][v] = graph[i][v]
	for k in range(n):
		B = [[0 for j in range(n)]for i in range(n)]
		for i in range(n):
			for j in range(n):
				B[i][j] = min(A[i][j], A[i][k] + A[k][j])
		A = B
	return A
n, m = tuple(map(int, input().split()))
graph = {i: {} for i in range(n)}
total_weight = 0
for j in range(m):
	a, b, w = tuple(map(int, input().split()))
	graph[a][b] = w
	graph[b][a] = w
	total_weight += w

dist_matrix = FloydWarshall(graph)
set_of_odd = set()
for i in range(n):
	if len(graph[i]) % 2 == 1:
		set_of_odd.add(i)
while len(set_of_odd) != 0:
	min_v = float('+inf')
	min_e = None
	list_of_odd = list(set_of_odd)
	for i in range(len(list_of_odd)):
		for j in range(i + 1, len(list_of_odd)):
			u, v = list_of_odd[i], list_of_odd[j]
			if dist_matrix[u][v] < min_v:
				min_v = dist_matrix[u][v]
				min_e = (u, v)
	total_weight += min_v
	set_of_odd.remove(min_e[0])
	set_of_odd.remove(min_e[1])
print(total_weight)
