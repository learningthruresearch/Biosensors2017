from math import *
import matplotlib.pyplot as plt
import csv

ListeFinale=[]

##########################################################
Data = "Control 1.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Control 2.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Control 3.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Control 4.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Control 5.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Control 6.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Control 7.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Control 8.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Control 9.csv"
File = open(Data,'r')
Test = csv.reader(File)
Angle = []
for Boucle in Test:
    Angle += [Boucle[5]]
Angle = Angle[1:]
for Rang in range(len(Angle)):
    Angle[Rang]=float(Angle[Rang])
ListeFinale+=[Angle]

Data = "Control 10.csv"
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
plt.title(" CONTROL : Euglena orientation angle with the magnetic field for each replicates (based on 30 measurements)")
plt.ylabel("Angle with the magnetic field (in degree)")
plt.xlabel("Number of the replicate")
plt.show()
