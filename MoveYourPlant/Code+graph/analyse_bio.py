import csv
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pylab

csvfile = open('data_lentils.csv')
fichier = csv.reader(csvfile, delimiter=',')

speed_box1 = []
speed_box2 = []
speed_box3 = []
speed_box4 = []
speed_box5 = []
speed_box6 = []

poids_box1 = []
poids_box2 = []
poids_box3 = []
poids_box4 = []
poids_box5 = []
poids_box6 = []

rapport_box1 = []
rapport_box2 = []
rapport_box3 = []
rapport_box4 = []
rapport_box5 = []
rapport_box6 = []

for row in fichier:
	if row[0] == '1':
		if float(row[-2]) > 0:
			lenth_avant = float(row[5])
			lenth_apres = float(row[7])
			poids_avant = float(row[4])
			poids_apres = float(row[6])
			if lenth_avant == -1:
				lenth_avant = 0
			if row[1] == '1':
				speed = (lenth_apres - lenth_avant) / 45
				speed_box1.append(speed)
				poids = (poids_apres - poids_avant)
				poids_box1.append(poids)
				rapport = (lenth_apres / poids_apres) - (lenth_avant / poids_avant)
				rapport_box1.append(rapport)
			if row[1] == '2':
				speed = (lenth_apres - lenth_avant) / 45
				speed_box2.append(speed)
				poids = (poids_apres - poids_avant)
				poids_box2.append(poids)
				rapport = (lenth_apres / poids_apres) - (lenth_avant / poids_avant)
				rapport_box2.append(rapport)
			if row[1] == '3':
				speed = (lenth_apres - lenth_avant) / 45
				speed_box3.append(speed)
				poids = (poids_apres - poids_avant)
				poids_box3.append(poids)
				rapport = (lenth_apres / poids_apres) - (lenth_avant / poids_avant)
				rapport_box3.append(rapport)
			if row[1] == '4':
				speed = (lenth_apres - lenth_avant) / 45
				speed_box4.append(speed)
				poids = (poids_apres - poids_avant)
				poids_box4.append(poids)
				rapport = (lenth_apres / poids_apres) - (lenth_avant / poids_avant)
				rapport_box4.append(rapport)
			if row[1] == '5':
				speed = (lenth_apres - lenth_avant) / 45
				speed_box5.append(speed)
				poids = (poids_apres - poids_avant)
				poids_box5.append(poids)
				rapport = (lenth_apres / poids_apres) - (lenth_avant / poids_avant)
				rapport_box5.append(rapport)
			if row[1] == '6':
				speed = (lenth_apres - lenth_avant) / 45
				speed_box6.append(speed)
				poids = (poids_apres - poids_avant)
				poids_box6.append(poids)
				rapport = (lenth_apres / poids_apres) - (lenth_avant / poids_avant)
				rapport_box6.append(rapport)

plt.boxplot([speed_box1, speed_box2, speed_box3, speed_box4, speed_box5, speed_box6])
box_leg = ['4978', '3520', '1661', '31', '0 (1)', '0 (2)']
pylab.xticks([1,2,3,4,5,6], box_leg)
plt.xlabel('Frequence (Hz)')
plt.ylabel('Growth speed (mm/h)')
plt.title('Speed growth of lentils as a fonction of frequencies exposure')
plt.savefig('graph_bio_1_rep2.png')
plt.show()

plt.boxplot([poids_box1, poids_box2, poids_box3, poids_box4, poids_box5, poids_box6])
box_leg = ['4978', '3520', '1661', '31', '0 (1)', '0 (2)']
pylab.xticks([1,2,3,4,5,6], box_leg)
plt.xlabel('Frequence (Hz)')
plt.ylabel('Weight (cg)')
plt.title('weight of lentils as a fonction of frequencies exposure')
plt.savefig('graph_bio_2_rep2.png')
plt.show()

plt.boxplot([rapport_box1, rapport_box2, rapport_box3, rapport_box4, rapport_box5, rapport_box6])
box_leg = ['4978', '3520', '1661', '31', '0 (1)', '0 (2)']
pylab.xticks([1,2,3,4,5,6], box_leg)
plt.xlabel('Frequence (Hz)')
plt.title('Speed growth / weight of lentils as a fonction of frequencies exposure')
plt.savefig('graph_bio_3_rep2.png')
plt.show()

moyenne = []
moyenne.append(float(sum(speed_box1)) / len(speed_box1))
moyenne.append(float(sum(speed_box2)) / len(speed_box2))
moyenne.append(float(sum(speed_box3)) / len(speed_box3))
moyenne.append(float(sum(speed_box4)) / len(speed_box4))
moyenne.append(float(sum(speed_box5)) / len(speed_box5))
moyenne.append(float(sum(speed_box6)) / len(speed_box6))

print(moyenne)