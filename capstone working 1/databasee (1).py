import pymysql

conn=pymysql.connect(host="localhost", user="root", passwd= "", db="my_python")

myCursor= conn.cursor()

myCursor.execute("insert into delhi values('hello')")

conn.commit()

conn.close()

