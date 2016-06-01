library(ggplot2)
g <- ggplot(mtcars, aes(wt, mpg))+geom_point(colour="blue")
g + labs(list(title = "Scatterplots by Milles per Gallon and  Car Weight",  x="Car Weight", y="Miles per Gallon"))
