import numpy as np
import matplotlib.pyplot as plt
import csv

data = open('data.csv', 'r')
fichier = data.readlines()
yep = ''
ordonnee = []
ordonnees = []
match_absc = []
abscisse = []
abscisses= []
individus = ''
match = {'4' : '300', '11': '300', '13': '300', '17': '300', '20': '300', '14' : '500', '22': '500', '23': '500', '24': '500', '1' : '800', '12': '800', '16': '800', '18': '800', '19': '800', '2': '1000', '5': '1000', '9': '1000', '10': '1000', '15' : '1000', '3': '1300', '6' : '1300', '8' : '1300', '21' : '1300', '25' : '1300', '7':'700'}
for row in range(len(fichier)):
    yep += fichier[row].strip()
    ordo = fichier[row][4:8].strip().strip('').replace(' ',"").replace("'","").replace(',','')
    ordonnee.append(ordo)
    absc = fichier[row][2:4]
    abscisse.append(absc)



#print(yep)
#print(ordonnee)
#print(abscisse)
#print(match_absc)
for individu in range(13):
    individus += fichier[individu].strip()
    ordon = fichier[individu][4:9].strip().strip('').replace(' ',"").replace("'","").replace(',','')
    ordonnees.append(ordon)
    abscs = fichier[individu][2:4].replace(' ',"").replace("'","").replace(',','')
    abscisses.append(abscs)

print(ordonnees)
print(abscisses)
print(match_absc)
#x_axis = np.array(abscisses).astype(np.float)
#y_axis = np.array(ordonnees).astype(np.float)
#plt.scatter(x_axis, y_axis)
#plt.xlabel('Poids absolus en gramme')
#plt.ylabel('Poids estimes en gramme')
#plt.title('Poids estimes par les participants en fonction du poids absolu')
#plt.savefig('Precision.png')
#plt.show()
