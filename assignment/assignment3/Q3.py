#
import MySQLdb
# conn = MySQLdb.connect(host = "localhost", user = "testdb", passwd = "1234", db = "ashuj" )
# cursor = conn.cursor()
# cursor.execute("select * from actor")
#
# data  = cursor.fetchall()
#
# for i in data :
# 	print i
#
# conn.close()

import MySQLdb as mdb
import sys


# create a new table and insert some values
def createTable(con):
	with con:
		
		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS TableTest")
		cur.execute("CREATE TABLE TableTest(Id INT PRIMARY KEY AUTO_INCREMENT, \
                     Name VARCHAR(25))")
		cur.execute("INSERT INTO TableTest(Name) VALUES('Bhai')")
		cur.execute("INSERT INTO TableTest(Name) Values ('Tazo')")
		cur.execute("INSERT INTO TableTest(Name) Values ('raja')")
		cur.execute("INSERT INTO TableTest(Name) Values ('Abhi')")
		cur.execute("INSERT INTO TableTest(Name) Values ('Ashu')")
		
# Retrieve table rows
def retrieveTable(con):
	with con:
		cur  = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT * FROM TableTest")
		
		rows  = cur.fetchall()
		
		for row in rows :
			print row ["Id"], row ["Name"]
			
		
		
# Update ROW
def updateRow(con):
	with con:
		
		cur = con.cursor()
		cur.execute("UPDATE TableTest SET Name  = %s WHERE Id  = %s", ("None Acaso", "4"))
		print "Nuber of rows updated:", cur.rowcount

# DELETE ROW
def deleteRow(con):
	with con:
		cur = con.cursor()
		cur.execute("DELETE FROM TableTest WHERE Id = %s", "2")
		print "Nuber of rows deleted:", cur.rowcount
		
		
# SET UP THE CONNECTION
try:
	con = mdb.connect(host = "localhost", user = "testdb", passwd = "1234", db = "ashuj")
	
	cur = con.cursor()
	cur.execute("SELECT VERSION()")
	ver = cur.fetchone()
	print "Database version : %s" % ver
	
	
	# CRUD OPERATIONS
	createTable(con)
	retrieveTable(con)
	updateRow(con)
	deleteRow(con)
	
except mdb.Error, e:
	print "Error, %d: %s" % (e.args[0],e.args[1])
	sys.exit(1)

finally:
	
	if con:
		con.close()
		