#task_2_3.py
class Animal():
	__description = ""
	__name = ""
	__age = ""

	def __init__(self, description, name, age):
		self.__description = description
		self.__name = name
		self.__age = age

	def get_description(self):
		return self.__description

	def set_description(self, description):
		self.__description = description

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	def get_age(self):
		return self.__age

	def set_age(self, age):
		self.__age = age

	def __str__(self):
		return (
			"Animal: name = " + self.get_name() +
			"age = " + str(self.get_age()) +
			"\nDescription: " + str(self.get_description()) + "."
			)


class Zebra(Animal):
	__white_stripes = 0
	
	def __init__(self, name, age, white_stripes, description = "My little Zebra"):
		self.__white_stripes = white_stripes
		Animal.__init__(self, description, name, age)

	def get_white_stripes(self):
		return self.__white_stripes

	def set_white_stripes(self, white_stripes):
		self.__white_stripes = white_stripes

	def __str__(self):
		return (
			"Zebra: name = " + self.get_name() +
			"; age = " + str(self.get_age()) +
			"; white stripes = " + str(self.__white_stripes) +
			"\nDescription: " + str(self.get_description()) + "."
			)


class Dolphin(Animal):
	__hydrodynamics = 0
	
	def __init__(self, name, age, hydrodynamics, description = "My hot big black dolphin"):
		self.__hydrodynamics = hydrodynamics
		Animal.__init__(self, description, name, age)

	def get___hydrodynamics(self):
		return self.__hydrodynamicses

	def set___hydrodynamics(self, hydrodynamics):
		self.__hydrodynamics = hydrodynamics

	def __str__(self):
		return (
			"Dolphin: name = " + self.get_name() +
			"; age = " + str(self.get_age()) +
			"; hydrodynamics = " + str(self.__hydrodynamics) +
			"\nDescription: " + str(self.get_description()) + "."
			)

if __name__ == "__main__":
	d = Dolphin("Asis", 32, 100)
	z = Zebra("Mrzish", 28, 2, description = "Double striped zebra")
	print(d)
	print(z)