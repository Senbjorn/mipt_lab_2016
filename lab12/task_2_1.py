#task_2_1
class Shape():
	__height = 0
	__length = 0

	def __init__(self ,height, length):
		self.__height = height
		self.__length = length

	def get_height(self):
		return self.__height

	def get_length(self):
		return self.__length

	def set_height(self, height):
		self.__height = height

	def set_length(self, length):
		self.__length = length

	def area(self):
		return None

	def __str__(self):
		return "(" + str(type(self)) + "; height = " + str(self.get_height()) + "; length = " + str(self.get_length()) + ")"

class Triangle(Shape):
	__a = 1
	__b = 1
	__c = 1

	def __init__(self, a, b, c):
		self.__a = a
		self.__b = b
		self.__c = c
		length = max(a, b, c)
		self.set_length(length)
		self.set_height(2 * self.area() / length)

	def area(self):
		a = self.__a
		b = self.__b
		c = self.__c
		p = (a + b + c) / 2
		return ((p - a) * (p - b) * (p - c) * p) ** 0.5

	def get_sibes(self):
		return [self.__a, self.__b, self.__c]

	def __str__(self):
		return ("(" + str(type(self)) + "; height = " + str(self.get_height()) + "; length = " + str(self.get_length())
			+ "; a = " + str(self.__a) + "; b = " + str(self.__b) + "; c = " + str(self.__c) + ")")


class Rectangle(Shape):
	def area(self):
		return self.get_height() * self.get_length()

if __name__ == "__main__":
	shape_1 = Shape(1, 2)
	print(shape_1)
	triangle_1 = Triangle(3, 4, 5)
	print(triangle_1, triangle_1.area())
	rectangle_1 = Rectangle(3, 5)
	print(rectangle_1, rectangle_1.area())