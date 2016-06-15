library(ggplot2)

df2 <- mtcars
ggplot(data=df2, aes(x=mpg, y=hp, group=gear)) +
  geom_line()+
  geom_point()