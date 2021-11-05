import os
import sqlite3

current = 0

con = sqlite3.connect('tasks.db')
cur = con.cursor()

cur.execute("create table if not exists tasks (id integer primary key autoincrement, done integer, description text)")

while True:
    values = []

    for v in cur.execute("select * from tasks"):
        values += [(v[0], bool(v[1]), v[2])]

    os.system("clear") # Clears the terminal

    for i in range(len(values)):
        v = values[i]

        if i == current:
            print("NEXT " + v[2])
        elif v[1]:
            print("DONE " + v[2])
        else:
            print("     " + v[2])

    print("\nOptions: (Q)uit, (N)ext, (A)dd, (D)one\n> ", end="")
    userInput = input().lower()

    # Quit if the user asks nicely
    if userInput == "q" or userInput == "quit":
        print("Bye!")
        break

    elif userInput == "a" or userInput == "add":
        os.system("clear")

        print("What task would you like to accomplish? ", end="")
        newTask = input()

        cur.execute("insert into tasks (done, description) values (0, '" + newTask + "')")
        con.commit()

    elif userInput == "d" or userInput == "done":
        cur.execute("update tasks set done = 1 where id = " + str(values[current][0]))
        con.commit()

        # Skip completed tasks
        while True:
            current += 1
            current %= len(values)

            if not values[current][1]:
                break;

    elif userInput == "n" or userInput == "next":
        # Skip completed tasks
        while True:
            current += 1
            current %= len(values)

            if not values[current][1]:
                break;

con.close()
