import matplotlib.pyplot as plt

aweight = [0.14, 0.19, 0.22] #average weights
atimes = [51.5, 52.3, 55.9] #average reaction times for the piezo element
weight = [0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.19, 0.19, 0.19, 0.19, 0.19, 0.19, 0.19, 0.19, 0.19, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22] #weights dropped on sensor
times = [72.66666667, 60.13333333, 37.33333333, 73.2, 56.26666667, 36.4, 45.33333333, 46.26666667, 35.6, 65.33333333, 23.73333333, 66.93333333, 13.46666667, 58.13333333, 81.06666667, 44.93333333, 64.13333333, 53.2, 37.33333333, 48.66666667, 63.33333333, 72.4, 33.06666667, 68.8, 29.33333333, 84.53333333, 65.86666667] #different reaction times
reac = [1433.333333, 1066.666667, 533.3333333, 733.3333333, 733.3333333, 900, 1400, 566.6666667, 2333.333333, 133.3333333, 4516.666667, 683.3333333, 433.3333333, 416.6666667, 600, 433.3333333, 533.3333333, 600, 966.6666667, 3366.666667, 716.6666667, 2483.333333, 750, 9133.333333, 1183.333333, 783.3333333, 1566.666667] #plant reaction times
areac = [1077.777778, 927.7777778, 2327.777778] #plant average reaction times for different weights

plt.subplot(211) #plot for sensor
plt.scatter(weight, times)
plt.scatter(aweight, atimes, s = 65, color = 'red')
plt.title('Piezo element sensor reaction time accroding to weight of stimulus', fontsize = '20')
plt.xlabel('weight of stimulus(in g)', fontsize = '20')
plt.ylabel('reaction time(in ms)', fontsize = '20')
plt.subplot(212) #plot for plants
plt.scatter(aweight, areac, s = 65, color = 'red')
plt.scatter(weight, reac)
plt.title('Dionea reaction time according to stimulus weight', fontsize = '20')
plt.ylabel('reaction time(in ms)', fontsize = '20')
plt.xlabel('weight of stimulus(in g)', fontsize = '20')
plt.show()
