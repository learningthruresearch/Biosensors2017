import numpy as np
import matplotlib.pyplot as plt

time501, velocity501 = np.genfromtxt("data-50%-1.csv", unpack=True, delimiter=",", skip_header=2)

time502, velocity502 = np.genfromtxt("data-50%-2.csv", unpack=True, delimiter=",", skip_header=2)

time751, velocity751 = np.genfromtxt("data75%-1.csv", unpack=True, delimiter=",", skip_header=2)

time752, velocity752 = np.genfromtxt("data75%-2.csv", unpack=True, delimiter=",", skip_header=2)

time251, velocity251 = np.genfromtxt("25%-1.csv", unpack=True, delimiter=",", skip_header=2)

time252, velocity252 = np.genfromtxt("25%-2.csv", unpack=True, delimiter=",", skip_header=2)

time253, velocity253 = np.genfromtxt("25%-3.csv", unpack=True, delimiter=",", skip_header=2)

timeMAX1, velocityMAX1 = np.genfromtxt("MAX1.csv", unpack=True, delimiter=",", skip_header=2)

timeNoir, velocityNoir = np.genfromtxt("Noir.csv", unpack=True, delimiter=",", skip_header=2)

Velocity501 = velocity501 / 1.8
Velocity502 = velocity502 / 1.8
Velocity751 = velocity751 / 1.8
Velocity752 = velocity752 / 1.8
Velocity251 = velocity251 / 1.8
Velocity252 = velocity252 / 1.8
Velocity253 = velocity253 / 1.8
VelocityMAX1 = velocityMAX1 / 1.8
VelocityNoir = velocityNoir / 1.8

Velocity501mean = np.mean(Velocity501)
Velocity502mean = np.mean(Velocity502)
Velocity751mean = np.mean(Velocity751)
Velocity752mean = np.mean(Velocity752)
Velocity251mean = np.mean(Velocity251)
Velocity252mean = np.mean(Velocity252)
Velocity253mean = np.mean(Velocity253)
VelocityMAX1mean = np.mean(VelocityMAX1)
VelocityNoirmean = np.mean(VelocityNoir)

percentages = [0, 25, 50, 75, 100]
R1 = [VelocityNoirmean, Velocity251mean, Velocity501mean, Velocity751mean, VelocityMAX1mean]
R2 = [0, Velocity252mean, Velocity502mean, Velocity752mean, 0]
R3 = [0, Velocity253mean, 0, 0, 0]
Replicate1 = plt.scatter(percentages, R1, c = 'red', s = 60, label="Replicate1")
Replicate2 = plt.scatter(percentages, R2, c = 'yellow', s = 60, label="Replicate2")
Replicate3 = plt.scatter(percentages, R3, c = 'green', s = 60, label="Replicate3")
plt.xlabel('LEDs intensity in %', fontsize = 20)
plt.ylabel('Mean velocity of the gas release during  experiment', fontsize = 20)
plt.legend((Replicate1, Replicate2, Replicate3),
           ('Replicate 1', 'Replicate 2', 'Replicate 3'),
           scatterpoints=1,
           loc='lower right',
           ncol=3,
           fontsize=20)
plt.show()
