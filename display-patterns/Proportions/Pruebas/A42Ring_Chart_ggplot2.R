library(ggplot2)
t<-table(mtcars$cyl, mtcars$gear)
x<-as.data.frame(t)
colnames(x)<-c("Cylindres", "Gear","Frequency")
bp <- ggplot(x, aes(x =Cylindres,y=Frequency, fill = Gear)) +
  geom_bar(width = 0.9,  stat = "identity", position="fill") +labs (title="Gear Car's Distribution by Cylindres")
pie <-bp+coord_polar("y", start=0)
pie