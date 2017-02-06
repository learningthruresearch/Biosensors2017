import numpy as np
import matplotlib.pyplot as plt
import csv
import pylab 

speed_arduino = [[] for i in range(5)]
speed_arduinos = [[] for i in range(5)]


with open('arduino.csv', 'rt') as csvfile:
        reader = csv.reader(csvfile)
	for row in reader:
	        path = row[0]
	        if '4' in path:
		        speed_arduino[0].append(float(row[1]))
                if '11' in path:
		        speed_arduino[0].append(float(row[1]))
                if '13' in path:
		        speed_arduino[0].append(float(row[1]))
                if '17' in path:
		        speed_arduino[0].append(float(row[1]))
                if '11' in path:
		        speed_arduino[0].append(float(row[1]))
	        if '20' in path:
		        speed_arduino[0].append(float(row[1]))
	        if '7' in path:
		        speed_arduino[1].append(float(row[1]))
	        if '14' in path:
		        speed_arduino[1].append(float(row[1]))
	        if '22' in path:
		        speed_arduino[1].append(float(row[1]))
	        if '23' in path:
		        speed_arduino[1].append(float(row[1]))
	        if '24' in path:
		        speed_arduino[1].append(float(row[1]))
	        if '1' in path:
		        speed_arduino[2].append(float(row[1]))
	        if '12' in path:
		        speed_arduino[2].append(float(row[1]))
	        if '16' in path:
		        speed_arduino[2].append(float(row[1]))
	        if '18' in path:
		        speed_arduino[2].append(float(row[1]))
	        if '19' in path:
		        speed_arduino[2].append(float(row[1]))
	        if '2' in path:
		        speed_arduino[3].append(float(row[1]))
	        if '5' in path:
		        speed_arduino[3].append(float(row[1]))
	        if '9' in path:
		        speed_arduino[3].append(float(row[1]))
	        if '10' in path:
		        speed_arduino[3].append(float(row[1]))
	        if '15' in path:
		        speed_arduino[3].append(float(row[1]))
	        if '3' in path:
		        speed_arduino[4].append(float(row[1]))
	        if '6' in path:
		        speed_arduino[4].append(float(row[1]))
	        if '8' in path:
		        speed_arduino[4].append(float(row[1]))
	        if '21' in path:
		        speed_arduino[4].append(float(row[1]))
	        if '25' in path:
		        speed_arduino[4].append(float(row[1]))
print(speed_arduino)
for temps in range(len(speed_arduino)):
     speed_arduinos[0].append(int(speed_arduino[temps][0])*10**-3)
     speed_arduinos[1].append(int(speed_arduino[temps][1])*10**-3)
     speed_arduinos[2].append(int(speed_arduino[temps][2])*10**-3)
     speed_arduinos[3].append(int(speed_arduino[temps][3])*10**-3)
     speed_arduinos[4].append(int(speed_arduino[temps][4])*10**-3)
print(speed_arduinos)

fig = plt.figure(1, figsize=(9,6))
ax = fig.add_subplot(111)
bpo = ax.boxplot(speed_arduinos, patch_artist=True)

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
plt.title('Time response according to the weight - Arduino')
plt.savefig('timeresponses_arduino.png')
plt.show()
