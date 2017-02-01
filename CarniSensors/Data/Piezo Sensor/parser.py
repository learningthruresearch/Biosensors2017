import matplotlib.pyplot as plt

frq = 1.2 #measuring frequency of the sensor

file = open('10%(3).csv', 'r')

grosseliste = [] #list for all numbers
time = [] #list for time scale in graph

mesure1 = [] #lists for data fom different repetitions
mesure2 = []
mesure3 = []

for aline in file.readlines(): #removing unwanted characters and putting data in one large list
    miniliste = aline.split('\r\n')
    del miniliste[-1]
    grosseliste.append(miniliste)

for i in range(1, 2000): #separating data from each repetition
    mesure1.append(grosseliste[i])
for i in range(2001, 4000):
    mesure2.append(grosseliste[i])
for i in range(4001, 6000):
    mesure3.append(grosseliste[i])

for i in range(1, 2000): #adding timestamps to time list
    time.append(i * frq)

plt.subplot(311) #plotting data from each repetition
plt.plot(time, mesure1, color = 'r', label ='red')
plt.title('Piezo element measurement according to time')
plt.subplot(312)
plt.plot(time, mesure2, color = 'r', label ='red')
plt.ylabel('Piezo element value(no unit))')
plt.subplot(313)
plt.plot(time, mesure3, color = 'r', label ='red')
plt.xlabel('time(ms)')
plt.show()

file.close()
