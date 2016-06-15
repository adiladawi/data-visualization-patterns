carb <- mtcars$carb
cyl <- mtcars$cyl

plot(carb, type="o", col="blue", ylim=c(0,10))

lines(cyl, type="o", pch=22, lty=2, col="red")

title(main="Mtcars", col.main="Blue", font.main=4)