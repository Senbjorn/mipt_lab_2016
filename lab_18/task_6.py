def reverse(graph):
	n = len(graph)
	rgraph = [[] for i in range(n)]
	for a in range(n):
		for v in graph[a]:
			rgraph[v].append(a)
	return rgraph

def deep_search(vertex, graph, marked = set(), vector = list(), app = True):
	marked.add(vertex)
	if not app:
		vector.remove(vertex)
	for v in graph[vertex]:
		if v not in marked:
			deep_search(v, graph, marked, vector, app)
	if app:
		vector.append(vertex)

def get_vector(graph):
	n = len(graph)
	S = set(range(n))
	vector = list()
	marked = set()
	while len(marked) != n:
		a = S.pop()
		deep_search(a, graph, marked, vector)
		S.difference_update(marked)
	return vector

def number_of_weak(graph):
	n = len(graph)
	new_graph = [[] for i in range(n)]
	for i in range(n):
		new_graph[i] = list(graph[i])
		for j in graph[i]:
			if not i in new_graph[j]:
				new_graph[j].append(i)
	marked = set()
	number_of_components = 0
	for i in range(n):
		if i not in marked:
			deep_search(i, new_graph, marked)
			number_of_components += 1
	return number_of_components

def number_of_strong(graph):
	n = len(graph)
	s = 0
	rgraph = reverse(graph)
	vector = get_vector(graph)
	marked = set()
	while len(marked) != n:
		s += 1
		deep_search(vector[-1], rgraph, marked, vector, False)
	return s

n, m = int(input()), int(input())
graph = [[] for i in range(n)]
for i in range(m):
	a, b = tuple(map(int, input().split()))
	graph[a].append(b)
print(number_of_weak(graph), number_of_strong(graph))


