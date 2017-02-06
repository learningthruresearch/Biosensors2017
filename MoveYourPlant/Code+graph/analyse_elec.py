import csv
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pylab

# Open all file in a directory
dirs = os.listdir("data_elec")

data = []

for file in dirs:
	fichier = np.loadtxt("data_elec/" + file, dtype="str", delimiter=',')
	for content in fichier:
		data.append(content[2:-1].split(' '))
F0 = []
F1 = []
F2 = []
F3 = []
F4 = []

for row in data:
	if row[0][1] == '0':
		F0.append(float(row[1])*1000)
	if row[0][1] == '1':
		F1.append(float(row[1])*1000)
	if row[0][1] == '2':
		if float(row[1]) > 1:
			F2.append(float(row[1])*1000)
	if row[0][1] == '3':
		F3.append(float(row[1])*1000)
	if row[0][1] == '4':
		F4.append(float(row[1])*1000)

plt.boxplot([F4, F3, F2, F1, F0])
box_leg = ['4978', '3520', '1661', '31', '0']
pylab.xticks([1,2,3,4,5], box_leg)
plt.xlabel('Frequency emitted (Hz)')
plt.ylabel('Frequency perceived (Hz)')
plt.title('Frequency perceived by the micro as a fonction of the emetted frequency')
plt.savefig('graph_elec.png')
plt.show()

plt.plot([F4, F3, F2, F1, F0], box_leg)
box_leg = ['4978', '3520', '1661', '31', '0']
#pylab.xticks([1,2,3,4,5], box_leg)
plt.xlabel('Frequency emitted (Hz)')
plt.ylabel('Frequency perceived (Hz)')
plt.title('Frequency perceived by the micro as a fonction of the emetted frequency')
plt.savefig('graph_elec.png')
plt.show()

