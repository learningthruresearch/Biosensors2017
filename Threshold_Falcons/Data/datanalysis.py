import csv
import matplotlib.pyplot as plt
import numpy as np

#fctn that creates data lists
def lists(condition, line, liste):
    if line[1] == condition:            #delimitates the condition in which the box will be
        for j in range(2,len(line)-1):
            liste.append(line[j])       # puts all the lentil lenghts-values from boxes in the same conditions on the same list
    return liste

#fctn that will parse our document into a list for X file (LOL) and X condition
def list_condition(nom_fichier, condition):
    dd = open(nom_fichier, 'r')         #opens the file
    data = dd.readlines()               #reads the file
    lista = list()                      #creates a list
    for i in data:
        line = i.split(',')             #converts the string in a lists
        lists(condition, line, lista)   #applicates the first fonction to X conditions
    return lista

#fctn that will do a sustraction from two lists
def sustraction(nom_fichier_debut, nom_fichier_fin, condition):
    lista_debut = list_condition(nom_fichier_debut, condition)          # liste du debut de l'experience
    lista_fin = list_condition(nom_fichier_fin, condition)              # liste du fin de l'experience
    sustr = [float(m) - float(n) for m,n in zip(lista_fin,lista_debut)] #does the sustraction of our two lists
    return sustr

#fctn that allows to compare a list with the "None" condition values
def comp(nom_fichier_debut, nom_fichier_fin, condition):
    lista = list_condition(nom_fichier_debut, condition)                 #initial list of the condition we want to NORMALIZE
    lista = [float(i) for i in lista]                                    #Convert list of str to a list of float
    sustr = sustraction(nom_fichier_debut, nom_fichier_fin, condition)   #difference that we want to NORMALIZE
    sustrNone = sustraction(nom_fichier_debut, nom_fichier_fin, "None")  #list of condition "None"
    sustrNone = [float(i) for i in sustrNone]                            #Convert list of str to a list of float
    moyennenone = (sum(sustrNone) / len(sustrNone))                      #"None" values' mean
    difference = [i - moyennenone for i in sustr]                        #difference between our list values and "None" mean
    final = [(difference[i] / lista[i]) for i in range(0,len(lista))]    #division between this difference and lentils' initial lenght
    return final

print(comp('data_debut.csv', 'data_fin_fake2.csv', "Sunlight"))
a = sustraction('data_debut.csv', 'data_fin_fake2.csv', "Sunlight")
b = sustraction('data_debut.csv', 'data_fin_fake2.csv', "None")
amoy = (sum(a) / len(a))
bmoy = (sum(b) / len(b))
totmoy = [amoy, bmoy]
c = list()
d = list()
for i in a:
    c.append(1)
for i in b:
    d.append(2)

plt.xlabel('Wavelength')
plt.scatter(c, a, alpha=0.75, facecolor='blue', marker='x')
plt.scatter(d, b, alpha=0.75, facecolor='blue', marker='x')
plt.ylabel('Lentils length')
plt.title("Cucurutxu")
listacaca = [1, 2]
plt.scatter(listacaca, totmoy, alpha=0.75, facecolor='black', s=500, marker='_')
plt.show()

#plt.plot(c, a, 'o')
#plt.plot(d, b, 'o')
#plt.show()
