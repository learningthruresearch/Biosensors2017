import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('conductometer.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=' ')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x,y)
plt.xlabel('Concentration (in M/L)')
plt.ylabel('Conductivity (in Ohm)')
plt.title('Conductivity according to concentration (conductometer)')
plt.legend()
plt.show()
