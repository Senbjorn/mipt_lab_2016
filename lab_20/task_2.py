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
#constructing spanning tree using depth first search
pos = nx.spring_layout(graph)
used = set()
for node in graph:
	if node not in used:
		tree_dfs = nx.dfs_tree(graph, node)
		paths = nx.single_source_dijkstra_path(tree_dfs, node)
		labels = {v: len(paths[v]) - 1 for v in paths}
		nx.draw_networkx_nodes(graph, pos,
								nodelist = tree_dfs.nodes(),
								node_color = 'g')
		nx.draw_networkx_edges(graph, pos,
								edgelist = tree_dfs.edges(),
								edge_color = 'r')
		nx.draw_networkx_labels(graph, pos,
								labels = labels,
								font_size = 12)
		used.update(set(tree_dfs.nodes()))
plt.show()