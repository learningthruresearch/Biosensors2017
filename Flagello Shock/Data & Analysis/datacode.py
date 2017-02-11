import matplotlib.pyplot as plt

file = open('data.csv','r') #open the file with all our data
data = file.readlines()  

ph = []                     #all the lists we will use              
replicat1 = []
replicat2 = []
replicat3 = []
grosdata = []
n = 0                      #indentation to number each ligne of our data

for i in data[1:]:         # we read every ligne of data exept the first one (ligne of titles)
    n += 1                 #number of each ligne of data
    var1 = i.strip('\n').split('\t')   #strip the \t and \n
    if n<10:                           # there are 9 data per replicat so we look at the first replicat
        ph.append(float(var1[0]))      # the first colum of the csv is pH, we transform numbres in float and we make a list of pH. We use this list for each replicat
        replicat1.append(float(var1[1]))  # we make a list with all the values of the first replicat. 
    elif 9<n<19:           # same operation for the second replicat
        replicat2.append(float(var1[1]))
    else:                   # same opertion for second replicat
        replicat3.append(float(var1[1]))

grosdata.append(replicat1[6:9])  #grosdata is a list of lists which brings together every pH measurement.
grosdata[0]+= replicat2[6:9] #grosdata[0] contains every pH 4 measurement
grosdata[0] += replicat3[6:9]

grosdata.append(replicat1[3:6])
grosdata[1]+= replicat2[3:6] #grosdata[1] contains every pH 5.5 measurement
grosdata[1] += replicat3[3:6]


grosdata.append(replicat1[:3])
grosdata[2]+= replicat2[:3] #grosdata[2] contains every pH 7 measurement
grosdata[2] += replicat3[:3]
print(grosdata[2])

g1 = plt.scatter(ph,replicat1, marker='o', color='r', s =60) #scatter plot with each replicat
g2 = plt.scatter(ph,replicat2, marker='o', color='y', s =60)
g3 = plt.scatter(ph,replicat3, marker='o', color='b', s =60)
#plt.boxplot(grosdata)  #boxplot of every pH
plt.ylim((0,110)) #Y axis represents a percentage so limited to 100
#plt.xticks([1, 2, 3], ['4', '5,5', '7']) #label of xaxis for the boxplot
plt.xlabel('pH', size = 18)
plt.ylabel('% of flagellated Chamydomonas', size = 18)
plt.title('Proportion of flagellated Chalydomonas according to pH', size = 20)
plt.legend([g1, g2, g3],
           ['Replicat 1', 'Replicat 2', 'Replicat 3'],
           loc='upper left')
plt.show()

