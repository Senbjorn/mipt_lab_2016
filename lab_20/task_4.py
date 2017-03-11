#task_4
import matplotlib.pyplot as plt
import networkx as nx
import random as rand

def get_random_color():
	return "#%02X%02X%02X" %(rand.randint(0, 256), rand.randint(0, 256), rand.randint(0, 256))

# reading form file
input_file = open('data.txt', 'r')
list_of_lines = input_file.readlines()
# creating nodes and edges of the graph
graph = nx.Graph()
for s in list_of_lines:
	a, b, w = tuple(s.split())
	w = float(w)
	graph.add_edge(a, b, weight = w)
pos = nx.shell_layout(graph)
components = list(nx.connected_component_subgraphs(graph))
for i in range(len(components)):
	print(len(components[i]))
	color = get_random_color()
	nx.draw_networkx_nodes(components[i], pos,
		nodelist = [v for v in components[i]],
		node_color = color,
		alpha = 1)
	nx.draw_networkx_edges(graph, pos,
		edgelist = [e for e in components[i].edges()],
		edge_color = color,
		alpha = 1)
plt.show()