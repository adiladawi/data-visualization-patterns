# PYTHON IMPLEMENTATION 


## Data Set


~~~~{.python}
from datos import data
d=data('mtcars')
d.head()
~~~~~~~~~~~~~




## Dependences

* Matplotlib
* Seaborn
* Pyqtgraph
* Pandas


## Code Example


### Matplotlib


~~~~{.python}
import numpy as np
import matplotlib.pyplot as plt
from datos import data
import pandas

d=data('mtcars')
t1 = d.pivot_table( values = 'carb',index=['cyl'], columns = ['gear'],
aggfunc = len)
bar_width = 0.15
opacity = 0.4
rects1 = plt.bar(t1.columns, t1.values[0], bar_width,
alpha=opacity,color='g')
rects2 = plt.bar(t1.columns + bar_width, t1.values[1], bar_width,
alpha=opacity, color='r')
rects3 = plt.bar(t1.columns +2* bar_width, t1.values[2], bar_width,
alpha=opacity, color='y')
plt.xlabel('Number of Gears')
plt.ylabel('Frequency')
plt.title('Car Distribution by Gear and Cylindres')
plt.legend(t1.index, title='Cylindres')
plt.show()
~~~~~~~~~~~~~

![](figures/32Multiset_Bar_ChartPy_figure2_1.png){width=12 cm}



### Seaborn


~~~~{.python}
import seaborn as sns
import matplotlib.pyplot as plt
from datos import data
import pandas

sns.set(style="whitegrid")
d=data('mtcars')
g = sns.factorplot("gear",hue="cyl", data=d,size=6, kind="count")
g.set_axis_labels( "Number of Gears", "Frequency")
plt.title('Car Distribution by Gear and Cylindres', family='Serif',
size=16)
plt.show()
~~~~~~~~~~~~~

![](figures/32Multiset_Bar_ChartPy_figure3_1.png){width=12 cm}



### Pyqtgraph


~~~~{.python}
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import numpy as np
from datos import data
import pandas

d=data('mtcars')
t1 = d.pivot_table( values = 'carb',index=['cyl'], columns = ['gear'],
aggfunc = len)
bar_width = 0.25
win = pg.plot(title='Simple Bar Chart')
bg1 = pg.BarGraphItem(x=t1.columns, height=t1.values[0],
width=bar_width, brush='g')
bg2 = pg.BarGraphItem(x=t1.columns+bar_width, height=t1.values[1],
width=bar_width, brush='r')
bg3 = pg.BarGraphItem(x=t1.columns+2*bar_width, height=t1.values[2],
width=bar_width, brush='y')
win.addItem(bg1)
win.addItem(bg2)
win.addItem(bg3)
win.setTitle('Car Distribution by Gear and Cylindres ')
win.setLabel('left', "Frequency", )
win.setLabel('bottom', "Number of Gears")

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore,
'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
~~~~~~~~~~~~~

![](figures/32Multiset_Bar_ChartPy_figure4_1.png){width=12 cm}



### References
