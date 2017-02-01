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
replicates = 3


# functions
def getData():

    for i in listVibrations:
        for j in range(replicates):
            with open('electronic_sensor/25_' + str(i) + '_' + str(j + 1), 'r') as rawData:
                for line in rawData:
                    key = i
                    cleanData25[key].append(line.strip('\n'))

    for i in listVibrations:
        for j in range(replicates):
            with open('electronic_sensor/40_' + str(i) + '_' + str(j + 1), 'r') as rawData:
                for line in rawData:
                    key = i
                    cleanData40[key].append(line.strip('\n'))


def firstGraph():

    title_font = {'fontname': 'Arial', 'size': '20', 'color': 'black', 'weight': 'normal',
                  'verticalalignment': 'top'}
    axis_font = {'fontname': 'Arial', 'size': '19'}
    fig = plt.figure()
    fig.suptitle("Measured intensity by electronic sensor in function of intensity of the motor", **title_font)

    averageOne = []
    for i in cleanData25:
        values = 0
        for j in range(len(cleanData25[int(i)])):
            values += int(cleanData25[int(i)][int(j)])
        averageOne.append(values / (len(cleanData25[int(i)])))

    plt.subplot(211)
    # plt.title('average at 25cm')
    plt.ylabel('at 25cm', **axis_font)
    plt.plot(listVibrations, averageOne, marker='o', linestyle='none', markeredgewidth=5, color='blue')

    averageTwo = []
    for i in cleanData40:
        values = 0
        for j in range(len(cleanData40[int(i)])):
            values += int(cleanData40[int(i)][int(j)])
        averageTwo.append(values / (len(cleanData40[int(i)])))

    plt.subplot(212)
    # plt.title('average at 40cm')
    plt.xlabel('strength of motor', **axis_font)
    plt.ylabel('at 40cm', **axis_font)
    plt.plot(listVibrations, averageTwo, marker='o', linestyle='none', markeredgewidth=5, color='red')

    plt.show()


# calls
getData()
firstGraph()
