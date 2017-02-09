from math import *
import matplotlib.pyplot as plt
import csv

ListeFinale=[]

##########################################################

Data = "Results Guppy 1 Mercredi.csv"
File = open(Data,'r')
Test = csv.reader(File)
for Boucle in Test:
	ListeFinale+=[Boucle]
ListeFinale=ListeFinale[1:]
for i in range(len(ListeFinale)):
	ListeFinale[i]=ListeFinale[i][1:]
	for j in range(len(ListeFinale[i])):
		ListeFinale[i][j]=float(ListeFinale[i][j])
Histo=[0,0,0,0,0,0,0,0]
for Valeur in ListeFinale:
	for i in range(len(Valeur)):
		Histo[i]+=Valeur[i]
for i in range(len(Histo)):
	Histo[i]=Histo[i]/5
X=[]
for t in range(8):
	X+=[t]
plt.bar(X, Histo, 1, color=['r','g','b','grey','r','g','b','grey'])

ListeFinale=[]
Data = "Results Guppy 2 Mercredi.csv"
File = open(Data,'r')
Test = csv.reader(File)
for Boucle in Test:
	ListeFinale+=[Boucle]
ListeFinale=ListeFinale[1:]
for i in range(len(ListeFinale)):
	ListeFinale[i]=ListeFinale[i][1:]
	for j in range(len(ListeFinale[i])):
		ListeFinale[i][j]=float(ListeFinale[i][j])
Histo2=[0,0,0,0,0,0,0,0]
for Valeur in ListeFinale:
	for i in range(len(Valeur)):
		Histo2[i]+=Valeur[i]
for i in range(len(Histo2)):
	Histo2[i]=Histo2[i]/5
X2=[]
for t in range(9,17):
	X2+=[t]
plt.bar(X2, Histo2, 1, color=['r','g','b','grey','r','g','b','grey'])

ListeFinale=[]
Data = "Results Guppy 3 Mercredi.csv"
File = open(Data,'r')
Test = csv.reader(File)
for Boucle in Test:
	ListeFinale+=[Boucle]
ListeFinale=ListeFinale[1:]
for i in range(len(ListeFinale)):
	ListeFinale[i]=ListeFinale[i][1:]
	for j in range(len(ListeFinale[i])):
		ListeFinale[i][j]=float(ListeFinale[i][j])
Histo3=[0,0,0,0,0,0,0,0]
for Valeur in ListeFinale:
	for i in range(len(Valeur)):
		Histo3[i]+=Valeur[i]
for i in range(len(Histo3)):
	Histo3[i]=Histo3[i]/5
X3=[]
for t in range(18,26):
	X3+=[t]
plt.bar(X3, Histo3, 1, color=['r','g','b','grey','r','g','b','grey'])

ListeFinale=[]
Data = "Results Guppy 4 (mâle) Mercredi.csv"
File = open(Data,'r')
Test = csv.reader(File)
for Boucle in Test:
	ListeFinale+=[Boucle]
ListeFinale=ListeFinale[1:]
for i in range(len(ListeFinale)):
	ListeFinale[i]=ListeFinale[i][1:]
	for j in range(len(ListeFinale[i])):
		ListeFinale[i][j]=float(ListeFinale[i][j])
Histo4=[0,0,0,0,0,0,0,0]
for Valeur in ListeFinale:
	for i in range(len(Valeur)):
		Histo4[i]+=Valeur[i]
for i in range(len(Histo4)):
	Histo4[i]=Histo4[i]/5
X4=[]
for t in range(27,35):
	X4+=[t]
plt.bar(X4, Histo4, 1, color=['r','g','b','grey','r','g','b','grey'])

##########################################################

plt.xlabel('Numéro du Guppy')
plt.ylabel('Temps passé dans une zone (en secondes)')
plt.grid(True)
plt.show()
