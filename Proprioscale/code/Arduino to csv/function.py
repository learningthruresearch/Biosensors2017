def Extract(nom):
	a = open(nom, "r")
	ResponseTime = 0
	maxi = 0
	courbe = []
	u = 0

	for i in a:
		courbe.append(float(i))
	output = []
	tic = 0
	toc = 0

	means = []
	ResponseTimes = []
	for i in range(len(courbe)-4):
		if courbe[i] > 30:
			ResponseTime+=100
			if (-courbe[i] + courbe[i+1] + courbe[i+2] - courbe[i-1]) < 5:
				tic += 1
				if tic == 5:
					ResponseTimes.append(ResponseTime - 500)
				output.append(courbe[i])
		else:
			if len(output[2:-2]) != 0:
				u += 1
				mean = sum(output[2:-2])/len(output[2:-2])
				means.append(mean)
				output = []
				toc = 1
				print("------")
			if toc == 1:
				ResponseTime = 0
				tic = 0
				toc = 0
	a = open(nom + ".csv", "w")
	for i in range(len(means)):
		#print(str(means[i]) + "," + str(ResponseTimes[i]))
		a.write(str(means[i]) + "," + str(ResponseTimes[i]) + "\n")
	print(nom)
	print(u)
	return means, ResponseTimes