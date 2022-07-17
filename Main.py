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
		pass
	
	elif response == 2:
		dishes.A_STAR(START_VERTEX, GOAL_VERTEX, dishes.heuristic)
		pass

	elif response == 3:
		order_meal()
		pass
	
	else:
		print("Invalid input detected. Repeating the interface.")

def list_menu():
	pass

def order_meal():
	while True:
		print("============ ORDERING INTERFACE ============")
		print("Type the number of the meal you want to order")
		print("[1] East Asian Cuisine")
		print("[2] Filipino Cuisine")
		print("[3] French Cuisine")
		print("[4] Go back")
		response = int(input(">> "))

		if response == 1:
			prepare_cuisine(EA_DISHES)
			break
		
		elif response == 2:
			prepare_cuisine(FIL_DISHES)
			break

		elif response == 3:
			prepare_cuisine(FR_DISHES)
			break

		elif response == 4:
			main_menu()
			break

		else:
			print("Invalid input detected. Repeating the interface.")

def main_menu():
	while True:
		print("== WELCOME TO GRAB GLOBAL ORDER INTERFACE ==")
		print("Type the number you want to proceed towards")
		print("[1] Order meal")
		print("[2] List down menu")
		print("[3] Quit application")
		response = int(input(">> "))

		if response == 3:
			break
		
		elif response == 2:
			list_menu()
			break

		elif response == 1:
			order_meal()
			break
		
		else:
			print("Invalid input detected. Repeating the interface.")
	
	print("Thank you for using the Grab Global Order Interface!")

main_menu()