import sqlite3
import random
from aiogram.types import URLInputFile

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

'''
for r in res:
    print("Name:", r[0])
    print("links img:", r[8])
    
'''

def random_film():
       num=random.randint(0, len(res))
       img = URLInputFile(f'{res[num][8]}')
       return f'Советую посмотреть этот фильм!\n\n<b>{res[num][0]}</b>, {res[num][4]}\n\n<i>{res[num][1]}</i>\n\n{res[num][5]}', img

def learn_about_film(message):
       for r in res:
              if r[0].lower()==message.lower():
                     return f'<b>{r[0]}</b>, {r[4]}\n\n<i>{r[1]}</i>\n\n{r[5]}', URLInputFile(f'{r[8]}')
              elif message.lower() in r[0].lower():
                     return f'Возможно вы имели в виду этот фильм:\n\n<b>{r[0]}</b>, {r[4]}\n\n<i>{r[1]}</i>\n\n{r[5]}', URLInputFile(f'{r[8]}')



conn.close()
