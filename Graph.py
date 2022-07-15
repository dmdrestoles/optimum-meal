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

	def __init__(self):
		self.cost = 0
		self.graph = defaultdict(list)

	def __str__(self):
		return str(self.graph)

	def __repr__(self):
		return str(self.graph)

	def add_edge(self, node, other):
		self.graph[node].append(other)

	def DFS(self, starting_vertex: Vertex, depth_limit: int):
		print("Starting DFS!")
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
