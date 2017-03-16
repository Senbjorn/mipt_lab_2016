#task_4

def dfs(vertex, graph, path, visited_t):
	visited_t.add(vertex)
	path.append(vertex)
	for v in graph[vertex]:
		if v == path[0] and len(path) == len(graph):
			return True
		if v not in visited_t and dfs(v, graph, path, visited_t):
			return True
	path.pop()
	visited_t.remove(vertex)
	return False

n, m = tuple(map(int, input().split()))
graph = [[] for i in range(n)]
for j in range(m):
	a, b = tuple(map(int, input().split()))
	graph[a].append(b)
	graph[b].append(a)

path = list()
dfs(0, graph, path, set())
print(*path)