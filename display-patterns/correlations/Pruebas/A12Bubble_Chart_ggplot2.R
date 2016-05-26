library (ggplot2)
g <- ggplot(mtcars, aes(wt, mpg, size = cyl))+geom_point(colour="blue") + scale_size_continuous(range=c(6,10))
g + labs(list(title = "Bubble Chart by Milles per Gallon and  Car Weight",  x="Car Weight", y="Miles per Gallon"))
