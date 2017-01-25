import matplotlib.pyplot as plt

time = [2, 3, 3.3, 4, 4.3]
variations = [31,6.4, 41, 2, 63]

plt.bar(time, variations, width = 0.2)
plt.title('variation of reaction time according light switch frequency')
plt.xlabel('time intervalls between light switches(in minutes)')
plt.ylabel('variation of reaction time(in %)')
plt.show()
