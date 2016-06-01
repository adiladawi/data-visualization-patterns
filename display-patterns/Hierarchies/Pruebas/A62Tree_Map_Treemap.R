library(treemap)
treemap(mtcars,
index=c("cyl", "gear"),
vSize="cyl", title="Tree Map by Cylindres and Gear")