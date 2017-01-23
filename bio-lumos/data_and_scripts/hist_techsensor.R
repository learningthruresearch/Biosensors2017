mean1 <- c(29.601970586104475, 31.978474823230744, 33.05471168094102, 34.27997403098735)
green <- c(70, 80, 90, 100)
barplot(mean1, width = 1, col= "orange",  main="Color detection by TSC3200", xlab =" 605nm             607nm             608nm            610nm", ylab ="% of difference compared to black screen", ylim = c(0, 100))
