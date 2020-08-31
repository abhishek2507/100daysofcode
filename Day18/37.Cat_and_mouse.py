'''
The question can be found at:
https://www.hackerrank.com/challenges/cats-and-a-mouse/
'''

def catAndMouse(x, y, z):
    if abs(z-y) > abs(z-x):
        return("Cat A")
    elif abs(z-y) <abs(z-x):
        return("Cat B")
    else:
        return("Mouse C")