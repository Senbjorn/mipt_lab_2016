#task_1
def dfs(vertex, graph, visited_c = set(), visited_f = set()):
	visited_c.add(vertex)
	for v in graph[vertex]:
		if v in visited_c:
			return [v]
		if v in visited_f:
			continue
		cycle = dfs(v, graph, visited_c, visited_f)
		if not cycle is None:
			if cycle[-1] is None:
				return cycle
			cycle.append(v)
			if vertex == cycle[0]:
				cycle.append(None)
			return cycle
	visited_c.remove(vertex)
	visited_f.add(vertex)
	return None

n, m = tuple(map(int, input().split()))
graph = [[] for i in range(n)]
for j in range(m):
	a, b = tuple(map(int, input().split()))
	graph[a].append(b)

visited_f = set()
for v in range(n):
	if v not in visited_f:
		cycle = dfs(v, graph, set(), visited_f)
		if not cycle is None:
			print(*(cycle[-2::-1]))
			break
else:
	print('YES')