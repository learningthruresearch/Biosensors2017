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
	fichier = csv.reader(csvfile, delimiter=',')

	distance_pate_tot = 0
	distance_tete_tot = 0

	a = 0 
	b = 0 
	print(file)
	for row in fichier:
		if row[2] != '1' and row[0] != ' ':
			if float(row[1]) == 1.:
				distance_pate_tot += float(row[5])
				a += 1
			if float(row[1]) == 2.:
				distance_tete_tot += float(row[5])
				b += 1
	speed_pate = distance_pate_tot / a
	speed_tete = distance_tete_tot / b

	speed = (speed_pate + speed_tete) / 2

	f = open('data_bio.csv', 'rt')
	reader = csv.reader(f)
	save = []
	for row in reader:
		save.append(row)

	f = open('data_bio.csv', 'wt')
	writer = csv.writer(f)

	for i in save:
		writer.writerow(i)
	writer.writerow((path + file, speed))
	f.close()
