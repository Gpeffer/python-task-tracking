# imports
import os
# define functions

def mileage(c, p):
    d = c - p
    return d

def gphm(c, p, g):
    d = mileage(c, p)
    d /= 100
    m = g / d
    return m

def mpg(c, p, g):
    d = mileage(c, p)
    d /= g
    return d

# ask for input

os.system("clear")
c = input('\nEnter current mileage\n> ')
os.system("clear")
p = input('\nEnter previous mileage\n> ')
os.system("clear")
g = input('\nEnter gallons\n> ')
os.system("clear")

# convert input to floats

c = float(c)
p = float(p)
g = float(g)

# run floats through functions

a = mileage(c, p)
b = gphm(c, p, g)
d = mpg(c, p, g)

# convert results of functions to strings

a = str(a)
b = str(b)
d = str(d)

# print results

print(str('\nMiles traveled is "' + a + '".'))
print(str('\nGallons per hundred miles is "' + b + '".'))
print(str('\nMiles per gallon is "' + d + '".\n'))

input(str('Press enter to continue...'))

os.system("clear")
