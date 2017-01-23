# coding UTF-8
# written by Samuel Churlaud
# data analysis for Bio-Lumos project
# version 1.0

import csv
import math

# files
data = csv.reader(open('data.csv', 'r'))
template = list(csv.reader(open('template.csv', 'r')))[0]
innerControls = csv.reader(open('inner_controls.csv', 'r'))
results = open('results.csv', 'w+')
conflicts_uncorrected = open('conflicts_uncorrected.csv', 'w+')

# variables
innerDict = {}  # associated with one key are all the positions for one given pair and its control
gapDict = {}  # associated with one key are the gap between two colors of a pair (from 0 to 3)
cleanData = []  # list of lists with what data.csv contains


# transform raw data into pythonic, easy to manipulate variables and files ; gives some stats
def readData():

    # transform csvreader (hard to manipulate) into a list of lists, with one list being one subject's results
    for line in data:
        justaList = []
        for i in line:
            justaList.append(i)
        cleanData.append(justaList)

    # write "True"s and "False"s into results file
    goodAnwsers = 0
    badAnswers = 0
    subjects = 0
    for line in cleanData:
        subjects += 1
        for i in range(len(line)):
            if line[i] == template[i]:
                results.write('True')
                goodAnwsers += 1
            else:
                results.write('False')
                badAnswers += 1
            if i == len(line) - 1:
                pass
            else:
                results.write(',')
        results.write('\n')
    print('subjects : ' + str(subjects))
    print('good answers : ' + str(goodAnwsers))
    print('bad answers : ' + str(badAnswers))
    mean = goodAnwsers / (goodAnwsers + badAnswers)
    print('average : ' + str(mean * 100) + '%')
    var = 0
    dataLength = 0
    for line in cleanData:
        for i in range(len(line)):
            if line[i] == template[i]:
                var += ((mean - 1) ** 2)
            else:
                var += ((mean - 0) ** 2)
            dataLength += 1
    sdt = math.sqrt((var) / (dataLength - 1))
    print('standart deviation : ' + str(sdt))

    # transform inner controls into dictionnary with number of pairs as keys and positions of pairs as values
    for row in innerControls:
        key = row[0]
        innerDict[key] = row[2:]
        key = row[1]
        gapDict[key] = row[2:]

    # compare inner controls and save contradictions' positions in conflicts_uncorrected.csv
    for i in range(len(cleanData)):
        for key in innerDict:
            for j in range(1, len(innerDict[key])):
                if cleanData[i][(int(innerDict[key][j]) - 1)] != cleanData[i][(int(innerDict[key][0]) - 1)]:
                    conflicts_uncorrected.write(str(i + 1) + ',' + innerDict[key][0] + '\n')
                    conflicts_uncorrected.write(str(i + 1) + ',' + innerDict[key][j] + '\n')
    conflicts_uncorrected.close()

    # remove duplicate lines in conflicts_uncorrected.csv
    nConflicts = 0
    lines_seen = set()  # holds lines already seen
    conflicts = open('conflicts.csv', 'w')
    for line in open('conflicts_uncorrected.csv', 'r'):
        if line not in lines_seen:  # not a duplicate
            conflicts.write(line)
            lines_seen.add(line)
            nConflicts += 1
    conflicts.close()
    conflicts_uncorrected.close()
    print('conflicts : ' + str(nConflicts))


readData()
