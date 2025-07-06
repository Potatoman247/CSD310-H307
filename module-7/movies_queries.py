import mysql.connector # to connect
from mysql.connector import errorcode

db = mysql.connector.connect(host='localhost', user='root',password='June092021?!', database='movies')

cursor = db.cursor()

print("-- DISPLAYING Studio RECORDS --")
cursor.execute("SELECT * FROM STUDIO")
studios = cursor.fetchall()
for studio in studios:
    print("Studio ID: {0}\n Studio Name: {1}\n".format(*studio))
    
print("-- DISPLAYING Genre RECORDS --")
cursor.execute("SELECT * FROM GENRE")
genres = cursor.fetchall()
for genre in genres:
    print("Genre ID: {0}\n Genre Name: {1}\n".format(*genre))

print("-- DISPLAYING Short Film RECORDS --")

cursor.execute("SELECT FILM_NAME, FILM_RUNTIME FROM FILM WHERE FILM_RUNTIME < 120")
films = cursor.fetchall()
for film in films:
    print("Film Name: {0}, Film Runtime: {1}\n".format(*film))

print("-- DISPLAYING Director RECORDS In Order --")

cursor.execute("SELECT FILM_NAME, FILM_DIRECTOR FROM FILM ORDER BY FILM_DIRECTOR")
films = cursor.fetchall()
for film in films:
    print("Film Name: {0}\n Director Name: {1}\n".format(*film))