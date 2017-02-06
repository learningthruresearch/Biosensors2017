setwd('/Users/ZoubouzoumBouzey/Documents/Bacteruino/bio/2nd/bigassplot2/')

table = read.table("alllm239.csv", header = TRUE)

summary(table)

table[,c('pas','X39')]

#par(mfrow=c(2,1))   #HAVE TO BE ACTIVETED in order to plot every graph differently. 

plot(table[,'pas'], table[,'X39'],main = "3,9 M", pch='*', col=1, xlim = c(0, 149), ylab = 'Abs', xlab = 'Time in unit of 10m' ,ylim = c(-0.0005 , 0.015))
blancall = lm(X39~pas, table)
summary(lm(X39~pas, table))
abline(blancall, lty=4,col = 2)