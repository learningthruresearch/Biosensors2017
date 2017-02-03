from function import Extract

bottle = [i for i in range(1, 26)]
match = {4 : 300, 11: 300, 13: 300, 17: 300, 20: 300, 7 : 500, 14 : 500, 22: 500, 23: 500, 24: 500, 1 : 800, 12: 800, 16: 800, 18: 800, 19: 800, 2: 1000, 5: 1000, 9: 1000, 10: 1000, 15 : 1000, 3: 1300, 6 : 1300, 8 : 1300, 21 : 1300, 25 : 1300}

#arduino

a = open("arduino.csv", "w")
for bot in bottle:
	try:
		mean, ResponseTime = Extract("data" + str(bot))
	except:
		print("error")
	weights = [match[bot] for i in range(len(mean))]
	toplot = (mean[1] * 1000 )/ mean[0]
	#plt.plot(match[bot], toplot, "o", color="green")
	a.write(str(bot) + "," + str(ResponseTime[1]) + "," + str(toplot) + "\n")

a.close()