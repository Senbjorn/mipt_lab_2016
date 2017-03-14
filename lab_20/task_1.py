#task_1
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
pos = nx.circular_layout(graph)
nodes = graph.nodes()
labels={nodes[i]:i + 1 for i in range(len(nodes))}
nx.draw_networkx_nodes(graph, pos,
                       node_color='b')
nx.draw_networkx_edges(graph, pos,
						edge_color='g')
nx.draw_networkx_labels(graph, pos,
						labels = labels)
plt.show()