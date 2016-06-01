x <- mtcars 
x$cyl <- factor(x$cyl)
x$color[x$cyl==4] <- "red"
x$color[x$cyl==6] <- "blue"
x$color[x$cyl==8] <- "darkgreen"	
dotchart(x$mpg,labels=row.names(mtcars),ylim=c(0, 1.00), pch=16,
         main="Gas Milage for Car Models\ngrouped by cylinder",
         xlab="Miles per Gallon", gcolor="black", color=x$color)
legend("bottomright", legend = c("4", "6", "8"),
       col = c("red","blue","darkgreen"), pch = 16, title="Cylindres")
