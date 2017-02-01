# coding = UTF-8
# written by Samuel Churlaud
# see github.com/learningthruresearch/Biosensors2017/tree/master/poworm_rangers
# version 2.1

# modules
import matplotlib.pyplot as plt

# variables
cleanData25 = {0: [], 100: [], 150: [], 200: [], 255: []}
cleanData40 = {0: [], 100: [], 150: [], 200: [], 255: []}
listVibrations = [0, 100, 150, 200, 255]
numberData = 3


# functions
def getData():

    for i in listVibrations:
        for j in range(numberData):
            with open('data/25_' + str(i) + '_' + str(j + 1), 'r') as rawData:
                for line in rawData:
                    key = i
                    cleanData25[key].append(line.strip('\n'))

    for i in listVibrations:
        for j in range(numberData):
            with open('data/40_' + str(i) + '_' + str(j + 1), 'r') as rawData:
                for line in rawData:
                    key = i
                    cleanData40[key].append(line.strip('\n'))


def firstGraph():

    fig = plt.figure()
    fig.suptitle("electronic sensor")

    averageOne = []
    for i in cleanData25:
        values = 0
        for j in range(len(cleanData25[int(i)])):
            values += int(cleanData25[int(i)][int(j)])
        averageOne.append(values / (len(cleanData25[int(i)])))

    plt.subplot(211)
    # plt.title('average at 25cm')
    plt.ylabel('observed vibrations at 25cm')
    plt.plot(listVibrations, averageOne, marker='o', linestyle='none', markeredgewidth=5, color='blue')

    averageTwo = []
    for i in cleanData40:
        values = 0
        for j in range(len(cleanData40[int(i)])):
            values += int(cleanData40[int(i)][int(j)])
        averageTwo.append(values / (len(cleanData40[int(i)])))

    plt.subplot(212)
    # plt.title('average at 40cm')
    plt.xlabel('strength of motor')
    plt.ylabel('observed vibrations at 40cm')
    plt.plot(listVibrations, averageTwo, marker='o', linestyle='none', markeredgewidth=5, color='red')

    plt.show()


# calls
getData()
firstGraph()
