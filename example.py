import os
from time import sleep

os.system('clear')

print(str('Welcome to your task-tracking application!'))
sleep(1)
os.system('clear')

print(str('\nHere is your list of things to do:\n'))


def strike(text):
    i = 0
    new_text = ''
    for i in range(len(text)):
        new_text += text[i] + u'\u0336'
    return(new_text)

for i in value:
    print(i)
