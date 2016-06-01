library(ggplot2)
g<-ggplot(mtcars, aes(x = mpg, fill = factor(cyl)))
g+geom_dotplot(stackgroups = TRUE, binwidth = 1.5, binpositions = "all", method="histodot")