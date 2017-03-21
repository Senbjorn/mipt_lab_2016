#task_3
def bfs(start, graph, D):
	D[start] = 0
	Q = [start]
	index = 0
	while index < len(Q):
		vertex = Q[index]
		index += 1
		for v in graph[vertex]:
			if D[v] > D[vertex] + 1: #True == мы первый раз видим v
				D[v] = D[vertex] + 1
				Q.append(v)

graph = read_graph_as_list()
count_components = 0
D = [float('+inf') for i in range(len(graph))]
for v in graph:
	if D[v] == float('+inf'):
		count_components += 1
		bfs(v, graph, D)
