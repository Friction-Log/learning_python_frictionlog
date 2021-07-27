# create a class called Car

class Car:
	def __init__(self, make, model, year):
		# this is the constructor, it creates an instance of the class Car
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		# this is a method that returns a string that describes the car
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		# this is a method that prints a statement showing the car's mileage
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		# this is a method that updates the mileage
		# only if the mileage is higher than the previous mileage
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		# this is a method that increments the mileage
		# only if the mileage is higher than the previous mileage
		if miles >= 0:
			self.odometer_reading += miles
		else:
			print("You can't roll back an odometer!")

# create an instance of the class Car
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

