import MySQLdb;
db = MySQLdb.connect(host="localhost", user="root", passwd="rengarajan", db="fyp");
cur = db.cursor();

def commonImage(target):
	result = []
	query = "SELECT page_id FROM page WHERE page_namespace=0 AND page_title LIKE \'" + target + "\';"
	cur.execute(query)
	il_from=cur.fetchone()[0]
	query = "SELECT il_to FROM imagelinks WHERE il_from=" + str(il_from) + ";"
	cur.execute(query)
	query_result = cur.fetchall()
	for i in query_result:
		il_to = i[0]
		if(il_to == 'Flag_of_India.svg' or il_to == 'PD-icon.svg'):
			continue
		query = "SELECT il_from FROM imagelinks WHERE il_from_namespace=0 AND il_to LIKE \'" + il_to + "\';"
		cur.execute(query)
		query_result2 = cur.fetchall()
		for j in query_result2:
			page_id = j[0]
			query = "SELECT page_title FROM page WHERE page_id=" + str(page_id) + ";"
			cur.execute(query)
			page_title = cur.fetchone()[0]
			result = result + [page_title]
	return(result)

print(commonImage('Public_holidays_in_India'))
