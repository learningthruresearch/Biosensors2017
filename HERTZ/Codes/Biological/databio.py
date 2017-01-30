import csv
import matplotlib.pyplot as plt
import numpy as np
import pylab

dd = open('subject-0.csv', 'r')         #opens the file
subjects = dict()
for i in dd:
    data = dd.readline().strip().split(',')
    subjet = data[8]
    if len(data) >= 9:  # valid data?
        if subjet not in subjects:
            subjects[subjet] = list()
        subjects[subjet].append(data)
print(subjects) 

