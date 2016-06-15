library(ggplot2)
data.set <- data.frame(
  Type = c(rep(mtcars$mpg, 2),rep(mtcars$cyl, 2)),
  Comparacion = rep(c('Millas por galón', 'Cilindros'), 2),
  Value = rpois(32, 20)
)

qplot(Type, Value, data = data.set, fill = Comparacion, geom = "area")