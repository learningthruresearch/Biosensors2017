setwd('/Users/ZoubouzoumBouzey/Documents/Bacteruino/bio/2nd/bigassplot2/')

table = read.table("gg.csv", header = TRUE)

table[,c('c','lm')]

summary(table)


#Group=rep(1:2,each=8)

#table=cbind(table,Group)

table[,c('c','lm')]

boxplot(lm~c, data = table)

#, main = "Box of all coefficient of every linear regression of each well at each concentration", col= c("yellow","green"),names = c("4.3","5.1"), xlab = "Concentration",ylab = "Coefficient of linear regression")
