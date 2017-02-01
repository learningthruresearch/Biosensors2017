import csv
import numpy as np
import matplotlib.pyplot as plt
import pylab

f = open('data_elec.csv', 'rt')
reader = csv.reader(f)
intens = [[] for i in range(5)]

for row in reader:
	path = row[0].split('/')
	if path[3] == 'Lum0':
		intens[0].append(float(row[1]))
	if path[3] == 'Lum1':
		intens[1].append(float(row[1]))
	if path[3] == 'Lum10':
		intens[2].append(float(row[1]))
	if path[3] == 'Lum100':
		intens[3].append(float(row[1]))
	if path[3] == 'Lum255':
		intens[4].append(float(row[1]))

box_leg = ['0', '1', '10', '100', '255']
plt.boxplot(intens)
pylab.xticks([1,2,3,4,5], box_leg)

plt.xlabel('Intensity (arbitrary unit)')
plt.ylabel('Intensity (arbitrary unit)')
plt.title('Light intensity receved in fonction of the light intensity ')
plt.savefig('2graph.png')
plt.show()

f.close()