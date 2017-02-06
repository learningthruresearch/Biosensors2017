setwd('/Users/ZoubouzoumBouzey/Documents/Bacteruino/bio/2nd/bigassplot2/')

table = read.table("alllm251.csv", header = TRUE)

summary(table)

table[,c('pas','X51')]

#par(mfrow=c(2,1))   #HAVE TO BE ACTIVETED in order to plot every graph differently. 

plot(table[,'pas'], table[,'X51'],main = "5,1 M", pch='*', col=1, xlim = c(0, 149), ylab = 'Abs', xlab = 'Time in unit of 10m' ,ylim = c(-0.0005 , 0.015))
blancall = lm(X51~pas, table)
summary(lm(X51~pas, table))
abline(blancall, lty=4,col = 2)
