setwd('/Users/ZoubouzoumBouzey/Documents/Bacteruino/bio/2nd/bigassplot2/')

table = read.table("allboxrs.csv", header = TRUE)

summary(table)

table[,c('C','rs')]
plot(table[,'C'], table[,'rs'], main = "R squared", xlab = "Concentration", ylab = "R squard ")
