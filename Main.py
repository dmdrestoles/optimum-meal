from Graph import *
from Food import *

EA_DISHES = load_dishes(east_asian_dishes)
FIL_DISHES = load_dishes(filipino_dishes)
FR_DISHES = load_dishes(french_dishes)

def prepare_cuisine(dishes: Graph):
	print("=== AUTOMATED MEAL PREPARATION SELECTION ===")
	print("Type the number you want your %s meal to be selected." % (dishes.name))
	print("[1] Random selection (DFS)")
	print("[2] Cheapest set (A*)")
	print("[3] Go back")
	response = int(input(">> "))

	if response == 1:
		dishes.DFS(START_VERTEX, 5)
		response = input("Do you want to wish for more? [Y/N]: ")
	
	elif response == 2:
		dishes.A_STAR(START_VERTEX, GOAL_VERTEX, dishes.heuristic)
		response = input("Do you want to wish for more? [Y/N]: ")

	elif response == 3:
		order_meal()
	
	else:
		print("Invalid input detected. Repeating the interface.")
		prepare_cuisine()
	

	if response == "Y":
		main_menu()
	else:
		print("I am glad to be in your service.")


def list_menu():
	print("============ FOOD ITEM INTERFACE ============")
	print("=============== EAST ASIAN ==================")
	for dish, foods in east_asian_dishes.food_list.items():
		i = 1
		print("==== [%s] ====" % (dish))

		for food in foods:
			print("[%d] %s (%d)" % (i, food.get_name(), food.get_cost()))
			i += 1
	print("================ FILIPINO ===================")
	for dish, foods in filipino_dishes.food_list.items():
		i = 1
		print("==== [%s] ====" % (dish))

		for food in foods:
			print("[%d] %s (%d)" % (i, food.get_name(), food.get_cost()))
			i += 1
	print("================= FRENCH ====================")
	for dish, foods in french_dishes.food_list.items():
		i = 1
		print("==== [%s] ====" % (dish))

		for food in foods:
			print("[%d] %s (%d)" % (i, food.get_name(), food.get_cost()))
			i += 1
	main_menu()

def order_meal():
	print("============ ORDERING INTERFACE ============")
	print("Type the number of the meal you want to order")
	print("[1] East Asian Cuisine")
	print("[2] Filipino Cuisine")
	print("[3] French Cuisine")
	print("[4] Go back")
	response = int(input(">> "))

	if response == 1:
		prepare_cuisine(EA_DISHES)
		
	
	elif response == 2:
		prepare_cuisine(FIL_DISHES)
		

	elif response == 3:
		prepare_cuisine(FR_DISHES)
		

	elif response == 4:
		main_menu()
		

	else:
		print("Invalid input detected. Repeating the interface.")
		order_meal()

def main_menu():
	print("== HELLO ALADDIN, YOUR WISH IS MY COMMAND ==")
	print("Type the number you want to proceed towards")
	print("[1] Order meal")
	print("[2] List down menu")
	print("[5] Quit application")
	response = int(input(">> "))

	if response == 5:	
		print("I am glad to be in your service.")
	
	elif response == 2:
		list_menu()
		
	elif response == 1:
		order_meal()
		
	else:
		print("Invalid input detected. Repeating the instructions.")
		main_menu()
	

main_menu()