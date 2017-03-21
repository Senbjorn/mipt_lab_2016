#task_4
def dfs_tree(vertex, graph, tree, used):
	used.add(vertex)
	for v in graph[vertex]:
		if v not in used:
			tree[vertex].append(v) # для орграфа (для просто графа надо tree[v].append(vertex))
			dfs(v, graph, tree, used)

#use of dfs_tree
#In the begining tree is an empty graph
graph = read_graph_as_list()
tree = [[] for i in range(len(graph))]
dfs_tree(0, graph, tree, set())