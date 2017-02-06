import MySQLdb;
db = MySQLdb.connect(host="localhost", user="root", passwd="rengarajan", db="fyp");
cur = db.cursor();

def neighbours(node):
	result = []
	result = result + parents(node)
	result = result + children(node)
	return(result)

def parents(node):
	result = []
	query = "SELECT page_id FROM page WHERE page_namespace=14 AND page_title LIKE \'" + node + "\';"
	cur.execute(query)
	cl_from = cur.fetchone()[0]
	query = "SELECT cl_to FROM categorylinks WHERE cl_from=" + str(cl_from) + ";"
	cur.execute(query)
	query_result = cur.fetchall()
	for i in query_result:
		result = result + [i[0]]
	return(result)

def children(node):
	result = []
	query = "SELECT cl_from FROM categorylinks WHERE cl_to LIKE \'" + node + "\' AND cl_type=\'subcat\';"
	cur.execute(query)
	query_result = cur.fetchall()
	for i in query_result:
		page_id = i[0]
		query = "SELECT page_title FROM page WHERE page_namespace=14 AND page_id=" + str(page_id) + ";"
		cur.execute(query)
		page_title = cur.fetchone()[0]
		result = result + [page_title]
	return(result)

def articles(node):
	result = []
	query = "SELECT cl_from FROM categorylinks WHERE cl_to LIKE \'" + node + "\' AND cl_type=\'page\';"
	cur.execute(query)
	query_result = cur.fetchall()
	for i in query_result:
		page_id = i[0]
		query = "SELECT page_title FROM page WHERE page_namespace=0 AND page_id=" + str(page_id) + ";"
		cur.execute(query)
		page_title = cur.fetchone()[0]
		result = result + [page_title]
	return(result)

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
        		visited.add(vertex)
			neigh = []
			neigh = neighbours (vertex)
			to_be_added = []
			for i in neigh:
				if i not in marked:
					count[i] = count[vertex] + 1;
					marked.add(i)
					to_be_added.append(i)
        		queue.extend(to_be_added)
		
	return visited








	

