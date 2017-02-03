import matplotlib.pyplot as plt
fichier = open("data_bio.csv", "r")
file = open("data_bio_replica.csv", "r")
Import_bio = fichier.readlines()
Import_replica = file.readlines()
Abscisse_bio = []
Ordonnee_bio = []
Abscisse_replica = []
Ordonnee_replica = []

for i in range (len(Import_bio)):
    Import_bio[i]=Import_bio[i].strip()
    Import_bio[i]=Import_bio[i].replace(" ","").split(",")
    print(Import_bio[i])
    Abscisse_bio.append(float(Import_bio[i][0]))
    Ordonnee_bio.append(float(Import_bio[i][1]))
print(Abscisse_bio)
print(Ordonnee_bio)
plt.plot(Abscisse_bio,Ordonnee_bio, "cs", markersize=10, label="Measurement of 5 different weights on 12 people")

fichier = open("data_electro.csv", "r")
Import_electro = fichier.readlines()
Abscisse_electro = []
Ordonnee_electro = []
for i in range (len(Import_electro)):
    Import_electro[i]=Import_electro[i].strip()
    Import_electro[i]=Import_electro[i].split(",")
    print(Import_electro[i])
    Abscisse_electro.append(Import_electro[i][0])
    Ordonnee_electro.append(Import_electro[i][1])
print(Abscisse_electro)
print(Ordonnee_electro)
plt.plot(Abscisse_electro, Ordonnee_electro, "mp", markersize=13, label="Measurement of 5 different weights with the Arduino")

#for i in range (len(Import_replica)):
#    Import_replica[i]=Import_replica[i].strip()
#    Import_replica[i]=Import_replica[i].replace(" ","").split(",")
#    print(Import_replica[i])
#    Abscisse_replica.append(float(Import_replica[i][0]))
#    Ordonnee_replica.append(float(Import_replica[i][1]))
#print(Abscisse_replica)
#print(Ordonnee_replica)
#plt.plot(Abscisse_replica,Ordonnee_replica, "go", markersize=10)

list_moyenne = [300, 475, 816, 1099, 1446]
#list_moyenne_replica = [278, 380, 814, 1010, 1484]
list_poids = [300, 500, 800, 1000, 1300]
plt.plot(list_poids, list_moyenne, "yo", markersize=10, label="Mean for the guessed weight for 12 people")
#plt.plot(list_poids, list_moyenne_replica, "yo", markersize=10)

font = {'size'   : 20}
plt.rc('font', **font)
plt.legend(loc="upper left")
plt.xlabel('Real weight in grams')
plt.ylabel('Felt weight in grams')
plt.title('Accuracy of the biological and electronic sensors in function of different masses')
plt.show()
