# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	port = '3306',
	passwd = 'Monboli1309@@'

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE cmln")

print("All Done!")
