from math import *
import matplotlib.pyplot as plt
import csv

ListeFinale=[]

##########################################################
Data = "Test 1.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Test 2.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Test 3.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Test 4.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Test 5.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Test 6.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Test 7.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Test 8.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Test 9.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Test 10.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]
##########################################################
plt.boxplot(ListeFinale)
plt.title("TEST : Euglena orientation angle with the magnetic field for each replicates (based on 30 measurements)")
plt.ylabel("Angle with the magnetic field (in degree)")
plt.xlabel("Number of the replicate")
plt.show()

#plt.xticklabels(['Replicate 1', 'Replicate 2', 'Replicate 3', 'Replicate 4', 'Replicate 5', 'Replicate 6', 'Replicate 7', 'Replicate 8', 'Replicate 9', 'Replicate 10'])