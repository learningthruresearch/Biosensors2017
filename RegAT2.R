#--------------------------------------------------------------------
#            Final Projet Biosensors - DrosoblueZ
#         Franck.P        Francois.S        Armelle.S


setwd('/Users/ZoubouzoumBouzey/Documents/biosensor_final/data/')
# Searching for the right source folder

table = read.table("t2.csv", header = TRUE)
# Associate the file "soin2.csv" to the variable 'table'

summary(table)
# Check if everything is alright

table[,c('pas'
         ,'a1','a2','a3','a4','a5','a6','a7','a8','a9','a10'
         ,'b1','b2','b3','b4','b5','b6','b7','b8','b9','b10'
         ,'c1','c2','c3','c4','c5','c6','c7','c8','c9','c10'
         ,'d1','d2','d3','d4','d5','d6','d7','d8','d9','d10')]
# Rename proprely the columun for the calling later in the plot

plot(print(cumsum(table$a1))~table$pas
     # Plot the data by calling the variable in wich they are
     , type='l', col=1
     # Give the type of line and color
     , xlim = c(1, 7), ylim = c(15, 50)
     # Limits given to the axis 
     , main = 'Cumulative curve of tube A at T2', xlab = 'Time in unite of 0,5 sec', ylab = 'Distance in mm')
     # Label the plot
ca1 = lm((cumsum(table$a1))~pas, table)
# Creat a variable in which we stock the cumulative data for each tube of fly
abline(ca1, lty=4, col = 1)
# Plot the cumulative curve
par(new=T)# orderd to plot on the same layer the next plot.


plot(print(cumsum(table$a2))~table$pas, type='l', col=2, xlim = c(1, 7), ylim = c(15, 50), xlab='', ylab = ' ')
ca2 = lm((cumsum(table$a2))~pas, table)
abline(ca2, lty=4, col = 2)
par(new=T)
plot(print(cumsum(table$a3))~table$pas, type='l', col=3, xlim = c(1, 7), ylim = c(15, 50), xlab='', ylab = '')
ca3 = lm((cumsum(table$a3))~pas, table)
abline(ca3, lty=4, col = 3)
par(new=T)
plot(print(cumsum(table$a4))~table$pas, type='l', col=1, xlim = c(1, 7), ylim = c(15, 50), xlab='', ylab = '')
ca4 = lm((cumsum(table$a4))~pas, table)
abline(ca4, lty=4, col = 1)
par(new=T)
plot(print(cumsum(table$a5))~table$pas, type='l', col=2, xlim = c(1, 7), ylim = c(15, 50), xlab='', ylab = '')
ca5 = lm((cumsum(table$a5))~pas, table)
abline(ca5, lty=4, col = 2)
par(new=T)
plot(print(cumsum(table$a6))~table$pas, type='l', col=3, xlim = c(1, 7), ylim = c(15, 50), xlab='', ylab = '')
ca6 = lm((cumsum(table$a6))~pas, table)
abline(ca6, lty=4, col = 3)
par(new=T) 
plot(print(cumsum(table$a7))~table$pas, type='l', col=1, xlim = c(1, 7), ylim = c(15, 50), xlab='', ylab = '')
ca7 = lm((cumsum(table$a7))~pas, table)
abline(ca7, lty=4, col = 1)
par(new=T)
plot(print(cumsum(table$a8))~table$pas, type='l', col=2, xlim = c(1, 7), ylim = c(15, 50), xlab='', ylab = '')
ca8 = lm((cumsum(table$a8))~pas, table)
abline(ca8, lty=4, col = 2)
par(new=T)
plot(print(cumsum(table$a9))~table$pas, type='l', col=3, xlim = c(1, 7), ylim = c(15, 50), xlab='', ylab = '')
ca9 = lm((cumsum(table$a9))~pas, table)
abline(ca9, lty=4, col = 3)
par(new=T)
plot(print(cumsum(table$a10))~table$pas, type='l', col=3, xlim = c(1, 7), ylim = c(15, 50), xlab='', ylab = '')
ca10 = lm((cumsum(table$a10))~pas, table)
abline(ca9, lty=4, col = 3)

legend(1, 50, legend=c("Cummulative curve","linear regression"),
       col=c("black","black")
       , lty = 1:4)
