import matplotlib.pyplot as plt
import numpy as np

N = 6
index = np.arange(N)
barWidth = 0.2

nucleus = [[[1, 42], [2, 82], [37, 102], [75, 139], [53, 138], [16, 83]], 
[[2, 54], [2, 68], [43, 61], [68, 102], [67, 98], [29, 101]], 
[[1, 53], [1, 36], [52, 63], [27, 49], [7, 31], [8, 48]]]

raw = [[], [], []]

for i in range(len(nucleus)):
	for j in nucleus[i]:
		raw[i].append((j[0] / j[1]) *100)

r1 = range(N)
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]


plt.bar(r1, raw[0], color = 'black', width = barWidth)
plt.bar(r2, raw[1], color = 'green', width = barWidth)
plt.bar(r3, raw[2], color = 'lightgreen', width = barWidth)


plt.xticks(index + 0.4 ,('0', '20', '100', '150', '200', '300'))
plt.legend(['> 3 days old','~ 1.5 days old','~ 1 day old'], loc='upper right',prop={'size':15})
plt.xlabel('Glucose concentration (g/L)')
plt.ylabel('% of cells with fluorecsence in nucleus')
plt.savefig('graph3.png')
plt.grid()
plt.show()