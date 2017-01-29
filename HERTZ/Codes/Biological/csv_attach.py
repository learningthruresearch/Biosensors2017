import csv
import sys

with open('subject-1.csv', 'r') as data:         #opens the file
    with open("data_gathered.csv", 'w') as new:
        next(data)
        new1 = new.readlines()
        for i in new1:
            if data[1][8] == new1[i][8]:
                for line in data:
                    new.write(line)

