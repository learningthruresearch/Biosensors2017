import csv
import matplotlib.pyplot as plt
import numpy as np
import pylab

#fctn that creates data lists
def lists(condition, line, liste):
    if line[1] == condition:            #delimitates the condition in which the box will be
        for j in range(2,len(line)-1):
            liste.append(line[j])       # puts all the lentil lenghts-values from boxes in the same conditions on the same list
    return liste

#fctn that will parse our document into a list for X file and X condition
def list_condition(nom_fichier, condition):
    dd = open(nom_fichier, 'r')         #opens the file
    data = dd.readlines()               #reads the file
    lista = list()                      #creates a list
    for i in data:
        line = i.split(',')             #converts the string in a lists
        lists(condition, line, lista)   #applicates the first fonction to X conditions
    return lista

print(list_condition("data_debut.csv", "Blue"))
#fctn that will do a sustraction from two lists
def sustraction(nom_fichier_debut, nom_fichier_fin, condition):
    lista_debut = list_condition(nom_fichier_debut, condition)          # liste du debut de l'experience
    lista_fin = list_condition(nom_fichier_fin, condition)              # liste du fin de l'experience
    sustr = [float(m) - float(n) for m,n in zip(lista_fin,lista_debut)] #does the sustraction of our two lists
    return sustr

conditions = ["UV", "Blue", "Green", "Red", "IR"]    #name of the conditions
condssize = ["UV (n=17)", "Blue (n=15)", "Green (n=14)", "Red (n=25)", "IR (n=23)"]    #name of the conditions
data = list()
for i in range(len(conditions)):					 #loop to create a graph for each condition
    b = sustraction('data_debut.csv', 'data_fin.csv', conditions[i]) #final length - initial length of X condition
    c = list()
    for j in b:								 #loop that deletes negative values and add the legnth of other lentils to a list.
        if j >= 0:
            c.append(j)
    data.append(c)							 #adds positive lengths for each condition to a single list

plt.boxplot(data)						   	                        #creates a boxplot for our data
pylab.xticks([1,2,3,4,5], condssize)	                            #changes the x axis fot condition names
plt.ylabel('Lentils growth (cm)')				                        #label x axis
plt.title("Lentils growth compared to different wavelengths")		#boxplot's title
plt.show()								                            #it shows the boxplot
plt.savefig('wavelenghts.png')                                                       #it saves the boxplot

#same process but now done with the controls
controls = ["None", "Sunlight"]
boxnames = ["Negative control (n=13)", "Positive control (n=18)"]
data = list()
for i in range(len(controls)):
    b = sustraction('data_debut.csv', 'data_fin.csv', controls[i])
    c = list()
    for j in b:
        if j >= 0:
            c.append(j)
    data.append(c)
    print(controls[i])
    print(len(c))

plt.boxplot(data)
pylab.xticks([1,2], boxnames)
plt.ylabel('Lentils length')
plt.ylim((0,3))
plt.title("Lentils growth on control situations")
plt.show()
plt.savefig('controls.png')
