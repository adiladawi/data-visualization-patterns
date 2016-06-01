library("lattice")
counts <- table(mtcars$gear, mtcars$cyl)
barchart(counts, stack = FALSE, horizontal="false", main="Car Distribution by Gears 	and Cyl",     xlab="Number of Gears", ylab="Frequency",
	auto.key = list(space="top", columns=3, title="Cyl", cex.title=1))