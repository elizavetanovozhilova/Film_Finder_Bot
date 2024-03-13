import sqlite3

conn = sqlite3.connect("mydata.db")

sql = ("CREATE TABLE films ("
       "name TEXT, "
       "genres TEXT, "
       "actors TEXT, "
       "directors TEXT, "
       "year INTEGER, "
       "description TEXT, "
       "countries TEXT, "
       "movie_link TEXT, "
       "img_link TEXT, "
       "age_restrictions INTEGER)")

sql = "SELECT * FROM films"

cursor = conn.cursor()

cursor.execute(sql)

res = cursor.fetchall()

for r in res:
    print("Name:", r[0])
    print("Actors:", r[2])
conn.close()
