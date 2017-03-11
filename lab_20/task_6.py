#task_6
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
# поиск и вывод пути
pos = nx.circular_layout(graph)
s, t = graph.nodes()[0], graph.nodes()[6]
print('Из ', s, 'в ', t)
path = list()
if nx.has_path(graph, s, t):
	path = nx.shortest_path(graph, s, t, 'weight')
	print(path)
else:
	print('нет пути!')
nx.draw_networkx_nodes(graph, pos,
						nodelist = [node for node in graph if node not in path],
						node_color='blue',
						node_size=400,
						alpha=0.5)
nx.draw_networkx_edges(graph, pos,
							edgelist = [edge for edge in graph.edges() if edge not in [(path[i - 1], path[i]) for i in range(1, len(path))]],
							alpha=0.5,
							edge_color='green')
nx.draw_networkx_nodes(graph, pos, nodelist = path,
						node_color='red',
						node_size=300,
						alpha=1)
nx.draw_networkx_edges(nx.DiGraph(graph), pos,
							edgelist = [(path[i - 1], path[i]) for i in range(1, len(path))],
							alpha=1,
							edge_color='orange',
							arrows = True)
nx.draw_networkx_labels(graph, pos,
						labels = {s: '1', t: '2'})
plt.show()
# PATH=C:\Program Files\Common Files\Microsoft Shared\Windows Live;C:\Users\Semjon\AppData\Local\Programs\Python\Python35-32\Scripts;C:\Users\Semjon\AppData\Local\Programs\Python\Python35-32;C:\ProgramData\Oracle\Java\javapath;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Program Files (x86)\ATI Technologies\ATI.ACE\Core-Static;C:\Program Files (x86)\Skype\Phone\;C:\Program Files\Git\cmd;C:\Program Files\Common Files\Microsoft Shared\Windows Live;C:\Users\Semjon\LaTeX\miktex\bin\x64\;