# coding = UTF-8
# written by Samuel Churlaud
# see github.com/learningthruresearch/Biosensors2017/tree/master/poworm_rangers
# version 1.0

# modules
import csv
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# variables
listVibrations = [0, 100, 150, 200, 255]
replicates = ['A', 'B', 'C', 'D', 'E', 'F']
average0 = []
average100 = []
average150 = []
average200 = []
average255 = []
time = []


# functions
def results0():
    for i in range(29):
        average0.append(int(0))

    for i in replicates:
        reader = csv.reader(open('clean_bio_sensor/Results0' + i + '.csv', 'r'))
        for line in reader:
            print(line[0])
            if int(line[0]) <= 29:
                average0[int(line[0]) - 1] += float(line[1])
            else:
                pass


def results100():

    for i in range(29):
        average100.append(int(0))

    for i in replicates:
        reader = csv.reader(open('clean_bio_sensor/Results100' + i + '.csv', 'r'))
        for line in reader:
            print(line[0])
            if int(line[0]) <= 29:
                average100[int(line[0]) - 1] += float(line[1])
            else:
                pass


def results150():
    for i in range(29):
        average150.append(int(0))

    for i in replicates:
        reader = csv.reader(open('clean_bio_sensor/Results150' + i + '.csv', 'r'))
        for line in reader:
            print(line[0])
            if int(line[0]) <= 29:
                average150[int(line[0]) - 1] += float(line[1])
            else:
                pass


def results200():
    for i in range(29):
        average200.append(int(0))

    for i in replicates:
        if i == 'B':
            pass
        else:
            reader = csv.reader(open('clean_bio_sensor/Results200' + i + '.csv', 'r'))
            for line in reader:
                print(line[0])
                if int(line[0]) <= 29:
                    average200[int(line[0]) - 1] += float(line[1])
                else:
                    pass


def results255():
    for i in range(29):
        average255.append(int(0))

    for i in replicates:
        reader = csv.reader(open('clean_bio_sensor/Results255' + i + '.csv', 'r'))
        for line in reader:
            print(line[0])
            if int(line[0]) <= 29:
                average255[int(line[0]) - 1] += float(line[1])
            else:
                pass


def normalize():
    for i in range(len(average0)):
        average0[i] *= (1 / 6)
        average100[i] *= (1 / 6)
        average150[i] *= (1 / 6)
        average200[i] *= (1 / 5)
        average255[i] *= (1 / 6)
        time.append(i * 4)


def graph():

    plot0 = mlines.Line2D(time, average0, color='blue', label='0 intensity', linewidth=4)
    plot100 = mlines.Line2D(time, average100, color='cyan', label='100 intensity', linewidth=4)
    plot150 = mlines.Line2D(time, average150, color='green', label='150 intensity', linewidth=4)
    plot200 = mlines.Line2D(time, average200, color='orange', label='200 intensity', linewidth=4)
    plot255 = mlines.Line2D(time, average255, color='red', label='255 intensity', linewidth=4)

    plt.legend(handles=[plot0, plot100, plot150, plot200, plot255], prop={'size': 15})

    plt.plot(time, average0, color='blue', linewidth=3)
    plt.plot(time, average100, color='cyan', linewidth=3)
    plt.plot(time, average150, color='green', linewidth=3)
    plt.plot(time, average200, color='orange', linewidth=3)
    plt.plot(time, average255, color='red', linewidth=3)
    title_font = {'fontname': 'Arial', 'size': '20', 'color': 'black', 'weight': 'normal',
                  'verticalalignment': 'bottom'}
    axis_font = {'fontname': 'Arial', 'size': '19'}
    plt.title('Distance between the worm and the motor in function of time', **title_font)
    plt.xlabel('Distance', **axis_font)
    plt.ylabel('Time in seconds', **axis_font)

    plt.show()


# calls
results0()
results100()
results150()
results200()
results255()
normalize()
graph()
