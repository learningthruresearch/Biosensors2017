import matplotlib.pyplot as plt
import csv

x = []
y = []
z = []

with open('compa.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=' ')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))

plt.plot(x,y, label = 'conductometer')
plt.plot(x,z, label = 'arduino')
plt.xlabel('Concentration (in M/L)')
plt.ylabel('Conductivity (in Ohm)')
plt.title('Conductivity according to concentration')
plt.legend()
plt.show()
