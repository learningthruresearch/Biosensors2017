# coding = UTF-8
# written by Samuel Churlaud
# see github.com/learningthruresearch/Biosensors2017/tree/master/poworm_rangers
# version 1.0

# modules
import matplotlib.pyplot as plt

# variables
cleanData = []
average = []


# functions
def getData():

    with open('data_output', 'r') as rawData:
        for line in rawData:
            cleanData.append(line.strip('\n'))
    rawData.close()


def firstGraph():

    for i in range(int(len(cleanData) / 10)):
        values = 0
        for j in range(10):
            values += int(cleanData[(i * 10) + j])
        average.append(int(values) / 10)

    plt.plot(average)
    plt.xlabel('time')
    plt.ylabel('vibration')
    plt.show()


# calls
getData()
firstGraph()
