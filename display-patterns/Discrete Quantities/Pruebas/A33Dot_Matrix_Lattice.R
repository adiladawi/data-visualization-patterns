library(lattice)
dotplot(rownames(mtcars) ~ mpg, data=mtcars, groups=mtcars$cyl, pch=16, main="Gas Milage for Car Models\ngrouped by cylinder",     xlab="Miles per Gallon", auto.key=list(space="top", columns=3, title="Cylindres", cex.title=1))
