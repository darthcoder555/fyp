import category_helper as ch
neighbours = ch.neighbours
'''def neighbours (st):
	if st == "A":
		return ['B','C']
	elif st == "B":
		return ['A', 'D', 'F']
	elif st == "C":
		return ['A', 'G']
	elif st == "D":
		return ['B', 'E', 'F']
	elif st == "E":
		return ['D', 'I', 'J']
	elif st == "F":
		return ['B', 'D', 'H']
	elif st == "G":
		return ['C', 'H']
	elif st == "H":
		return ['F', 'G', 'I']
	elif st == "I":
		return ['E', 'H', 'K']
	elif st == "J":
		return ['E', 'K']
	elif st == "K":
		return ['I', 'J']'''

def k_level_nodes (cur_node, k):
	visited, queue = set(), [cur_node]
	count = {}
	count[cur_node] = 0;
	marked = set()
	marked.add(cur_node)
	while queue:
		vertex = queue.pop(0)
		if count[vertex] > k:
			break
	        if vertex not in visited:
			print(vertex)
        		visited.add(vertex)
			neigh = []
			if(count[vertex] == k):
				continue
			neigh = neighbours(vertex)
			to_be_added = []
			for i in neigh:
				if i not in marked:
					print(i)
					count[i] = count[vertex] + 1;
					marked.add(i)
					to_be_added.append(i)
        		queue.extend(to_be_added)
		
	return visited


		
