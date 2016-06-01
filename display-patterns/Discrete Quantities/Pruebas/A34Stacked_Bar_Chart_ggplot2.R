library("ggplot2")
g <- ggplot(mtcars, aes(factor(gear), fill=factor(cyl))) + geom_bar( position = "fill")
g + labs(list(title = "Car Distribution by Gears and Cyl", x="Number of Gears", y="Frequency"))