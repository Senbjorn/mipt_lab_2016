#task_5
min_path = None
min_w = float('+inf')

def dfs(vertex, graph, path, visited_t):
	global min_path, min_w
	visited_t.add(vertex)
	path.append(vertex)
	for v in graph[vertex]:
		if v == path[0] and len(path) == len(graph):
			s = sum([graph[path[i]][path[i + 1]] for i in range(-1, len(path) - 1)])
			min_w, min_path = (s, list(path)) if min_w > s else (min_w, min_path)
		if v not in visited_t and dfs(v, graph, path, visited_t):
			return True
	path.pop()
	visited_t.remove(vertex)
	return False

n, m = tuple(map(int, input().split()))
graph = {i: {} for i in range(n)}
for j in range(m):
	a, b, w = tuple(map(int, input().split()))
	graph[a][b] = w
	graph[b][a] = w

path = list()
dfs(0, graph, path, set())
print(min_w)
print(*min_path)