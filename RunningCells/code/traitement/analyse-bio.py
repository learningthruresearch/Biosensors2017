import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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

axes = plt.gca()

plt.subplot(221)
plt.xlabel("Time in min")
plt.ylabel("Velocity of the gas release in cm.min⁻¹")
plt.title("Velocity of the gas release according to time - 50% LED intensity")
plt.plot(time501, Velocity501, "b", label="Replicate 1")
plt.plot(time502, Velocity502, "c", label="Replicate 2")
plt.plot(time502, Velocity503, "m", label="Replicate 3")
plt.ylim([0,0.8])
plt.legend()

plt.subplot(222)
plt.xlabel("Time in min")
plt.ylabel("Velocity of the gas release in cm.min⁻¹")
plt.title("Velocity of the gas release according to time - 75% LED intensity")
plt.plot(time751, Velocity751, "g", label="Replicate 1")
plt.plot(time752, Velocity752, "y", label="Replicate 2")
plt.ylim([0,0.8])
plt.legend()

plt.subplot(223)
plt.xlabel("Time in min")
plt.ylabel("Velocity of the gas release in cm.min⁻¹")
plt.title("Velocity of the gas release according to time - 25% LED intensity")
plt.plot(time251, Velocity251, "r", label="Replicate 1")
plt.plot(time252, Velocity252, "k", label="Replicate 2")
plt.plot(time253, Velocity253, "m", label="Replicate 3")
plt.ylim([0,0.8])
plt.legend()

plt.subplot(224)
plt.xlabel("Time in min")
plt.ylabel("Velocity of the gas release in cm.min⁻¹")
plt.title("Velocity of the gas release according to time - Controls")
plt.plot(timeMAX1, VelocityMAX1, "y", label="Positive control")
plt.plot(timeNoir, VelocityNoir, "k", label="Negative control")
plt.ylim([0,0.8])
plt.legend()

plt.show()
