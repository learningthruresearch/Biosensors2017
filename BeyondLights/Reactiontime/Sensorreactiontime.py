import matplotlib.pyplot as plt

reaction = [16.92, 15.9, 13.26, 16.0, 15.2, 15.8]
time = [1.5, 2, 3, 3.3, 4, 4.3]
error = [5.2, 4.7, 4.8, 4.2, 4.3, 4.8]

variation = [6, 16.6, 20.1, 5, 4] 

plt.subplot(211)
plt.bar(time, reaction, width = 0.1)
plt.xlabel('Time between light changes(in minutes)')
plt.ylabel('Average Reaction time(in milliseconds)')
plt.title('RGB sensor reaction time according to frequency of light change')
plt.subplot(212)
plt.bar(time[1:6], variation, width = 0.1)
plt.xlabel('Time between light changes(in minutes)')
plt.ylabel('Variation of the reaction time(in %)')
plt.title('RGB sensor reaction time variation according to frequency of light change')

plt.show()
