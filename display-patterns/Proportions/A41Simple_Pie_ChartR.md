R IMPLEMENTATION
================

R is a language and environment for statistical computing and graphics.
It is a GNU project which is similar to the S language and environment
which was developed at Bell Laboratories (formerly AT&T, now Lucent
Technologies) by John Chambers and colleagues. R provides a wide variety
of statistical (linear and nonlinear modelling, classical statistical
tests, time-series analysis, classification, clustering, …) and
graphical techniques, and is highly extensible (The R Fundation,
2016)[^1].

Data Set
--------

For this proyect it was use the dataset mtcars. This data was extracted
from the 1974 Motor Trend US magazine, and comprises fuel consumption
and 10 aspects of automobile design and performance for 32 automobiles
(1973–74 models).

    table(mtcars$cyl)

    ## 
    ##  4  6  8 
    ## 11  7 14

Dependences
-----------

-   **Graphics**. This package contains functions for **base graphics**.
    Base graphics are traditional S-like graphics, as opposed to the
    more recent grid graphics(R Core Team,s.f. )[^2].
-   **Lattice**. Is an implementation of Trellis graphics for R. It is a
    powerful and elegant high-level data visualization system with an
    emphasis on multivariate data. It is designed to meet most typical
    graphics needs with minimal tuning, but can also be easily extended
    to handle most nonstandard requirements (Sarkar, 2011)[^3]
-   **ggplot2**. Is a plotting system for R, based on the grammar of
    graphics, which tries to take the good parts of base and lattice
    graphics and none of the bad parts. It takes care of many of the
    fiddly details that make plotting a hassle (like drawing legends) as
    well as providing a powerful model of graphics that makes it easy to
    produce complex multi-layered graphics(Wickham, 2013)[^4].

Code Example
------------

### Graphics

    t<-table(mtcars$cyl)
    colores<-c("pink","green","skyblue")
    pct <- round(t/sum(t) * 100)
    lbl<-paste(c("4 Cyl","6 Cyl","8 Cyl"), pct, sep =" ")
    lbl<-paste(lbl, "%", sep =" ")
    pie(x=t,labels=lbl, col = colores, radius = 1, main="Proportion Cylindres in a Car Distribution", cex=1)

![](A41Simple_Pie_ChartR_files/figure-markdown_strict/unnamed-chunk-2-1.png)


For a complete list of functions with individual help pages, use library
(help = "graphics")(R Core Team,s.f. )[^2].

The online documentation is also available at
[docs.Graphics](https://stat.ethz.ch/R-manual/R-devel/library/graphics/html/00Index.html)

### Lattice

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

![](A41Simple_Pie_ChartR_files/figure-markdown_strict/unnamed-chunk-3-1.png)


The complete online documentation is also available in the form of a
single
[PDF](https://cran.r-project.org/web/packages/lattice/lattice.pdf) file
at CRAN.

From within R, type:

> help(Lattice)

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

![](A41Simple_Pie_ChartR_files/figure-markdown_strict/unnamed-chunk-4-1.png)


The ggplot2 documentation is available at
[docs.ggplot2.org](http://docs.ggplot2.org/current/)

References
----------

[^1]: The R Fundation. (s.f). R.Consultado el 3 de marzo, 2016 en
<https://www.r-project.org/about.html>.

[^2]: R Core Team. (s.f). The R Graphics Package. Consultado el 3 de
marzo, 2016 en
<https://stat.ethz.ch/R-manual/R-devel/library/graphics/html/graphics-package.html>.

[^3]: Sarkar, Deepayan. (2011). Lattice: trellis graphics for R.
Consultado el 4 de marzo, 2016 en
<http://lattice.r-forge.r-project.org/>

[^4]: Wickham, Hadley. (2013). ggplot2. Consultado el 4 de marzo, 2016 en
<http://ggplot2.org/>
