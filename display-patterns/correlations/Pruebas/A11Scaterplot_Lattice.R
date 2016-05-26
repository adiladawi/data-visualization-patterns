library(lattice)
xyplot(mtcars$mpg~mtcars$wt, 
    main="Scatterplots by Milles per Gallon and  Car Weight", 
    xlab="Car Weight", ylab="Miles per Gallon", pch=19)
