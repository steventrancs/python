import mysql.connector
from mysql.connector import errorcode

def input_config():
	host    = raw_input("Host: ")
	usrName = raw_input("user: ")
	passWrd = raw_input("pass: ")
	dbName  = raw_input("database: ")

	return (host, usrName, passWrd, dbName)

def connect_database():
	cfg = input_config()
	try:
		cnx = mysql.connector.connect(user=cfg[1], password=cfg[2], host=cfg[0],
																database=cfg[3])
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Username or password incorrect!")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	else:
		cnx.close()

connect_database()