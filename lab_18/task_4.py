def deep_search(vertex, graph, marked = set()):
	marked.add(vertex)
	for v in graph[vertex]:
		if v not in marked:
			deep_search(v, graph, marked)

def component(vertex, graph):
	marked = set()
	deep_search(vertex, graph, marked)
	if len(marked) != len(graph):
		return Falsedef deep_search(vertex, graph, marked = set()):
	marked.add(vertex)
	for v in graph[vertex]:
		if v not in marked:
			deep_search(v, graph, marked)

def component(vertex, graph):
	marked = set()
	deep_search(vertex, graph, marked)
	if len(marked) != len(graph):
		return False
	return True

def strong_connectivity(graph):
	for i in range(len(graph)):
		if not component(i, graph):
			return False
	return True

n, m = int(input()), int(input())
graph = [[] for i in range(n)]
for i in range(m):
	a, b = tuple(map(int, input().split()))
	graph[a].append(b)
if strong_connectivity(graph):
	print('YES')
else:
	print('NO')