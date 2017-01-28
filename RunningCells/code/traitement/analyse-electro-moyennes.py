import numpy as np
import matplotlib.pyplot as plt

LED0, LDR0 = np.genfromtxt("0intensity-50measures.csv", unpack=True, delimiter=",")

LED25, LDR25 = np.genfromtxt("25intensity-50measures.csv", unpack=True, delimiter=",")

LED50, LDR50 = np.genfromtxt("50intensity-50measures.csv", unpack=True, delimiter=",")

LED75, LDR75 = np.genfromtxt("75intensity-50measures.csv", unpack=True, delimiter=",")

LEDMax, LDRMax = np.genfromtxt("Maxintensity-50measures.csv", unpack=True, delimiter=",")

dataLED = [0, 25, 50, 75, 100]

LDR0mean = np.mean(LDR0)

LDR25mean = np.mean(LDR25)

LDR50mean = np.mean(LDR50)

LDR75mean = np.mean(LDR75)

LDRMaxmean = np.mean(LDRMax)

dataLDRmeans = [LDR0mean, LDR25mean, LDR50mean, LDR75mean, LDRMaxmean]
plt.xlabel("LED intensity in %")
plt.ylabel("Mean of 50 LDR measurements")
plt.title("Mean of 50 LDR measurements according to one LED intensity - with 100ms delay")
plt.scatter(dataLED, dataLDRmeans, c = 'red', s = 100)
plt.xlim([0,100])
plt.ylim([0,200])
plt.show()
