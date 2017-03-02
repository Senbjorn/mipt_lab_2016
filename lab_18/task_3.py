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
number_of_components = 0
for i in range(n):
	if i not in marked:
		deep_search(i, graph, marked)
		number_of_components += 1
print(number_of_components)