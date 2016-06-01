x<-subset(mtcars, mtcars$cyl==4)
x<-range(x$mpg)
y<-subset(mtcars, mtcars$cyl==6)
y<-range(y$mpg)
z<-subset(mtcars, mtcars$cyl==8)
z<-range(z$mpg)
df<-data.frame(cyl=c(4,6,8),from=c(x[1],y[1],z[1]), to=c(x[2],y[2],z[2]))
barplot(df$to, border='transparent', space=1, col='blue')
barplot(df$from, space=1, add=TRUE, col='white', 
        border='transparent', names.arg=df$cyl, 
        cex.names=0.8, main="Range of Milles per Gallon (mpg) by Cylindres (cyl)", xlab="Milles Per Gallon", ylab="Cylindres")
box(bty='l')
