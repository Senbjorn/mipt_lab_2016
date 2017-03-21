#task_2
def dfs(vertex, graph, used):
	used.add(vertex)
	for v in graph[vertex]:
		if v not in used:
			dfs(v, graph, used)

graph = read_graph_as_list()
used = set()
count_components = 0
for v in graph:
	if v not in used:
		count_components += 1
		dfs(v, graph, used)
