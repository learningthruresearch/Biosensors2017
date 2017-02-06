import numpy as np
import matplotlib.pyplot as plt
import csv
import pylab 

time = []
data = []
speed = [[] for i in range(5)]

with open('replica_humain.csv', 'rt') as csvfile:
        read = csv.reader(csvfile)
        for row in read:
	        path = row[0]
	        if '300' in path:
		        speed[0].append(float(row[1]))
                if '500' in path:
		        speed[1].append(float(row[1]))
                if '800' in path:
		        speed[2].append(float(row[1]))
                if '1000' in path:
		        speed[3].append(float(row[1]))
                if '1300' in path:
		        speed[4].append(float(row[1]))

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
plt.ylabel('Average time response (s)')
plt.title('Time response according to the weight - Human sensors replica')
plt.savefig('timeresponses_human_replica.png')
plt.show()
