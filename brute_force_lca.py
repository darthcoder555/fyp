from category_helper import parents
from category_helper import children
red_colored_nodes = {}

'''def parent (node):
	l = []	
	if node == "A":
		return l
	elif node == "B":
		l.append ("A")
	elif node == "C":
		l.append ("A")
	elif node == "D":
		l.append("B")
	elif node == "E":
		l.append("B")
	elif node == "F":
		l.append("C")
		l.append ("B")
	elif node == "G":
		l.append("C")
#		l.append ("E")
	elif node == "H":
		l.append ("D")
		#l.append ("E")
	elif node ==  "I":
		l.append ("E")
	elif node == "J":
		l.append ("F")
		l.append ("G")
	elif node == "K":
		l.append ("G")
	return l

def children (node):
	l = []	
	if node == "H":
		return l
	if node == "I":
		return l
	if node == "J":
		return l
	if node == "K":
		return l
	elif node == "B":
		l.append ("D")
		l.append ("E")
		l.append ("F")
	elif node == "C":
		l.append ("F")
		l.append ("G")
	elif node == "D":
		l.append("H")
	elif node == "E":
		l.append("H")
		l.append ("I")
	elif node == "F":
		l.append("J")
	elif node == "G":
		l.append("J")
		l.append ("K")
	return l '''

def brute_force_lca (source, root_node):
	queue = [source]	
	while True:
		vertex = queue.pop(0)
		if vertex == root_node:
			red_colored_nodes[vertex] = 1
			break
		if vertex != source:
			red_colored_nodes[vertex] = 1
		parents_set = parents (vertex)
		queue.extend (parents_set)
	while queue:
		vertex = queue.pop(0)
		red_colored_nodes[vertex] = 1

def find_lca (destination):
	queue = [destination]
	while True:
		vertex = queue.pop(0)
		x = red_colored_nodes.get (vertex, None)
		if x != None:
			return vertex
		parents_set = parents(vertex)
		queue.extend (parents_set)

def path (source, destination, flag):
	queue = [source]

	prev = {}
	path = []

	while True :
		vertex = queue.pop(0)	
		#print vertex
		if vertex == destination:
			break;
		parents_set = parents (vertex)
		queue.extend (parents_set)
		for i in parents:
			prev[i] = vertex
		
	path.append (destination)
	pre = prev[destination]
	while pre != source:
		
		path.append (pre)
		pre = prev[pre]			
		c = 1
	path.append (source)				
	return path	

#Source and Destination values

source = "Physics"
destination = "Chemistry"	
brute_force_lca (source, "Contents")
LCA = find_lca (destination)

print LCA

path1 = path (source, LCA, 1)

#print path1
path2 = []
if destination == LCA:
	path2.append (LCA)
else:
	path2 = path (destination, LCA, 1)

#print path2

path_ans = []

for i in range (len(path1) - 1, -1, -1):
	path_ans.append (path1[i])

for i in range (1, len(path2)):
	path_ans.append (path2[i])

print path_ans







		

		
