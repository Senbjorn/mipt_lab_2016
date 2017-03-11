#task_5
import matplotlib.pyplot as plt
import networkx as nx

# reading form file
input_file = open('data.txt', 'r')
list_of_lines = input_file.readlines()
# creating nodes and edges of the graph
graph = nx.Graph()
for s in list_of_lines:
	a, b, w = tuple(s.split())
	graph.add_edge(a, b, weight = float(w))
node = graph.nodes()[6]
print(node)
for i in graph.nodes():
	if nx.has_path(graph, node, i):
		print(i, ': ', nx.shortest_path_length(graph, node, i, 'weight'))
	else:
		print(i, ': ', 'нет пути!')