library("ggplot2")
g <- ggplot(mtcars, aes(gear)) + geom_bar(fill = "gray", colour = "green", , binwidth = 0.5)
g + labs(list(title = "Car Distribution", x="Number of Gears", y="Frequency"))
