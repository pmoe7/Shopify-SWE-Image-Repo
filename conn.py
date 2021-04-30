import mysql.connector
host='localhost'
db = 'shopify'
user = 'root'
password = ''

connection = mysql.connector.connect(host=host, database=db, user=user, password=password)