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
pos = nx.spring_layout(graph)
labels={i:"aaa" for i in graph.nodes()}
nx.draw_networkx_nodes(graph, pos,
                       node_color='b',
                       node_size=500,
                   alpha=0.8)
nx.draw_networkx_edges(graph, pos, width=8, alpha=0.5, edge_color='g')
nx.draw_networkx_labels(graph, pos, labels, font_size=16)
plt.show()