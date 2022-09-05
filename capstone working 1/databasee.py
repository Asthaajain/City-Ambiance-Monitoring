import pymysql

conn=pymysql.connect(host="localhost", user="root", passwd= "", db="my_python")

myCursor= conn.cursor()

myCursor.execute("insert into delhi values('hello')")

print(myCursor.fetchall(),end="\n ")

conn.commit()

conn.close()

