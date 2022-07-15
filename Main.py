from Graph import *
from Food import *

east_asian_dishes.shuffle()

start_vertex = Vertex("START", False)
vertices = [ [start_vertex] ]
# List down nodes
for cuisine, dishes in east_asian_dishes.food_list.items():
	dish_group = []
	for dish in dishes:
		dish_group.append(Vertex(dish, False))
	vertices.append(dish_group)
	pass

vertices.append( [Vertex("GOAL", True)] )
#print(vertices)
# Declare graph edges
graph = Graph()
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

# print(graph)

graph.DFS(start_vertex, 5)