import csv
import matplotlib.pyplot as plt
import numpy as np

#fctn that creates a nested dictionary where the keys are the n° of subject and the ear
def addvalues(dictionary):
    for subject in subjects_ears.keys():
        ears = ['left', 'right']                    # creates a list to allow the iteration
        for ear in ears:
            subjects_ear_data = subjects_ears.get(subject).get(ear) # takes the values for each ear for each subject
            for j in dictionary.keys():
                n = list()                          # creates a new list
                for i in subjects_ear_data:         # iterates on the data of each subject's ear
                    if j in i:                      # is the key of the dictionary is in the ear data (if the freq listened to was the key)
                        n.append(i[5])              # append the response to the list 'n'
                dictionary[j].append(n)             # appends the list as a value for the dict keys
    return dictionary

#fctn that equiparates "t"=1 and "o"=0. It makes then a coefficient of response: sums the responses of a subject[ear] and divides the sum by the number of responses.
def counting(dictionary):
    dictionary = addvalues(dictionary)
    detect = {"t":1,"o":0}                          # equiparates "t"=1 and "o"=0
    for key1 in dictionary.keys():                  # iterates on dictionary keys
        data = []
        for values in dictionary.get(key1):         # gets the trios or duos of responses
            if len(values) >= 1:                    # valid data ?
                for i in range(len(values)):
                    values[i] = detect[values[i]]   # changes t and o for 1 and 0
                data.append(sum(values)/len(values))# it sums the new values and divides it sum by the number of responses. 
        dictionary[key1] = data                     # adds data to the key
    return dictionary


fichier = open('output.csv', 'rb')                   # opens the file
a = fichier.readlines()                              # reads everyline of the file

subjects = dict()                                    # creates a dictionary for subjects
for i in range(1,len(a)):                            # loop to fill the dictionary
    data = str(a[i]).replace("\\n'", '').replace('"','').split(',')  # deletes the '\\n' and makes a list out of the values separed by a ','
    if len(data) >= 9:                               # valid data?
        subjectID = data[8]                          # takes the number of subject
        if subjectID not in subjects:                # verify if the number of subject is a key for the dictionary
            subjects[subjectID] = list()             # adds the key to the list
        subjects[subjectID].append(data)             # adds the data of subject X as a value for its key.

subjects_ears = dict()
for subject in subjects.keys():
    subjects_ears[subject] = dict()
    subjects_ears[subject]['right'] = list()             # create a nested dictionar with the keys 'left' and 'right' for every subject
    subjects_ears[subject]['left'] = list()
    for line in subjects.get(subject):
        if line[3] == 'left':                        # verify if the ear the subject was using was the left one
            subjects_ears[subject]['left'].append(line)  # adds the data as a 'left' key value
        else:                                        # if not left ear:
            subjects_ears[subject]['right'].append(line) # adds the data as a 'left' key value

freq60Hz = {'60Hz-0diff':[],'60Hz-2diff':[],'60Hz-4diff':[], '60Hz-8diff':[], '60Hz-20diff':[]}         # creates adictionary for each frequency
freq250Hz = {'250Hz-0diff':[],'250Hz-2diff':[],'250Hz-4diff':[],'250Hz-8diff':[],'250Hz-20diff':[]}
freq2000Hz = {'2000Hz-0diff':[],'2000Hz-2diff':[],'2000Hz-4diff':[],'2000Hz-8diff':[],'2000Hz-20diff':[]}

print(counting(freq60Hz))
print(counting(freq250Hz))
print(counting(freq2000Hz))

cle = ['0 Hz', '2 Hz', '4 Hz', '8 Hz', '20 Hz']

fig = plt.figure(1, figsize=(9, 6))
ax = fig.add_subplot(111)
bp = ax.boxplot([freq60Hz['60Hz-0diff'], freq60Hz['60Hz-2diff'], freq60Hz['60Hz-4diff'], freq60Hz['60Hz-8diff'], freq60Hz['60Hz-20diff']], positions = range(5), patch_artist=True)
#lp = ax.plot(range(55, 85), range(55, 85), label = 'x=y')
ax.set_xticklabels(cle)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.set_ylim([-0.5,1.5])
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_title('Results for 60 Hz')
ax.set_xlabel('Modulation in Hertz')
ax.set_ylabel('Detection coefficient in AU (between 0 and 3)')
ax.legend()

## change outline color, fill color and linewidth of the boxes
for box in bp['boxes']:
    # change outline color
    box.set( color= 'red', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='red', linewidth=2)

## change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color='red', linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='red', linewidth=2)

## change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker='+', color='red', alpha=0.5)



fig1 = plt.figure(2, figsize=(9, 6))
ax1 = fig1.add_subplot(111)
bp1 = ax1.boxplot([freq250Hz['250Hz-0diff'], freq250Hz['250Hz-2diff'], freq250Hz['250Hz-4diff'], freq250Hz['250Hz-8diff'],freq250Hz['250Hz-20diff']], positions = range(5), patch_artist=True)
#lp1 = ax1.plot(range(245, 275), range(245, 275), label = 'x=y')
ax1.set_xticklabels(cle)
ax1.get_xaxis().tick_bottom()
ax1.get_yaxis().tick_left()
ax1.set_ylim([-0.5,1.5])
ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax1.set_title('Results for 250 Hz')
ax1.set_xlabel('Modulation in Hertz')
ax1.set_ylabel('Detection coefficient in AU (between 0 and 3)')
ax1.legend()

## change outline color, fill color and linewidth of the boxes
for box in bp1['boxes']:
    # change outline color
    box.set( color='r', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
for whisker in bp1['whiskers']:
    whisker.set(color='r', linewidth=2)

## change color and linewidth of the caps
for cap in bp1['caps']:
    cap.set(color='r', linewidth=2)

## change color and linewidth of the medians
for median in bp1['medians']:
    median.set(color='r', linewidth=2)

## change the style of fliers and their fill
for flier in bp1['fliers']:
    flier.set(marker='+', color='r', alpha=0.5)



fig2 = plt.figure(3, figsize=(9, 6))
ax2 = fig2.add_subplot(111)
bp2 = ax2.boxplot([freq2000Hz['2000Hz-0diff'], freq2000Hz['2000Hz-2diff'], freq2000Hz['2000Hz-4diff'], freq2000Hz['2000Hz-8diff'], freq2000Hz['2000Hz-20diff']], positions = range(5), patch_artist=True)
#lp2 = ax2.plot(range(1995, 2025), range(1995, 2025), label = 'x=y')
ax2.set_xticklabels(cle)
ax2.get_xaxis().tick_bottom()
ax2.get_yaxis().tick_left()
ax2.set_ylim([-0.5,1.5])
ax2.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax2.set_title('Results for 2000 Hz')
ax2.set_xlabel('Modulation in Hertz')
ax2.set_ylabel('Detection coefficient in AU (between 0 and 3)')
ax2.legend()

## change outline color, fill color and linewidth of the boxes
for box in bp2['boxes']:
    # change outline color
    box.set( color='r', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
for whisker in bp2['whiskers']:
    whisker.set(color='r', linewidth=2)

## change color and linewidth of the caps
for cap in bp2['caps']:
    cap.set(color='r', linewidth=2)

## change color and linewidth of the medians
for median in bp2['medians']:
    median.set(color='r', linewidth=2)

## change the style of fliers and their fill
for flier in bp2['fliers']:
    flier.set(marker='+', color='r', alpha=0.5)


fig.savefig('electronic_60Hz.png')
fig1.savefig('electronic_250Hz.png')
fig2.savefig('electronic_2000Hz.png')



plt.show()
