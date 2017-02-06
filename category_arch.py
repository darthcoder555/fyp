import category_helper as ch
neighbours = ch.parents
def shortest_path (cur_node, target_node):
	visited, queue = set(), [cur_node]
	parent = {}
	path = []
	marked = set()
	marked.add(cur_node)
	while queue:
		vertex = queue.pop(0)
		if vertex == target_node:
			break
	        if vertex not in visited:
        		visited.add(vertex)
			neigh = []
			neigh = neighbours (vertex)
			to_be_added = []
			for i in neigh:
				if i not in visited:
					to_be_added.append(i)
					parent[i] = vertex
        		queue.extend(to_be_added)
	this_node = target_node
	while 	this_node != cur_node:
		path.append (this_node)
		this_node = parent[this_node]
	path.append (this_node)
	path.reverse()
	return path
print shortest_path ('Physics','Nature')


		
