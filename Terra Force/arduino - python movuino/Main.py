import sys
import time
import numpy as np
import OSC_communication as osc
import math
import pickle

import csv
c = csv.writer(open("results_centre5.csv", "wb"))
c.writerow(["ax", "ay", "az", "gx", "gy", "gz"])

fichier = open("donnees.txt", 'wb')

def main(args = None):
	# Start OSC server (to receive message)
	print "Starting OSCServer"
	osc_server = osc.OSCserver('192.168.0.102', 7400) # Init the OSC server with YOUR IP and use the same port number as the sender (here Movuino on port 7400)
	osc_server.addListener("movuinOSC") # add listener on address "movuinOSC"
	time.sleep(0.1)

	

	timer0 = time.time()
	timer1 = timer0
	while (timer1-timer0 < 10):
		timer1 = time.time()
		time.sleep(0.05)

		# RECEIVE MOVUINO DATA
		curAddr, curVal = osc_server.get_CurrentMessage() # extract address and values of current message
		if curAddr == "movuinOSC" :
			ax = float(curVal[0])
			ay = float(curVal[1])
			az = float(curVal[2])
			gx = float(curVal[3])
			gy = float(curVal[4])
			gz = float(curVal[5])

			print ax, ay, az, gx, gy, gz
			c.writerow([ax, ay, az, gx, gy, gz])

			mon_pickler = pickle.Pickler(fichier)
			mon_pickler.dump(ax)

	osc_server.closeServer() # ERROR MESSAGE but close the OSC server without killing the app

if __name__ == '__main__':
	sys.exit(main())

