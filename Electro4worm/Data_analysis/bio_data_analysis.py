import matplotlib.pyplot as plt
import numpy as np


n_groups=3
index = np.arange(n_groups)
barWidth = 0.12
t1=[20,70,20]
r1= range(len(t1))
t2=[30,60,16]
r2=[x + barWidth for x in r1]
t3=[28,45,24]
r3=[x + barWidth for x in r2]
t4=[40,40,20]
r4=[x + 0.22 for x in r3]
t5=[25,36,32]
r5=[x + barWidth for x in r4]
t6=[32,35,24]
r6=[x + barWidth for x in r5]
yerr=[10,10,10,10,10,10,]

temps = ('T1','T2','T3','T4','T5','T6')

a=plt.bar(r1, t1, color = 'cornflowerblue', width = barWidth,yerr=[7,13,7], ecolor = 'black')
b=plt.bar(r2, t2, color = 'greenyellow', width = barWidth,yerr=[7,13,7], ecolor = 'black')
c=plt.bar(r3, t3, color = 'salmon', width = barWidth,yerr=[7,13,7], ecolor = 'black')
d=plt.bar(r4, t4, color = 'midnightblue', width = barWidth,yerr=[7,13,7], ecolor = 'black')
e=plt.bar(r5, t5, color = 'orange', width = barWidth,yerr=[7,13,7], ecolor = 'black')
f=plt.bar(r6, t6, color = 'mediumorchid', width = barWidth,yerr=[7,13,7], ecolor = 'black')


plt.ylim(0,85)
plt.xticks(index + 0.4 ,('Zone A','Zone B','Zone C'))
plt.legend(['BEFORE Electric field N°1','BEFORE Electric field N°2','BEFORE Electric field N°3','AFTER Electric field N°1','AFTER Electric field N°2','AFTER Electric field N°3'], loc='upper right',prop={'size':20})
plt.grid()
plt.show()


