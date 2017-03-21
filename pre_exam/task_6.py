#task_6
def dijkstra(start, graph):
	n = len(graph)
	D = {v: float('+inf') for v in range(n)}
	D[start] = 0
	used = set()
	while True:
		min_d = float('+inf')
		min_v = None
		for v in D:
			if v not in used and min_d > D[v]:
				min_d = D[v]
				min_v = v
		if min_v is None:
			break # заканчиваем когда все вершины нашли == все v либо в used либо D[v] == +inf
		for neighbour in graph[min_v]:
			if D[neighbour] > D[min_v] + graph[min_v][neighbour]:
				D[neighbour] = D[min_v] + graph[min_v][neighbour]
		used.add(min_v)
	return D

def reverse(graph):
	n = len(graph)
	graph_reversed = {i: {} for i in range(n)}
	for v in range(n):
		for u in graph[v]:
			graph_reversed[u][v] = graph[v][u]
	return graph_reversed


def get_path(start, finish, D, graph):
	graph_reversed = reverse(graph)
	P = [finish]
	x = finish
	while x != start:
		min_u = None
		min_v = float('+inf')
		for u in graph_reversed[x]:
			if D[u] + graph_reversed[x][u] < min_v:
				min_v = D[u] + graph_reversed[x][u]
				min_u = u
		P.append(min_u)
		x = min_u
	return P[-1::-1]

n, m, s, f = tuple(map(int, input().split()))
graph = {x: {} for x, y in zip(range(n), range(n))}
for i in range(m):
	a, b, w = tuple(map(int, input().split()))
	graph[a][b] = w
	graph[b][a] = w
D = dijkstra(s, graph)
