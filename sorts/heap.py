from random import randint

class Heap():

	def __init__(self):
		self._heap = []

	def push(self, data):
		self._heap.append(data)
		i = len(self._heap) - 1
		while i != 0:
			p = (i - 1) // 2
			if self._heap[i] <= self._heap[p]:
				return
			else:
				self._heap[i], self._heap[p] = self._heap[p], self._heap[i]
				i = p

	def pop(self):
		if len(self._heap) == 0:
			raise IndexError
		if len(self._heap) == 1:
			return self._heap.pop()
		result = self._heap[0]
		self._heap[0] = self._heap.pop()
		i = 0
		while i * 2 + 1 < len(self._heap):
			c = i * 2 + 1
			lc = self._heap[c]
			rc = self._heap[c + 1] if c + 1 < len(self._heap) else lc
			if lc >= rc and self._heap[i] < lc:
				self._heap[i], self._heap[c] = self._heap[c], self._heap[i]
				i = c
			elif lc < rc and self._heap[i] < rc:
				self._heap[i], self._heap[c + 1] = self._heap[c + 1], self._heap[i]
				i = c + 1
			else:
				return result
		return result

def heap_sort(A):
	heap = Heap()
	for x in A:
		heap.push(x)
	for i in range(len(A)):
		A[i] = heap.pop()

A = [randint(0, 20) for i in range(10)]
print(*A)
heap_sort(A)
print(*A)


