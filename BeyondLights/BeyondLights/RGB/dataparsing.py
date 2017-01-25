#from math import *
#import numpy as np
#import matplotlib.pyplot as plt

file = open("data2min.csv", 'r')
listeR = []
listeG = []
listeB = []

for line in file.readlines():
    a = line.split('  ')
    del a[-1]
    print(a)
    listeR.append(a[-3])
    listeG.append(a[-2])
    listeB.append(a[-1])
print(listeR)
print(listeG)
print(listeB)



