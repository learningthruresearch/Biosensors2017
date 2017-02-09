import numpy as np
import matplotlib.pyplot as plt	

lum = open("Lum.csv","r")
Lum = []
Time1 = []
Time2 = []

for line in lum.readlines():
    a = line.split("  ")
    A = a[-1].strip()
    Lum.append(A)
print(Lum)


temp = open("Temp.csv","r")
Temp = []

for line in temp.readlines():
    b = line.split('Raw = ')
    B = b[-1].strip()
    Temp.append(B)
print(Temp)

for i in range(len(Lum)):
    Time1.append(30*i)
print(Time1)

for i in range(len(Temp)):
    Time2.append(30*i)
print(Time2)

plt.subplot(211)
plt.plot(Time2,Temp,'g') 
plt.ylabel('Temperature')
plt.xlabel('Time')
plt.title('Temperature according to the time')

plt.subplot(212)
plt.plot(Time1,Lum,'r') 
plt.xlabel('Time')
plt.ylabel('Luminosity')
plt.title('Luminosity according to the time')

plt.show()
