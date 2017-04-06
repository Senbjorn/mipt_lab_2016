#task_7

class Node:
	def __init__(self, data):
		self.data = data
		self.value = 1
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
			self.root.value += 1
			return
		T.add(data)

	def is_balanced(self):
		if self.root is None:
			return True
		T1 = Tree()
		T1.root = self.root.left
		T2 = Tree()
		T2.root = self.root.right
		if abs(T1.height() - T2.height()) > 1:
			return False
		return T1.is_balanced() and T2.is_balanced()

	def leaves(self):
		if self.root is None:
			return
		if self.root.left is None and self.root.right is None:
			print(self.root.data, end = ' ')
		T1 = Tree()
		T1.root = self.root.left
		T2 = Tree()
		T2.root = self.root.right
		T1.leaves()
		T2.leaves()

	def height(self, h = 0):
		if self.root is None:
			return h
		T1 = Tree()
		T1.root = self.root.left
		T2 = Tree()
		T2.root = self.root.right
		return max(T1.height(h + 1), T2.height(h + 1))

	def bfs(self):
		ind = 0
		Q = [self.root]
		while ind < len(Q):
			node = Q[ind]
			ind += 1
			if not node.left is None:
				Q.append(node.left)
			if not node.right is None:
				Q.append(node.right)
		print(*[q.data for q in Q])


	def print(self):
		if self.root is None:
			return
		T = Tree()
		T.root = self.root.left
		T.print()
		print(self.root.data, self.root.value)
		T = Tree()
		T.root = self.root.right
		T.print()
tree = Tree()
for x in list(map(int, input().split())):
	tree.add(x)
tree.bfs()