import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import csv

time_human = []
data_human = []
time_human_replica = []
data_human_replica = []
time_arduino = []
data_arduino = []
times = ''
match = {'1' :'800', '2' :'1000', '3' :'1300', '4':'300', '5':'1000','6':'1300','7':'500', '8':'1300', '9':'1000', '10':'1000', '11':'300', '12':'800', '13':'300', '14':'500', '15':'1000', '16':'800', '17':'300', '18':'800', '19':'800', '20':'300', '21':'1300', '22':'500', '23':'500', '24':'500', '25':'1300'}
fichier_human = np.loadtxt("Human.csv", dtype="str", delimiter=',')
fichier_arduino = np.loadtxt("arduino.csv", dtype="str", delimiter=',')
fichier_human_replica = np.loadtxt("replica_human.csv", dtype="str", delimiter=',')

for i in range(len(fichier_human)):
	time_human.append(fichier_human[i][3])
	data_human.append(fichier_human[i][2])


for z in range(len(fichier_human_replica)):
	time_human_replica.append(fichier_human_replica[z][5])
        data_human_replica.append(fichier_human_replica[z][1])
print(time_human_replica)
print(data_human_replica)

for j in range(len(fichier_arduino)):
        time_arduino.append(int(fichier_arduino[j][1])*10**-3)
        data_arduino.append(fichier_arduino[j][2])
print(time_arduino)
print(data_arduino)

for y in data_human_replica:
	times += match[y]
print(times)
plt.scatter(data_human, time_human, color='red', label ='Human sensors')
plt.scatter(data_arduino, time_arduino, color='blue', label ='pressure sensors')
plt.scatter(data_human_replica, time_human_replica, color='yellow', label ='human replica sensors')
plt.xlabel('weight (g)')
plt.ylabel('time response (s)')
plt.title('Time response according to weight')
plt.legend()
plt.savefig('Time_responses_according_to_weight.png')
plt.show()
