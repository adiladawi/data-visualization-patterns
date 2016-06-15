head(mtcars)
library(ggplot2)
ggplot(data=mtcars, aes(x=mtcars$wt, y=mtcars$mpg))+
  geom_line()+
  geom_point()