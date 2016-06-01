library(latticeExtra)
panel.piechart <-
  function(x, y, labels = as.character(y),
           edges = 200, radius = 0.8, clockwise = FALSE,
           init.angle = if(clockwise) 90 else 0,
           density = NULL, angle = 45, 
           col = superpose.polygon$col,
           border = superpose.polygon$border,
           lty = superpose.polygon$lty, ...)
  {
    stopifnot(require("gridBase"))
    superpose.polygon <- trellis.par.get("superpose.polygon")
    opar <- par(no.readonly = TRUE)
    on.exit(par(opar))
    if (panel.number() > 1) par(new = TRUE)
    par(fig = gridFIG(), omi = c(0, 0, 0, 0), mai = c(0, 0, 0, 0))
    pie(as.numeric(x), labels = labels, edges = edges, radius = radius,
        clockwise = clockwise, init.angle = init.angle, angle = angle,
        density = density, col = col, border  = border, lty = lty)
  }
piechart <- function(x, data = NULL, panel = "panel.piechart", ...)
{
  ocall <- sys.call(sys.parent())
  ocall[[1]] <- quote(piechart)
  ccall <- match.call()
  ccall$data <- data
  ccall$panel <- panel
  ccall$default.scales <- list(draw = FALSE)
  ccall[[1]] <- quote(lattice::barchart)
  ans <- eval.parent(ccall)
  ans$call <- ocall
  ans
}
t<-table(mtcars$cyl)
colores<-c("pink","green","skyblue")
pct <- round(t/sum(t) * 100)
lbl<-paste(c("4 Cyl","6 Cyl","8 Cyl"), pct, sep =" ")
lbl<-paste(lbl, "%", sep =" ")
par(new = TRUE)
piechart(t, labels=lbl, main="Proportion Cylindres ",col = colores, xlab="")