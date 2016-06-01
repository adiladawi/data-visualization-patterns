library(lattice)
panel.spline <- function(x, y) {
  panel.xyplot(x, y) 
  panel.loess(x, y) 
}
attach(mtcars)
xyplot(mpg~wt, scales=list(cex=2, col="red"),
       panel=panel.spline)