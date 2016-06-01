counts <- table(mtcars$gear)
barplot(counts, main="Car Distribution", xlab="Number of Gears", ylab="Frequency", col="grey")