import numpy as np
import numpy as np 
import matplotlib as mp
import matplotlib.pyplot as plt
import csv

l0 = [[] for i in range(15)]
l1 = []

data = open('data-electro.csv', 'r')
l00 = data.readline().strip().split(',')
for i in l00:
	l1.append(int(i))
for raw in data:
	raw = raw.strip().split(',')
	for i in range(len(raw)):
		l0[i].append(float(raw[i]))

l01 = l0[0:5]
l11 = l1[0:5]
l02 = l0[5:10]
l12 = l1[5:10]
l03 = l0[10:15]
l13 = l1[10:15]

fig = plt.figure(1, figsize=(9, 6))
ax = fig.add_subplot(111)
bp = ax.boxplot(l01, positions = l11, patch_artist=True)
lp = ax.plot(range(55, 85), range(55, 85), label = 'x=y')
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.set_ylim([55,85])
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_title('Results for 60 Hz') 
ax.set_xlabel('Frequency emitted (Hz)')
ax.set_ylabel('Frequency registered (Hz)')
ax.legend()

## change outline color, fill color and linewidth of the boxes
for box in bp['boxes']:
    # change outline color
    box.set( color= 'red', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='red', linewidth=2)

## change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color='red', linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='red', linewidth=2)

## change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker='o', color='red', alpha=0.5)



fig1 = plt.figure(2, figsize=(9, 6))
ax1 = fig1.add_subplot(111)
bp1 = ax1.boxplot(l02, positions = l12, patch_artist=True)
lp1 = ax1.plot(range(245, 275), range(245, 275), label = 'x=y')
ax1.get_xaxis().tick_bottom()
ax1.get_yaxis().tick_left()
ax1.set_ylim([245,275])
ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax1.set_title('Results for 250 Hz')
ax1.set_xlabel('Frequency emitted (Hz)')
ax1.set_ylabel('Frequency registered (Hz)')
ax1.legend()

## change outline color, fill color and linewidth of the boxes
for box in bp1['boxes']:
    # change outline color
    box.set( color='r', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
for whisker in bp1['whiskers']:
    whisker.set(color='r', linewidth=2)

## change color and linewidth of the caps
for cap in bp1['caps']:
    cap.set(color='r', linewidth=2)

## change color and linewidth of the medians
for median in bp1['medians']:
    median.set(color='r', linewidth=2)

## change the style of fliers and their fill
for flier in bp1['fliers']:
    flier.set(marker='o', color='r', alpha=0.5)



fig2 = plt.figure(3, figsize=(9, 6))
ax2 = fig2.add_subplot(111)
bp2 = ax2.boxplot(l03, positions = l13, patch_artist=True)
lp2 = ax2.plot(range(1995, 2025), range(1995, 2025), label = 'x=y')
ax2.get_xaxis().tick_bottom()
ax2.get_yaxis().tick_left()
ax2.set_ylim([1995,2025])
ax2.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax2.set_title('Results for 2000 Hz')
ax2.set_xlabel('Frequency emitted (Hz)')
ax2.set_ylabel('Frequency registered (Hz)') 
ax2.legend()

## change outline color, fill color and linewidth of the boxes
for box in bp2['boxes']:
    # change outline color
    box.set( color='r', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
for whisker in bp2['whiskers']:
    whisker.set(color='r', linewidth=2)

## change color and linewidth of the caps
for cap in bp2['caps']:
    cap.set(color='r', linewidth=2)

## change color and linewidth of the medians
for median in bp2['medians']:
    median.set(color='r', linewidth=2)

## change the style of fliers and their fill
for flier in bp2['fliers']:
    flier.set(marker='o', color='r', alpha=0.5)


fig.savefig('electronic_60Hz.png')
fig1.savefig('electronic_250Hz.png')
fig2.savefig('electronic_2000Hz.png')
