R IMPLEMENTATION
================

Data Set
--------

    table(mtcars$cyl)

    ## 
    ##  4  6  8 
    ## 11  7 14

Dependences
-----------

-   lattice
-   ggplot2

Code Example
------------

### Graphics

    t<-table(mtcars$cyl)
    colores<-c("pink","green","skyblue")
    pct <- round(t/sum(t) * 100)
    lbl<-paste(c("4 Cyl","6 Cyl","8 Cyl"), pct, sep =" ")
    lbl<-paste(lbl, "%", sep =" ")
    pie(x=t,labels=lbl, col = colores, radius = 1, main="Proportion Cylindres in a Car Distribution", cex=1)

![](A41Simple_Pie_ChartR_files/figure-markdown_strict/unnamed-chunk-2-1.png)<!-- -->

### Lattice

	library(latticeExtra)
	panel.piechart <- function(x, y, labels = as.character(y),
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

![](A41Simple_Pie_ChartR_files/figure-markdown_strict/unnamed-chunk-3-1.png)<!-- -->

### ggplot2

    library(ggplot2)
    t<-table(mtcars$cyl)
    x<-as.data.frame(t)
    colnames(x)<-c("Cylindres", "Frequency")
    bp <- ggplot(x, aes(x ="",y=Frequency, fill = Cylindres)) +
    geom_bar(width = 1,  stat = "identity") +labs (title="Proportion Cylindres in a Car Distribution")
    pie <-bp+coord_polar("y", start=0)
    pie +   geom_text(aes(y = Frequency/3 + c(0, cumsum(Frequency)[-length(Frequency)]), 
                          label = paste(round(Frequency/sum(Frequency) * 100), " %")), size=5)

![](A41Simple_Pie_ChartR_files/figure-markdown_strict/unnamed-chunk-4-1.png)<!-- -->

References
----------
