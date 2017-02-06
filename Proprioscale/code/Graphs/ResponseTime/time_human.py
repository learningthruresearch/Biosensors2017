import numpy as np
import matplotlib.pyplot as plt
import csv
import pylab 

fichier = np.loadtxt("Human.csv", dtype="str", delimiter=',')

time = []
data = []
speed = [[] for i in range(5)]
speed_arduino = [[] for i in range(5)]
speed_arduinos = [[] for i in range(5)]

with open('Human.csv', 'rt') as csvfile:
        read = csv.reader(csvfile)
        for row in read:
	        path = row[1]
	        if '4' in path:
		        speed[0].append(float(row[3]))
                if '11' in path:
		        speed[0].append(float(row[3]))
                if '13' in path:
		        speed[0].append(float(row[3]))
                if '17' in path:
		        speed[0].append(float(row[3]))
                if '11' in path:
		        speed[0].append(float(row[3]))
	        if '20' in path:
		        speed[0].append(float(row[3]))
	        if '7' in path:
		        speed[1].append(float(row[3]))
	        if '14' in path:
		        speed[1].append(float(row[3]))
	        if '22' in path:
		        speed[1].append(float(row[3]))
	        if '23' in path:
		        speed[1].append(float(row[3]))
	        if '24' in path:
		        speed[1].append(float(row[3]))
	        if '1' in path:
		        speed[2].append(float(row[3]))
	        if '12' in path:
		        speed[2].append(float(row[3]))
	        if '16' in path:
		        speed[2].append(float(row[3]))
	        if '18' in path:
		        speed[2].append(float(row[3]))
	        if '19' in path:
		        speed[2].append(float(row[3]))
	        if '2' in path:
		        speed[3].append(float(row[3]))
	        if '5' in path:
		        speed[3].append(float(row[3]))
	        if '9' in path:
		        speed[3].append(float(row[3]))
	        if '10' in path:
		        speed[3].append(float(row[3]))
	        if '15' in path:
		        speed[3].append(float(row[3]))
	        if '3' in path:
		        speed[4].append(float(row[3]))
	        if '6' in path:
		        speed[4].append(float(row[3]))
	        if '8' in path:
		        speed[4].append(float(row[3]))
	        if '21' in path:
		        speed[4].append(float(row[3]))
	        if '25' in path:
		        speed[4].append(float(row[3]))

fig = plt.figure(1, figsize=(9,6))
ax = fig.add_subplot(111)
bpo = ax.boxplot(speed, patch_artist=True)
for box in bpo['boxes']:
    box.set( color='#7570b3', linewidth=2)
    box.set( facecolor = '#1b9e77' )
for whisker in bpo['whiskers']:
    whisker.set(color='#7570b3', linewidth=2)
for cap in bpo['caps']:
    cap.set(color='#000000', linewidth=2)
for median in bpo['medians']:
    median.set(color='#CC0000', linewidth=2)
for flier in bpo['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5)

BoxName = ['300', '500', '800', '1000', '1300']
pylab.xticks([1,2,3,4,5],BoxName)
plt.xlabel('weight (g)')
plt.ylabel('time response (s)')
plt.title('Time response according to the weight - Human sensors')
plt.savefig('timeresponses_human.png')
plt.show()
