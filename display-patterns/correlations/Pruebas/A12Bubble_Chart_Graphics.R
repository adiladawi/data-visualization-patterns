radius <- sqrt( mtcars$cyl/ pi )
symbols(mtcars$wt,mtcars$mpg, circles=radius,inches=0.17, fg="blue", bg="blue", xlab="Car Weight", ylab="Miles per Gallon", main="Bubble Chart by Milles per Gallon and  Car Weight")
legend("topright", legend=c(4,6,8), col="blue",title = "cyl", pch=16, cex= 1.8, pt.cex=3:5)
