counts <- table(mtcars$cyl, mtcars$gear)
barplot(counts, main="Car Distribution by Gears and Cyl",
	xlab="Number of Gears", ylab="Frequency", col=c("darkblue","red"), legend = rownames(counts), beside=TRUE)