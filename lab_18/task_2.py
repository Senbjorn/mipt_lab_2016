def deep_search(vertex, graph, marked = set()):
	marked.add(vertex)
	for v in graph[vertex]:
		if v not in marked:
			deep_search(v, graph, marked)

n, m = int(input()), int(input())
graph = [[] for i in range(n)]
for i in range(m):
	a, b = tuple(map(int, input().split()))
	graph[a].append(b)
	graph[b].append(a)
marked = set()
deep_search(0, graph, marked)
if len(marked) == n:
	print('YES')
else:
	print('NO')
