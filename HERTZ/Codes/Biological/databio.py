import csv

fichier = open('output.csv', 'rb')                   # opens the file
subjects = dict()                                    # creates a dictionary for subjects
a = fichier.readlines()                              # reads everyline of the file
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

addvalues(freq60Hz)
addvalues(freq250Hz)
addvalues(freq2000Hz)
