import sys
import os

f = open("/home/garrypeffer/Python/task-tracking.md", "r")
print(f.read())

print(str('\nOptions: (e)ntry, (f)inish, (q)uit'))

action = input("Enter option: \n\n")


if action == str('e') or action == str('entry'):
    entry = input("Enter entry: \n")
    f = open("/home/garrypeffer/Python/task-tracking.md", "a")
    f.write("\n" + (entry) + "\n")
    f.close()
    
if action == str('f') or action == str('finish'):
if action == str('q') or action == str('quit'):
    print(str('Have a nice day!'))
    break
