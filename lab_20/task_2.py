#task_2
import matplotlib.pyplot as plt
import networkx as nx

# reading form file
input_file = open('data.txt', 'r')
list_of_lines = input_file.readlines()
# creating nodes and edges of the graph
graph = nx.Graph()
for s in list_of_lines:
	a, b, w = tuple(s.split())
	w = float(w)
	graph.add_edge(a, b, weight = w)
tree_dfs = nx.Graph()
for node in graph:
	if node not in tree_dfs:
		tree_dfs.add_edges_from(nx.dfs_tree(graph, node).edges())
nx.draw_spring(tree_dfs)
plt.show()