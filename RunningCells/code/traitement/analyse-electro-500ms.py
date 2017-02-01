import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

LED1, LDR1 = np.genfromtxt("delay500ms_1.csv", unpack=True, delimiter=",")

LED2, LDR2 = np.genfromtxt("delay500ms_2.csv", unpack=True, delimiter=",")

LED3, LDR3 = np.genfromtxt("delay500ms_3.csv", unpack=True, delimiter=",")

LED4, LDR4 = np.genfromtxt("delay500ms_4.csv", unpack=True, delimiter=",")

LED5, LDR5 = np.genfromtxt("delay500ms_5.csv", unpack=True, delimiter=",")

LED6, LDR6 = np.genfromtxt("delay500ms_6.csv", unpack=True, delimiter=",")

plt.xlabel("LED instensity in %")
plt.ylabel("LDR measurement")
plt.title("LDR measurement according to LED intensity with 500ms delay")

LEDx1 = LED1 / 2.55
plt.plot(LEDx1, LDR1)

LEDx2 = LED2 / 2.55
plt.plot(LEDx2, LDR2)

LEDx3 = LED3 / 2.55
plt.plot(LEDx3, LDR3)

LEDx4 = LED4 / 2.55
plt.plot(LEDx4, LDR4)

LEDx5 = LED5 / 2.55
plt.plot(LEDx5, LDR5)

LEDx6 = LED6 / 2.55
plt.plot(LEDx6, LDR6)

plt.show()
