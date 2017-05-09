#--------------------------------------------------------------------
#            Final Projet Biosensors - DrosoblueZ
#         Franck.P        Francois.S        Armelle.S



setwd('/Users/ZoubouzoumBouzey/Documents/biosensor_final/data/')
#Searching for the right source folder

table = read.table("soin2.csv", header = TRUE)
# Associate the file "soin2.csv" to the variable 'table'

summary(table) #Check if everything is alright
table[,c('t','reg','pas1','reg1','pas2','reg2')]
#rename proprely the columun for the calling later in the plot


plot(table[,'t'], table[,'reg']
     # data to plot 
     , col=2
     # Color for the plot
     , main = 'Speed of the fly in function of the temperature'
     # Main title
     , ylab = 'Speed of the fly in mm/sec'
     # Label for the y axis
     , xlab = 'Temperature in Celsius'
     # Label for the x axis
     , xlim = c(0, 31)
     # Limits given to the x axis 
     , ylim = c(0, 17))
     # Limits given to the y axis 
par(new=T) # orderd to plot on the same layer the next plot.

plot(table[,'pas1'], table[,'reg1']
     , col=3
     , main = 'Speed of the fly in function of the temperature'
     , ylab = 'Speed of the fly in mm/sec'
     , xlab = 'Temperature in Celsius'
     , xlim = c(0, 31)
     , ylim = c(0, 17))
par(new=T)

plot(table[,'pas2'], table[,'reg2']
     , col=4
     , main = 'Speed of the fly in function of the temperature'
     , ylab = 'Speed of the fly in mm/sec'
     , xlab = 'Temperature in Celsius'
     , xlim = c(0, 31)
     , ylim = c(0, 17))

legend(0, 17, legend=c("One single fly"),
       col=c("black")
       , pch = 19)
