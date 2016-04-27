# PYTHON IMPLEMENTATION 


## Data Set


~~~~{.python}
from datos import data
d=data('mtcars')
~~~~~~~~~~~~~




## Dependences

* Matplotlib
* Seaborn
* Pyqtgraph
* Pandas


## Code Example


### Matplotlib


~~~~{.python}
import matplotlib.pyplot as plt
import numpy as np
from datos import data
import pandas

fig, ax = plt.subplots()
ax.axis('equal')
colors =[ 'lightcoral','#66FF66','lightskyblue']
d=data('mtcars')
subset1, subset2, subset3= d[d.cyl==4], d[d.cyl==6], d[d.cyl==8]
ps = pandas.Series([i for i in subset1.gear])
c1 = ps.value_counts()
ps = pandas.Series([i for i in subset2.gear])
c2 = ps.value_counts()
ps = pandas.Series([i for i in subset3.gear])
c3 = ps.value_counts()
ax.pie(c1,  colors=colors,
        autopct='%1.1f%%', startangle=90, radius=1)
ax.pie(c2,   colors=colors,
       autopct='%1.1f%%', startangle=90, radius=0.6)
colors =[ 'lightcoral','lightskyblue']
ax.pie(c3,   colors=colors,
       autopct='%1.1f%%', startangle=90, radius=0.3)
plt.title("Gear Car's Distribution by Cylindres", size=18)
plt.legend(['3 Gear', '4 Gear', '5 Gear'], frameon=False, loc=4)
plt.show()
~~~~~~~~~~~~~

![](figures/A42Ring_ChartPy_figure2_1.png)\



### Seaborn




### Pyqtgraph




### References