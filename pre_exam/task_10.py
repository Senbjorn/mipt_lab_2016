#task_10
#Тарьяна алгоритм
def dfs(vertex, graph, top_sorted, visited_t, visited_p):
	visited_t.add(vertex)
	for v in graph[vertex]:
		if v in visited_t:
			return False
		if v not in visited_p and not dfs(v, graph, top_sorted, visited_t, visited_p):
			return False
	visited_t.remove(vertex)
	visited_p.add(vertex)
	top_sorted.append(vertex)
	return True

n, m = tuple(map(int, input().split()))
graph = [[] for i in range(n)]
for j in range(m):
	a, b = tuple(map(int, input().split()))
	graph[a].append(b)
visited_p = set()
top_sorted = list()
for v in range(n):
	if v not in visited_p and not dfs(v, graph, top_sorted, set(), visited_p):
		print('NO')
		break
else:
	print(*top_sorted[-1::-1])