import mysql.connector as sql


connection  = sql.connect(
     host = "localhost",
     user='root',
     password='test1234',
     database =  "accounts"

     )
cursor = connection.cursor()
addData = ('INSERT INTO account_info ( name, email, pin,balence) VALUES ("test","teste",11111111,0)')
cursor.execute(addData)
connection.commit()
fetch = ("SELECT * FROM account_info")
cursor.execute(fetch)
