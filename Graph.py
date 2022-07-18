from collections import defaultdict

from Food import *

class Vertex:
	"""
	A Vertex class that serves as nodes in the Graph class.
	"""
	def __init__(self, data, goal):
		self.data = data
		self.next = None
		self.successors = []
		self.is_visited = False
		self.goal = goal

	def __str__(self):
		return str(self.data)

	def __repr__(self):
		return str(self.data)

	def add_next(self, vertex):
		self.next = vertex

	def has_visited(self):
		return self.is_visited

	def get_successors(self):
		return self.successors
	
	def add_successor(self, state):
		self.successor.append(state)

	def visited(self):
		self.is_visited = True

	def get_data(self):
		return self.data


class Graph:
	"""
	Generates a graph, based on this tutorial:
	https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
	A specialized graph that counts the cost of the data.
	"""

	def __init__(self, name):
		self.cost = 0
		self.name = name
		self.graph = defaultdict(list)
		self.heuristic = None

	def get_neighbors(self, v):
		return self.graph[v]
 
    # This is heuristic function which is having equal values for all nodes
	def h(self, n):
		return self.heuristic[str(n)]

	def __str__(self):
		return str(self.graph)

	def __repr__(self):
		return str(self.graph)

	def add_edge(self, node, other):
		self.graph[node].append(other)

	def DFS(self, starting_vertex: Vertex, depth_limit: int):
		stack = []

		stack.append(starting_vertex)

		while stack:
			starting_vertex = stack[-1]
			stack.pop()
			if type(starting_vertex.data) == Food:
				self.cost += starting_vertex.data.get_cost() 
				print("Selecting %s: %s (%d)" % (starting_vertex.data.get_type(), starting_vertex.data.get_name(), starting_vertex.data.get_cost()))

			if (starting_vertex.goal):
				print("Meal selection done!")
				print("Total cost: %d" % (self.cost))
				break

			if not starting_vertex.has_visited():
				starting_vertex.visited()

			for vertex in self.graph[starting_vertex]:
				if not vertex.has_visited():
					stack.append(vertex)

	def A_STAR(self, start: Vertex, stop: Vertex, heuristic):
		# In this open_lst is a list of nodes which have been visited, but who's 
        # neighbours haven't all been always inspected, It starts off with the start node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been inspected
		open_lst = set([start])
		closed_lst = set([])
 
        # distances has present distances from start to all other nodes
        # the default value is +infinity
		distances = {}
		distances[start] = 0
 
        # adjacencies contains an adjac mapping of all nodes
		adjacencies = {}
		adjacencies[start] = start
 
		while len(open_lst) > 0:
			n = None
 
            # it will find a node with the lowest value of f() -
			for v in open_lst:
				if n == None or distances[v] + self.h(v) < distances[n] + self.h(n):
					n = v
				
				if n == None:
					print('Path does not exist! No content for n!')
					return None
 
            # if the current node is the stop
            # then we start again from start
			if n == stop:
				created_path = []

				while adjacencies[n] != n:
					created_path.append(n)
					n = adjacencies[n]

				created_path.append(start)

				created_path.reverse()

				created_meal = created_path[1:4]

				for food in created_meal:
					print("Selecting %s: %s (%d)" % (food.data.get_type(), food.data.get_name(), food.data.get_cost()))
				
				print("Meal selection done!")
				print("Total cost: %d" % (distances[v]))
				return created_path
 
            # for all the neighbors of the current node do
			for vertex in self.get_neighbors(n):
			# if the current node is not presentin both open_lst and closed_lst
			# add it to open_lst and note n as it's adjacencies
				if vertex not in open_lst and vertex not in closed_lst:
					open_lst.add(vertex)
					adjacencies[vertex] = n
					if isinstance(vertex.data, Food):
						distances[vertex] = distances[n] + vertex.data.get_cost()
					else:
						distances[vertex] = distances[n]

				# otherwise, check if it's quicker to first visit n, then m
				# and if it is, update adjacencies data and distances data
				# and if the node was in the closed_lst, move it to open_lst
				else:
					if distances[vertex] > distances[n] + vertex.data.get_cost():
						distances[vertex] = distances[n] + vertex.data.get_cost()
						adjacencies[vertex] = n

						if vertex in closed_lst:
							closed_lst.remove(vertex)
							open_lst.add(vertex)

			# remove n from the open_lst, and add it to closed_lst
			# because all of his neighbors were inspected
			open_lst.remove(n)
			closed_lst.add(n)

		print('Cannot create meal! We apologize for this error.')
		return None

START_VERTEX = Vertex("START", False)
GOAL_VERTEX = Vertex("GOAL", True)

def load_dishes(cuisine: Cuisine):
	cuisine.shuffle()
	
	vertices = [ [START_VERTEX] ]
	heuristic = dict()
	heuristic[str(START_VERTEX)] = 1
	# List down nodes
	for type, dishes in cuisine.food_list.items():
		dish_group = []
		for dish in dishes:
			dish_group.append(Vertex(dish, False))
			heuristic[str(Vertex(dish, False))] = 1
			
		vertices.append(dish_group)
		pass
	
	# print(heuristic)
	vertices.append( [GOAL_VERTEX] )
	heuristic[str(GOAL_VERTEX)] = 1
	#print(vertices)
	# Declare graph edges
	
	graph = Graph(cuisine.name)
	graph.heuristic = heuristic

	# print("Heuristic: %s" % (graph.heuristic))
	previous_group = []
	for dish_group in vertices:
		new_group = dish_group
		#print("New group: %s" % (str(new_group)))
		
		if previous_group:
			paired_edges = [(x,y) for x in previous_group for y in new_group]

			for i in paired_edges:
				graph.add_edge(i[0], i[1])

			#print(paired_edges)
		previous_group = new_group

	return graph