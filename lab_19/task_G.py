#task_G
def dijkstra(start, graph):
	n = len(graph)
	D = [None] * n
	D[start] = 0
	index = 0
	Q = [start]
	while index < len(Q):
		v = Q[index]
		index += 1
		for u in graph[v]:
			if D[u] == None or D[v] + min(graph[v][u]) < D[u]:
				D[u] = D[v] + min(graph[v][u])
				Q.append(u)
	return D

def add(graph, a, b, w):
	if b in graph[a]:
		grph[a][b].append(w)
	else:
		graph[a][b] = [w]

n, m, s, f = tuple(map(int, input().split()))
graph = {x: {} for x, y in zip(range(n), range(n))}
for i in range(m):
	a, b, w = tuple(map(int, input().split()))
	add(graph, a, b, w)
	add(graph, b, a, w)
D = dijkstra(s, graph)
if D[f] == None:
	print('INF')
else:
	print(D[f])