#task_1
class Vector():

	def __init__(self, s = "0,0"):
		s = s.split(',')
		self.x = float(s[0])
		self.y = float(s[1])

	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)

	def __str__(self):
		return "Vector(x = " + str(self.x) + ", y = " + str(self.y) + ")"
	
	def print(self,msg):
		print("Vector(x = " + str(self.x) + ", y = " + str(self.y) + ")")

	def abs(self):
		return (self.x ** 2 + self.y ** 2) ** 0.5

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __lt__(self, other):
		return self.abs() < other.abs()

	def __le__(self, other):
		return self.abs() <= other.abs()

	def __gt__(self, other):
		return self.abs() > other.abs()

	def __ge__(self, other):
		return self.abs() >= other.abs()

n = int(input())
Points = [Vector(input()) for i in range(n)]
print([str(a) for a in Points])
Points.sort()
print(Points[-1])