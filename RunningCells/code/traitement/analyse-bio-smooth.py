import numpy as np
import matplotlib.pyplot as plt

time501, velocity501 = np.genfromtxt("data-50%-1.csv", unpack=True, delimiter=",", skip_header=2)

time502, velocity502 = np.genfromtxt("data-50%-2.csv", unpack=True, delimiter=",", skip_header=2)

time503, velocity503 = np.genfromtxt("50%-3.csv", unpack=True, delimiter=",", skip_header=2)

time751, velocity751 = np.genfromtxt("data75%-1.csv", unpack=True, delimiter=",", skip_header=2)

time752, velocity752 = np.genfromtxt("data75%-2.csv", unpack=True, delimiter=",", skip_header=2)

time251, velocity251 = np.genfromtxt("25%-1.csv", unpack=True, delimiter=",", skip_header=2)

time252, velocity252 = np.genfromtxt("25%-2.csv", unpack=True, delimiter=",", skip_header=2)

time253, velocity253 = np.genfromtxt("25%-3.csv", unpack=True, delimiter=",", skip_header=2)

timeMAX1, velocityMAX1 = np.genfromtxt("MAX1.csv", unpack=True, delimiter=",", skip_header=2)

timeNoir, velocityNoir = np.genfromtxt("Noir.csv", unpack=True, delimiter=",", skip_header=2)

Velocity501 = velocity501 / 1.8
Velocity502 = velocity502 / 1.8
Velocity503 = velocity503 / 1.8
Velocity751 = velocity751 / 1.8
Velocity752 = velocity752 / 1.8
Velocity251 = velocity251 / 1.8
Velocity252 = velocity252 / 1.8
Velocity253 = velocity253 / 1.8
VelocityMAX1 = velocityMAX1 / 1.8
VelocityNoir = velocityNoir / 1.8

def smoothitout(OneDnumpy, number_of_bins):
    data = np.split(OneDnumpy, len(OneDnumpy) / number_of_bins)
    Mean = []
    for i in range(len(data) - 1):
        Mean.append(np.mean(data[i]))
    return Mean

dataNoir = smoothitout(VelocityNoir, 10)
dataMAX1 = smoothitout(VelocityMAX1, 10)
data501 = smoothitout(Velocity501, 10)
data502 = smoothitout(Velocity502, 10)
data503 = smoothitout(Velocity503, 10)
data251 = smoothitout(Velocity251, 10)
data252 = smoothitout(Velocity252, 10)
data253 = smoothitout(Velocity253, 10)
data751 = smoothitout(Velocity751, 10)
data752 = smoothitout(Velocity752, 10)
Time11 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
Time15 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]


plt.subplot(221)
plt.xlabel("Time in minutes")
plt.ylabel("Velocity of the gas release in cm.min-¹")
plt.title("Velocity of the gas release according to time - 25% LED intensity")
plt.plot(Time15, data251, label='Replicate 1')
plt.plot(Time15, data252, label='Replicate 2')
plt.plot(Time15, data253, label='Replicate 3')
plt.legend()
plt.ylim([0,0.4])

plt.subplot(222)
plt.xlabel("Time in minutes")
plt.ylabel("Velocity of the gas release in cm.min-¹")
plt.title("Velocity of the gas release according to time - 75% LED intensity")
plt.plot(Time11, data751, label='Replicate 1')
plt.plot(Time11, data752, label='Replicate 2')
plt.legend()
plt.ylim([0,0.4])

plt.subplot(223)
plt.xlabel("Time in minutes")
plt.ylabel("Velocity of the gas release in cm.min-¹")
plt.title("Velocity of the gas release according to time - 50% LED intensity")
plt.plot(Time11, data501, label='Replicate 1')
plt.plot(Time11, data502, label='Replicate 2')
plt.plot(Time11, data503, label='Replicate 3')
plt.legend()
plt.ylim([0,0.4])

plt.subplot(224)
plt.xlabel("Time in minutes")
plt.ylabel("Velocity of the gas release in cm.min-¹")
plt.title("Velocity of the gas release according to time - Controls")
plt.plot(Time15, dataNoir, label='Negative Control')
plt.plot(Time15, dataMAX1, label='Positive Control')
plt.legend()
plt.ylim([0,0.4])
plt.show()
