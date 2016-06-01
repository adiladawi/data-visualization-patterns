library(lattice)
x<-subset(mtcars, mtcars$cyl==4)
x<-range(x$mpg)
y<-subset(mtcars, mtcars$cyl==6)
y<-range(y$mpg)
z<-subset(mtcars, mtcars$cyl==8)
z<-range(z$mpg)
df<-data.frame(cyl=c(4,6,8),from=c(x[1],y[1],z[1]), to=c(x[2],y[2],z[2]))
xyplot( to  ~ cyl + from, df, ylim = c(0, 35), xlim=c(2, 10), border='transparent', 
        main="Range of Milles per Gallon (mpg) by Cylindres (cyl)", xlab="Milles Per Galllon",ylab="Cylindres",
       panel = function(x, y, subscripts, groups,...){
         panel.barchart(y = y[subscripts], 
                    x = x[subscripts[groups=="cyl"]],  horizontal=FALSE, col="blue",box.width=1,
                    ...)
         panel.barchart(y = x[subscripts[groups=="from"]], 
                        x = x[subscripts[groups=="cyl"]],  horizontal=FALSE, col = "white", box.width=1,
                        ...)
       })
