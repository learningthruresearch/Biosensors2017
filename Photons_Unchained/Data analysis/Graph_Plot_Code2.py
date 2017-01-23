import matplotlib.pyplot as plt

Organism = [-1,
-2,
0,
1,
0,
-1,
0,
0]
Light = [30,
            60,
            90,
            120,
            150,
            180,
            210,
            240]

plt.plot(Light, Organism, 'yo')

plt.xlabel('Intensity of Light')

plt.ylabel('Differential population (on a 20 seconds interval)')

plt.title('Light intensity')

plt.legend('1 2 3 4 ', 'center right')

plt.axis([0, 300, -4, 6])
#sets a chosen axis

plt.grid(True)
#creates a grid on the graph

plt.show
