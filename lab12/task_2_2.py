#task_2_2.py
class Mother():
	__name = "Maaam"

	def __init__(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

	def __str__(self):
		return "-m: I'm mother. My name is " + self.__name + "."


class Doughter(Mother):
	def __str__(self):
		return "-d: I'm doughter. My name is " + self.get_name() + "."


if __name__ == "__main__":
	m = Mother("Alla")
	d = Doughter("Nika")
	print(m, d)