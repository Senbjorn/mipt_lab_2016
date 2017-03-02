#task_H
def dijkstra(start, graph):
	n = len(graph)
	D = [None] * n
	D[start] = 0
	index = 0
	Q = [start]
	while index < len(Q):
		v = Q[index]
		index += 1
		for u in graph[v]:
			if D[u] == None or D[v] + min(graph[v][u]) < D[u]:
				D[u] = D[v] + min(graph[v][u])
				Q.append(u)
	return D

def reverse(graph):
	n = len(graph)
	graph_reversed = {x: {} for x, y in zip(range(n), range(n))}
	for i in range(n):
		for v in graph[i]:
			for w in graph[i][v]:
				add(graph_reversed, v, i, w)

def add(graph, a, b, w):
	if b in graph[a]:
		grph[a][b].append(w)
	else:
		graph[a][b] = [w]

def min_vertex(x, D, graph):
	A = {v: w + D[v] for v, w in zip([u for u in graph[x].keys if D[u] != None], [min(graph[x][u]) for u in graph[x].keys if D[u] != None])}
	L = list(A.items)
	min_i = L[0][0]
	min_v = L[0][1]
	for v in A:
		if A[v] < min_v:
			min_v = A[v]
			min_i = v
	return min_i
def path(graph, D, s, f):
	graph = reverse(graph)
	x = f
	P = [f]
	while x != s:
		x = min_vertex(x, D, graph)
		P.append(x)
	return P[-1::-1] 

n, m, s, f = tuple(map(int, input().split()))
graph = {x: {} for x, y in zip(range(n), range(n))}
for i in range(m):
	a, b, w = tuple(map(int, input().split()))
	add(graph, a, b, w)
	add(graph, b, a, w)
D = dijkstra(s, graph)
print(*path(graph, D, s, f))