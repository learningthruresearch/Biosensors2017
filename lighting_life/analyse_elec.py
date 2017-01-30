import csv
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

import os, sys

# Open all file in a directory
path = sys.argv[1]
dirs = os.listdir(path)

for file in dirs:
	csvfile = open(path + '/' + file)
	fichier = csv.reader(csvfile, delimiter=' ')
	intens = 0
	a = 0

	for row in fichier:
		intens += int(row[0])
		a += 1
	intens_moy = intens / a 	

	f = open('data_elec.csv', 'rt')
	reader = csv.reader(f)
	save = []
	for row in reader:
		save.append(row)

	f = open('data_elec.csv', 'wt')
	writer = csv.writer(f)

	for i in save:
		writer.writerow(i)
	writer.writerow((path + '/' + file, intens_moy))
	f.close()