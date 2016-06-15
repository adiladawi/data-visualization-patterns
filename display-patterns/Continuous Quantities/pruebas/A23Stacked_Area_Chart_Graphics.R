source('Continuous Quantities/plot_area.r')
datos<-data.frame(mtcars$cyl,mtcars$mpg)
plot.area(datos,prop=F,horiz=T)