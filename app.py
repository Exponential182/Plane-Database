import sqlite3

database = 'fighters.db'
db = sqlite3.connect(database)
cursor = db.cursor()
query = 'SELECT aircraft, climbrate FROM fighters WHERE climbrate > 100'
cursor.execute(query)
results = cursor.fetchall()
print(results)


db.close()

