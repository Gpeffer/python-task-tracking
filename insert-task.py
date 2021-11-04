import sqlite3
import sys

sys.argv[1]
con = sqlite3.connect('tasks.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE if not exists "tasks"
                (tasks)''')

# Insert a row of data
cur.execute("INSERT INTO tasks (tasks) VALUES " + "('" + str(sys.argv[1]) + "')")

# Save (commit) the changes
con.commit()

# Close the connection
con.close()
