import sys
from os import system, name
from time import sleep

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()

# Opening message
print(str('\nWelcome to your daily dose of organization!\n'))

sleep(1)

# Python3 code to iterate over a list
list = [str('Walk the dog'), str('Wash the dishes'), str('Clean the garage'), str('Do the laundry'), str('Cook dinner')]

# Using enumerate()
for i, val in enumerate(list):
    print (i, ",", val)

# List out options for user input
option = input(str('\nOptions:\n(n)ext, (d)one, (q)uit\n\n'))

# Begin list of conditionals based on result of user input
for i in list:
    print(i[0], i[1], i[2])

list.close()
