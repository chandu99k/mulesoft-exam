import sqlite3
def create_db(db_name):
	'''function for creating databse'''
	db_name+=".db"
	f=open(db_name,'a')
	f.close()


def create_table():
	'''function for creating table with name movie_names'''
	db_name="Movies.db"
	try:
		conn=sqlite3.connect(db_name)
		cursor=conn.cursor()
		cursor.execute(
			'''
			create table if not exists movie_names(
			movie_name varchar(20),lead_actor varchar(20),actress varchar(20),year varchar(20),director varchar(20))
			''')
		conn.commit()
		return conn
	except sqlite3.Error as e:
		print(e)
def insert_data(conn,data):
	'''function to insert data into table'''
	cursor=conn.cursor()
	try:
		for item in data:
			cursor.execute("insert into movie_names values(?,?,?,?,?)",item)
		conn.commit()
	except sqlite3.Error as e:
		print(e)



if __name__=="__main__":
	create_db("Movies")
	conn=create_table()
	data=[('bachelor','GV-prakash','divya-barathi','2022','satish'),
	('dj-tillu','Sidhu','Neha-setty','2022','vimal-krishna')]
	insert_data(conn,data)
	
