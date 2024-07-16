import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
res = cur.execute("SELECT * FROM movie")
movies = res.fetchall()

