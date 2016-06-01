library("lattice")
counts <- table(mtcars$gear)
barchart(counts, main="Car Distribution", xlab="Number of Gears",ylab="Frequency", horizontal="false", col="grey")