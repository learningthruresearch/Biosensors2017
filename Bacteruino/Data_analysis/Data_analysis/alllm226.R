setwd('/Users/ZoubouzoumBouzey/Documents/Bacteruino/bio/2nd/bigassplot2/')

table = read.table("alllm226.csv", header = TRUE)

summary(table)

table[,c('pas','X26')]

#par(mfrow=c(2,1))   #HAVE TO BE ACTIVETED in order to plot every graph differently. 

plot(table[,'pas'], table[,'X26'],main = "0,1 M", pch='*', col=1, xlim = c(0, 149), ylab = 'Abs', xlab = 'Time in unit of 10m' ,ylim = c(-0.0005 , 0.015))
blancall = lm(X26~pas, table)
summary(lm(X26~pas, table))
abline(blancall, lty=4,col = 2)
