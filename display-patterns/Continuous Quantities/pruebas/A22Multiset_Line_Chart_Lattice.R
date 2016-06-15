library(lattice)
L = mtcars$am == 0 
Camaro=mtcars["Camaro Z28",]
Datsun=mtcars["Datsun 710",]
x= 1:11
df <- data.frame(Camaro = Camaro, Datsun = Datsun, x = x)

## Warning in data.frame(Camaro = Camaro, Datsun = Datsun, x = x): row names
## were found from a short variable and have been discarded

xyplot(Camaro + Datsun  ~ x, data = df, type = "o", auto.key=TRUE)