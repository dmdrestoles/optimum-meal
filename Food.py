import csv
import random

class Food:
	"""
	A Food class that stores information about the food's name, cost, and type.
	"""
	def __init__(self, name, cost, type):
		self.name = name
		self.cost = int(cost)
		self.type = type

	def __str__(self):
		return ("%s (%d)" % (self.name, self.cost))

	def __repr__(self):
		return ("%s (%d)" % (self.name, self.cost))

	def get_name(self):
		return self.name

	def get_cost(self):
		return self.cost

	def get_type(self):
		return self.type

class Cuisine:
	"""
	A Cuisine class handles Food objects grouped by cuisines.
	"""
	def __init__(self, name):
		self.name = name
		self.food_list = {
			"Main Dish": [],
			"Side Dish": [],
			"Dessert": []
		}

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name

	def add_food(self, food: Food):
		self.food_list[food.get_type()].append(food)

	def shuffle(self):
		for key, val in self.food_list.items():
			random.shuffle(val)

east_asian_dishes = Cuisine('East Asian')

with open('East Asian.csv') as f:
	reader = csv.reader(f, delimiter=',')

	for row in reader:
		foodentry = Food(row[0], row[1], row[2])
		east_asian_dishes.add_food(foodentry)

filipino_dishes = Cuisine('Filipino')

with open('Filipino.csv') as f:
	reader = csv.reader(f, delimiter=',')

	for row in reader:
		foodentry = Food(row[0], row[1], row[2])
		filipino_dishes.add_food(foodentry)

french_dishes = Cuisine('French')

with open('French.csv') as f:
	reader = csv.reader(f, delimiter=',')

	for row in reader:
		foodentry = Food(row[0], row[1], row[2])
		french_dishes.add_food(foodentry)