import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

LED, LDR = np.genfromtxt("data-electroLDR.csv", unpack=True, delimiter=",", skip_header=1)

LED2 = LED / 2.55

plt.xlabel("LED instensity in %")
plt.ylabel("LDR measurement")
plt.title("LDR measurement according to LED intensity")
plt.plot(LED2, LDR, "b")
plt.show()
