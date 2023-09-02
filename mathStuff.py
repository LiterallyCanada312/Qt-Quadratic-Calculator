# I didnt want to put this stuff in the main file since it doesnt look as neat lol
import math

def doQuadratic(a,b,c):
    discriminant = (b*b - (4*a*c))
    firstPossibility = (-b+math.sqrt(discriminant))/(2*a)
    secondPossibility = (-b-math.sqrt(discriminant))/(2*a)
    returns = []
    returns.append(firstPossibility)
    returns.append(secondPossibility)

    return returns


