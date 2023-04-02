import sqlite3
import os
import csv

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

os.chdir("C:\Code\DataSets\Anime")
cwd = os.getcwd()

db = sqlite3.connect("AnimeShowData.db")
db.row_factory = dict_factory

cur = db.cursor()

title = input("Input Title: ").strip().upper()
print(f"User Input Title is {title}")

result = cur.execute("SELECT * FROM AnimeShowData WHERE UPPER(studios) LIKE ?", (title,))

print(result.fetchone().keys())
for row in result.fetchall():
    print(row["Title"])


cur.close()
db.close()