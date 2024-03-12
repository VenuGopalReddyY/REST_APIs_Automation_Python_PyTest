import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', password='Sowrya@12345', database='APIDevelop')

print(connection.is_connected())

cursor = connection.cursor()

cursor.execute("select * from CustomerInfo")
print(cursor.fetchall())
list = cursor.fetchall()
sum = 0
for a in list:
    sum = sum + a[2]

print(sum)

query = "update CustomerInfo set Amount = %s where location = %s"
data = (100, "Africa")
cursor.execute(query, data)
connection.commit()



connection.close()
