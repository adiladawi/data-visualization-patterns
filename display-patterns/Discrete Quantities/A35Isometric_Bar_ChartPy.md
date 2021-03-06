# PYTHON IMPLEMENTATION 


## Data Set

For this example it was used Data Set called mtcars (Motor Trend Car Road Tests), which comes by default in R. This data was extracted from the 1974 Motor Trend US magazine, and comprises fuel consumption and 10 aspects of automobile design and performance for 32 automobiles (1973–74 models). 

To use this data set in Python, was used a Python module called rpy2. First create a file named as datos.py and write the next code.


~~~~{.python}
from rpy2.robjects import r
from rpy2.robjects import pandas2ri

def data(name):
        return pandas2ri.ri2py(r[name])
~~~~~~~~~~~~~



Then it is necessary import the datos.py file into the proyect, which you are working.


~~~~{.python}
from datos import data
d=data('mtcars')
~~~~~~~~~~~~~




## Dependences

* **rpy2** Python interface to the R language (Gautier, 2016)[^1]. The rpy2 package is used to access all R datasets from Python.
* **Matplotlib** is a python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. matplotlib can be used in python scripts, the python and ipython shell, web application servers, and six graphical user interface toolkits (Hunter, 2016)[^2].
* **Pyqtgraph**  is a pure-python graphics and GUI library built on PyQt4 / PySide and numpy. It is intended for use in mathematics / scientific / engineering applications (Campagnola, 2014)[^3]


## Code Example


### Matplotlib


~~~~{.python}
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from datos import data

d=data('mtcars')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d',  xlabel='Cylindres' ,
ylabel='Gears', zlabel='Frequency', title='Car Distribution by Gear
and Cylindres')
t1 = d.pivot_table( values = 'carb',index=['cyl'], columns = ['gear'],
aggfunc = len)
x,y =t1.index, t1.columns
xpos, ypos = np.meshgrid(x , y )
elements = len(x) * len(y)
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros(elements)
dx= np.ones_like(zpos)
dy=0.4 *np.ones_like(zpos)
dz=t1.values.flatten()
dz[np.isnan(dz)] = 0
c=['salmon','aqua','lightpink',
'salmon','aqua','lightpink','salmon','aqua','lightpink']
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=c, zsort='average')
plt.show()
~~~~~~~~~~~~~

![](figures/A35Isometric_Bar_ChartPy_figure3_1.png)


The complete online documentation is also available at [matplotlib](http://matplotlib.org/contents.html).



### Pyqtgraph


~~~~{.python}
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
from datos import data

d=data('mtcars')
t1 = d.pivot_table( values = 'carb',index=['cyl'], columns = ['gear'],
aggfunc = len)
dz=t1.values.flatten()
dz[np.isnan(dz)] = 0
m= np.array(dz).reshape((3, 3))
app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 20
w.show()
w.setWindowTitle('Car Distribution by Gear and Cylindres')

gx = gl.GLGridItem()
gx.rotate(90, 0, 1, 0)
gx.translate(-10, 0, 10)
w.addItem(gx)
gy = gl.GLGridItem()
gy.rotate(90, 1, 0, 0)
gy.translate(0, -10, 10)
w.addItem(gy)
gz = gl.GLGridItem()
gz.translate(0, 0, 0)
w.addItem(gz)

pos = np.mgrid[0:3, 0:3, 0:1].reshape(3,3,3).transpose(1,2,0)
size = np.empty((3,3,3))
size[...,0:2] = 0.5
size[...,2] = m
bg = gl.GLBarGraphItem(pos, size)
w.addItem(bg)


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore,
'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
~~~~~~~~~~~~~

![](figures/A35Isometric_Bar_ChartPy_figure4_1.png)


The complete online documentation is also available at [Pyqtrgaph](http://www.pyqtgraph.org/documentation/).


### References

[^1]: Gautier, Laurent (2016). rpy2. Consultado el 01 de Febrero, 2016 en http://rpy2.bitbucket.org/
[^2]: Hunter, John (2016). matplotlib. Consultado el 03 de Febrero, 2016 en http://matplotlib.org/
[^3]: Campagnola, Luke (2014). Pyqtgraph. Consultado el 10 de Febrero, 2016 http://www.pyqtgraph.org/
