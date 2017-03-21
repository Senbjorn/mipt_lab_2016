#task_5
def bfs_tree(start, graph, tree):
	D = [float('+inf') for i in range(len(graph))]
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
				tree[vertex].append(v) # для орграфа (для просто графа надо tree[v].append(vertex))

#use of bfs_tree
#In the begining tree is an empty graph
graph = read_graph_as_list()
tree = [[] for i in range(len(graph))]
bfs_tree(0, graph, tree)