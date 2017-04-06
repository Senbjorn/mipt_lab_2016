#task_3
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

	def height(self, h = 0):
		if self.root is None:
			return h
		T1 = Tree()
		T1.root = self.root.left
		T2 = Tree()
		T2.root = self.root.right
		return max(T1.height(h + 1), T2.height(h + 1))

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
for x in list(map(int, input().split())):
	tree.add(x)
print(tree.height())