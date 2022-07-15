from collections import defaultdict


class Node:

	def __init__(self, data, goal):
		self.data = data
		self.next = None
		self.goal = goal

	def __str__(self):
		return self.data

	def add_next(self, node):
		self.next = node


class Stack:
	"""
	A native implementation of a stack that uses nodes' self and next for
	accessing and moving through the stack
	"""
	def __init__(self):
		self.head = None

	def is_empty(self):
		if self.head:
			return False
		return True

	def push(self, node):
		if self.head is not None:
			self.head.add_next(node)
		self.head = node
	
	def pop(self):
		current_head = None
		if self.head is None:
			print("Error, stack is empty!")
		else:
			current_head = self.head
			self.head = self.head.next

		return current_head

	def peek(self):
		print( self.head )
		return self.head.data

class Queue:
	"""
	A list-based implementation of the queue to utilize the list's append
	function for easier access of data
	"""
	def __init__(self):
		self.queue = []
		self.head = None

	def is_empty(self):
		if self.head:
			return False
		return True

	def peek(self):
		print( self.queue[0] )
		return self.queue[0]

	def enqeueue(self, node):
		self.queue.append(node)
		if self.is_empty():
			self.head = node

	def dequeue(self):
		current_head = None
		if self.head is None:
			print("Error, stack is empty!")
		else:
			current_head = self.queue.pop(0)
			self.head = self.queue[0]

		return current_head
	
class Vertex:
	def __init__(self, name, goal):
		self.name = name
		self.next = None
		self.successors = []
		self.is_visited = False
		self.goal = goal

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name

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

class Graph:
	"""
	Generates a graph, based on this tutorial:
	https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
	"""

	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, node, other):
		self.graph[node].append(other)

	def BFS(self, starting_vertex : Vertex):
		print("Starting BFS!")
		queue = []

		queue.append(starting_vertex)
		starting_vertex.visited()

		while queue:
			starting_vertex = queue.pop(0)
			print("Dequeuing: " + str(starting_vertex))

			if starting_vertex.goal:
				print("Goal reached: " + str(starting_vertex))
				break
			else:
				print("Goal state not reached, enqueuing successors...")
				
			for i in self.graph[starting_vertex]:
				if not i.has_visited():
					print("Enqueuing vertex: " + str(i))
					queue.append(i)
					i.visited()

	def DFS(self, starting_vertex: Vertex, depth_limit: int):
		print("Starting DFS!")
		stack = []

		stack.append(starting_vertex)

		while stack:
			starting_vertex = stack[-1]
			stack.pop()
			print("Popping: " + str(starting_vertex))

			if (starting_vertex.goal):
				print("Goal reached: " + str(starting_vertex))
				break

			if not starting_vertex.has_visited():
				print("Goal check failed on: " + str(starting_vertex))
				starting_vertex.visited()

			for vertex in self.graph[starting_vertex]:
				if not vertex.has_visited():
					stack.append(vertex)
					print("Appending vertex: " + str(vertex))

a = Vertex("A", False)
b = Vertex("B", False)
c = Vertex("C", False)
d = Vertex("D", False)
e = Vertex("E", True)

dfser = Graph()

dfser.add_edge(b, a)
dfser.add_edge(a, c)
dfser.add_edge(c, b)
dfser.add_edge(a, d)
dfser.add_edge(b, e)
print("===Depth-first Search===")
dfser.BFS(a)
print("\n========================")