#task_E
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
				D[v] = D[u] + 1
				Q.append(v)
	return D
