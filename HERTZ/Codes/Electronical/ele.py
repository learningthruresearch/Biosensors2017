import numpy as np
import numpy as np 
import matplotlib as mp
import matplotlib.pyplot as plt
import csv

l0 = [[] for i in range(4)]
data = open('test.csv', 'r')
l1 = data.readline().strip().split(',')
for raw in data:
	raw = raw.strip().split(',')
	for i in range(len(raw)):
		l0[i].append(float(raw[i]))

fig = plt.figure(1, figsize=(9, 6))
ax = fig.add_subplot(111)
bp = ax.boxplot(l0, patch_artist=True)
## change outline color, fill color and linewidth of the boxes
for box in bp['boxes']:
    # change outline color
    box.set( color='#7570b3', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='#7570b3', linewidth=2)

## change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color='#7570b3', linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='#b2df8a', linewidth=2)

## change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5)

ax.set_xticklabels(l1)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.title('Results for 60 Hz')
plt.xlabel('Frequency emitted (Hz)')
plt.ylabel('Frequency registered (Hz)')
plt.show()