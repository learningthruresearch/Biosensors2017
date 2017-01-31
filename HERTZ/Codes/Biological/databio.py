import csv
import matplotlib.pyplot as plt
import numpy as np
import pylab
import re

fichier = open('subject-0.csv', 'r')             #opens the file
subjects = dict()                                #creates a dictionary for subjects
for i in fichier:                                #loop to fill the dictionary 
    data = fichier.readline().strip().split(',') #reads every line, deletes the '\n' and makes a list out of the values separed by a ','
    if len(data) >= 9:                           #valid data?
        subject = data[8]                        #Takes the number of subject
        if subject not in subjects:              #Verify if the number of subject is a key for the dictionary
            subjects[subject] = list()           #Adds the key to the list
        subjects[subject].append(data)           #Adds the data of subject X as a value for its key.

subjects_ears = dict()
for key in subjects.keys():
    subjects_ears[key] = dict()
    subjects_ears[key]['right'] = list()         #Create a nested dictionar with the key 'left' and 'right'
    subjects_ears[key]['left'] = list()
    for line in subjects.get(key):
        if line[3] == 'left':                    # Verify if the ear the subject was using was the left one
            subjects_ears[key]['left'].append(line)  #Adds the data as a valueto the 'left' key
        else:
            subjects_ears[key]['right'].append(line)
#print(subjects_ears)


freq60Hz = {'60Hz-0diff':{'left':[],'right':[]},'60Hz-2diff':{'left':[],'right':[]},'60Hz-4diff':{'left':[],'right':[]},'60Hz-20diff':{'left':[],'right':[]}}
freq250Hz = {'250Hz-0diff':{'left':[],'right':[]},'250Hz-2diff':{'left':[],'right':[]},'250Hz-4diff':{'left':[],'right':[]},'250Hz-20diff':{'left':[],'right':[]}}
freq2000Hz = {'2000Hz-0diff':{'left':[],'right':[]},'2000Hz-2diff':{'left':[],'right':[]},'2000Hz-4diff':{'left':[],'right':[]},'2000Hz-20diff':{'left':[],'right':[]}} 

for key in subjects_ears.keys():
    ears = ['left', 'right']
    print("for ear in", ears)
    for ear in ears:
        print(ear)
        print("f = subjects_ears.get(key).get(ear)")
        f = subjects_ears.get(key).get(ear)
        print("for i in f")
        n = list()
        for i in f:
            print(i)
            print("for j in freq60Hz.keys()")
            for j in freq60Hz.keys():
                print("if", j, "in", i)
                if j in i:
                    print("n.append(",i[5],")")
                    n.append(i[5])
                    print(n)
        freq60Hz[j][ear].append(n)
print(freq60Hz)

