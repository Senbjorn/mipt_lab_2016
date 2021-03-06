#task_1
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class Tree:
	def __init__(self):
		self.root = None

	def add(self, data):
		node = Node(data)
		if self.root is None:
			self.root = node
			return
		T = Tree()
		if self.root.data > data:
			if self.root.left is None:
				self.root.left = node
				return
			else:
				T.root = self.root.left
		elif self.root.data < data:
			if self.root.right is None:
				self.root.right = node
				return
			else:
				T.root = self.root.right
		else:
			return
		T.add(data)
	def print(self):
		if self.root is None:
			return
		T = Tree()
		T.root = self.root.left
		T.print()
		print(self.root.data, end = ' ')
		T = Tree()
		T.root = self.root.right
		T.print()

tree = Tree()
for x in [0, 1, 0, 1, 0, 1]:
	tree.add(x)
tree.print()