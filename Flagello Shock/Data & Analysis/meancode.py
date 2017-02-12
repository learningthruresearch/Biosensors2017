import matplotlib.pyplot as plt

file = open('mean.csv','r') #open the file with all our data
data = file.readlines()  
                    #all the lists we will use              
replicat1 = []
replicat2 = []
replicat3 = []
n = 0                      #indentation to number each ligne of our data

for i in data[1:]:         # we read every ligne of data exept the first one (ligne of titles)
    n += 1                 #number of each ligne of data
    var1 = i.strip('\n').split('\t')   #strip the \t and 
    if n<4:
        replicat1.append(float(var1[1]))
    elif 3<n<7:           # same operation for the second replicat
        replicat2.append(float(var1[1]))
    else:                   # same opertion for second replicat
        replicat3.append(float(var1[1]))      

ph = [7,5.5,4]
g1 = plt.scatter(ph,replicat1, marker='o', color='r', s = 60) #scatter plot with each replicat
g2 = plt.scatter(ph,replicat2, marker='o', color='y', s = 60)
g3 = plt.scatter(ph,replicat3, marker='o', color='b', s = 60)

plt.ylim((0,110)) #Y axis represents a percentage so limited to 100
#plt.xticks([1, 2, 3], ['4', '5,5', '7']) #label of xaxis for the boxplot
plt.xlabel('pH', size = 18)
plt.ylabel('% of flagellated Chamydomonas', size = 18)
plt.title('Mean of flagellated Chalydomonas according to pH', size = 20)
plt.legend([g1, g2, g3],
           ['Replicat 1', 'Replicat 2', 'Replicat 3'],
           loc='upper left')
plt.show()

