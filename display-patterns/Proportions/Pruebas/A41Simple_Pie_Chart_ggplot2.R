library(ggplot2)
t<-table(mtcars$cyl)
x<-as.data.frame(t)
colnames(x)<-c("Cylindres", "Frequency")
bp <- ggplot(x, aes(x ="",y=Frequency, fill = Cylindres)) +
  geom_bar(width = 1,  stat = "identity") +labs (title="Proportion Cylindres in a Car Distribution")
pie <-bp+coord_polar("y", start=0)
pie +   geom_text(aes(y = Frequency/3 + c(0, cumsum(Frequency)[-length(Frequency)]), 
                      label = paste(round(Frequency/sum(Frequency) * 100), " %")), size=5)
