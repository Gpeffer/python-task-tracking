import sqlite3
import sys

con = sqlite3.connect('tasks.db')
cur = con.cursor()

# View all tasks
for row in (cur.execute('SELECT * FROM tasks')):
       row = [data.rstrip() for data in row]
       print(str(row))

# Close the connection
con.close()
