#task_3
def alg_prima(graph):
	in_processing = {(0, u) for u in graph[0]}
	in_tree = {0}
	edge_list = []
	while True:
		min_v = float('+inf')
		min_e = None
		for e in list(in_processing):
			s, t = e
			if t in in_tree:
				in_processing.remove(e)
				continue
			if graph[s][t] < min_v:
				min_v = graph[s][t]
				min_e = e
		if min_e is None:
			break
		edge_list.append(min_e)
		in_processing.update({(min_e[1], v) for v in graph[min_e[1]] if v not in in_tree})
		in_tree.add(min_e[1])
	return edge_list

n, m = tuple(map(int, input().split()))
graph = {i: {} for i in range(n)}
for j in range(m):
	a, b, w = tuple(map(int, input().split()))
	graph[a][b] = w
	graph[b][a] = w
edge_list = alg_prima(graph)
w = sum(graph[a][b] for a, b in edge_list)
print(w)
for i in range(len(edge_list)):
	print(*edge_list[i])
