import csv
import numpy as np
import matplotlib.pyplot as plt
import pylab

f = open('data.csv', 'rt')
reader = csv.reader(f)
speed = [[] for i in range(5)]

for row in reader:
	path = row[0].split('/')
	if path[1] == 'Lum0':
		speed[0].append(float(row[1])/400)
	if path[1] == 'Lum1':
		speed[1].append(float(row[1])/400)
	if path[1] == 'Lum10':
		speed[2].append(float(row[1])/400)
	if path[1] == 'Lum100':
		speed[3].append(float(row[1])/400)
	if path[1] == 'Lum255':
		speed[4].append(float(row[1])/400)

box_leg = ['0', '1', '10', '100', '255']
plt.boxplot(speed)
pylab.xticks([1,2,3,4,5], box_leg)

plt.xlabel('Intensity (arbitrary unit)')
plt.ylabel('speed (mm.s-1)')
plt.title('Speed averadge of tardigrades in fonction of green light')
plt.savefig('1graph.png')
plt.show()

f.close()