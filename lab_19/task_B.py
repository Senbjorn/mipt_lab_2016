#task_B
def bfs(start, graph):
	n = len(graph)
	D = [None] * n
	D[start] = 0
	Q = [start]
	qindex = 0
	while qindex < len(Q):
		u = Q[qindex]
		qindex += 1
		for v in graph[u]:
			if D[v] is None:
				print(u, v)
				D[v] = D[u] + 1
				Q.append(v)
	return D
n, m = tuple(map(int, input().split()))
graph = [[] for i in range(n)]
edges = []
for i in range(m):
	a, b = tuple(map(int, input().split()))
	edges.append((a, b))
	graph[a].append(b)
	graph[b].append(a)
D = bfs(0, graph)