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

### Lattice

### ggplot2

    library(ggplot2)
    t<-table(mtcars$cyl, mtcars$gear)
    x<-as.data.frame(t)
    colnames(x)<-c("Cylindres", "Gear","Frequency")
    bp <- ggplot(x, aes(x =Cylindres,y=Frequency, fill = Gear)) +
      geom_bar(width = 0.9,  stat = "identity", position="fill") +labs (title="Gear Car's Distribution by Cylindres")
    pie <-bp+coord_polar("y", start=0)
    pie

![](A42Ring_ChartR_files/figure-markdown_strict/unnamed-chunk-4-1.png)<!-- -->

References
----------
