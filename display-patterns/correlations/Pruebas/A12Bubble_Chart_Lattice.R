library(lattice)
xyplot(mtcars$mpg~mtcars$wt, aspect = 2/3,
       grid = TRUE,
       cex = sqrt( mtcars$cyl/ pi )*2.3, fill.color = rep("blue",40), 
       col = "blue",main="Bubble Chart by Milles per Gallon and  Car Weight", 
       xlab="Car Weight", ylab="Miles per Gallon",
       panel = function(x, y, ..., cex, fill.color, subscripts) {
         panel.xyplot(x, y, cex = cex[subscripts],
                      pch = 21, fill = fill.color[subscripts], ...)
       })