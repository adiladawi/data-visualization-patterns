source('Sankey.R')

mpg=mtcars["Datsun 710",1]
hp=mtcars["Datsun 710",4]
cyl=mtcars["Datsun 710",2]
wt= mtcars["Datsun 710",6]
disp=mtcars["Datsun 710",3]
qsec=mtcars["Datsun 710",7]
gear =mtcars["Datsun 710",10]
inputs = c(mpg,disp)
losses = c(qsec,gear,cyl,hp)
unit = "n ="

labels = c("Miles/(US) gallon",
           "Displacement\n",
           "1/4 mile time",
           "Number of forward gears",
           "Number of cylinders",
           "Datsun 710\nGross HP")

SankeyR(inputs,losses,unit,labels)

# Clean up my mess
rm("inputs", "labels", "losses", "SankeyR", "unit")