d <- table(mtcars$gear, mtcars$cyl)
data<-as.data.frame(d)
names(data)<-c("Gears","Cylindres","Frequency")
data$Gears
library(latticeExtra)
cloud(Frequency~Gears+Cylindres, data, panel.3d.cloud=panel.3dbars, col.facet='grey', 
      xbase=0.4, ybase=0.4, scales=list(arrows=FALSE, col=1), main="Car Distribution by Gears and Cyl", 
      par.settings = list(axis.line = list(col = "transparent")))
