#task_3
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
#constructing spanning tree using breadth first search
pos = nx.spring_layout(graph)
used = set()
for node in graph:
	if node not in used:
		tree_bfs = nx.bfs_tree(graph, node)
		paths = nx.single_source_dijkstra_path(tree_bfs, node)
		labels = {v: len(paths[v]) - 1 for v in paths}
		nx.draw_networkx_nodes(graph, pos,
								nodelist = tree_bfs.nodes(),
								node_color = 'y')
		nx.draw_networkx_edges(graph, pos,
								edgelist = tree_bfs.edges(),
								edge_color = 'orange')
		nx.draw_networkx_labels(graph, pos,
								labels = labels,
								font_size = 12)
		used.update(set(tree_bfs.nodes()))
plt.show()