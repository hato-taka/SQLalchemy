import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = "sample.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

query = "SELECT item_id, item_name, price FROM items WHERE item_name='おにぎり'"

cur.execute(query)
print(cur.fetchall())
print(cur.fetchone())
# print(cur.fetchmany(3))
conn.commit()
conn.close()