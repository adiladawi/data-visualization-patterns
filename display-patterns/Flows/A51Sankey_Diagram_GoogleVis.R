require(googleVis)
mpg=mtcars["Datsun 710",1]
hp=mtcars["Datsun 710",4]
cyl=mtcars["Datsun 710",2]
wt= mtcars["Datsun 710",6]
disp=mtcars["Datsun 710",3]
qsec=mtcars["Datsun 710",7]
gear =mtcars["Datsun 710",10]
dat <- data.frame(From=c(rep("Miles/(US) gallon",4), rep("Displacement", 4)),
                  To=c(rep(c("1/4 mile time",
                             "Number of forward gears",
                             "Number of cylinders",
                             "Datsun 710 Gross horsepower"))),
                  Weight=c(mpg,gear,cyl,hp))

sk1 <- gvisSankey(dat, from="From", to="To", weight="Weight")
plot(sk1)