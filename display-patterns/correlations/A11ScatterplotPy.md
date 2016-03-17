# PYTHON IMPLEMENTATION

## Data Set

## Dependences
* rpy2:  The rpy2 package is used to access all R datasets from Python.
* Matplotlib
* Seaborn
* Vispy
* Pyqtgraph


## Code Example

### Matplotlib


~~~~{.python}
import numpy as np
import matplotlib.pyplot as plt
from datos import data
d=data('mtcars')
plt.scatter(d.wt,d.mpg,  c='blue')
plt.title('Scatterplot by Milles per Gallon and  Car Weight',
family='serif', size=16)
plt.xlabel('Car Weight', family= 'serif')
plt.ylabel('Miles per Gallon', family='serif')
plt.show()
~~~~~~~~~~~~~

![](figures/scatterplot_figure1_1.png){width=12 cm}


### Seaborn


~~~~{.python}
import matplotlib.pyplot as plt
import seaborn as sns
from datos import data

d=data('mtcars')
sns.set(style="white")
g = sns.FacetGrid(d)
g.map(plt.scatter, "wt", "mpg")
plt.title("Scatterplot by Milles per Gallon and  Car Weight",
family='serif', size=16)
g.set_axis_labels("Car Weight","Milles per Gallon")
plt.show()
~~~~~~~~~~~~~

![](figures/scatterplot_figure2_1.png){width=12 cm}



### Pyqtgraph


~~~~{.python}
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from datos import data

d=data('mtcars')
win = pg.GraphicsWindow()
win.resize(800,500)
win.setWindowTitle('pyqtgraph example: Scatterplot')
plt= win.addPlot(title="Scatterplots by Milles per Gallon and  Car
Weigh")
plt.plot(d.wt,d.mpg, pen=None, symbol='o', symbolSize=5,
symbolPen=(255,255,255,200), symbolBrush=(0,0,255,150))
plt.setLabel('left', "Miles per Gallon", units='mpg')
plt.setLabel('bottom', "Car Weight", units='lbs')

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore,
'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
~~~~~~~~~~~~~
![](figures/scatterplot_figure3_1.png){width=12 cm}


## References
