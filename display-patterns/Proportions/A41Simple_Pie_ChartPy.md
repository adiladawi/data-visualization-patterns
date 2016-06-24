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
* **Seaborn** is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics (Waskom,2013)[^3].
* **Pyqtgraph**  is a pure-python graphics and GUI library built on PyQt4 / PySide and numpy. It is intended for use in mathematics / scientific / engineering applications (Campagnola, 2014)[^4].


## Code Example


### Matplotlib


~~~~{.python}
import matplotlib.pyplot as plt
from datos import data
import pandas

colors = ['lightcoral', 'lightskyblue','yellowgreen']
d=data('mtcars')
ps = pandas.Series([i for i in d.cyl])
c = ps.value_counts()
plt.pie(c,  labels=c.index, colors=colors, autopct='%1.1f%%',
shadow=True, startangle=0)
plt.axis('equal')
plt.title('Car Distribution by Cylindres', size=18)
plt.show()
~~~~~~~~~~~~~

![](figures/A41Simple_Pie_ChartPy_figure3_1.png)


The complete online documentation is also available at [matplotlib](http://matplotlib.org/contents.html).


### Seaborn


~~~~{.python}
import matplotlib.pyplot as plt
import seaborn as sns
from datos import data
import pandas

sns.set(style="white")
d=data('mtcars')
colors = sns.husl_palette(3)
d=data('mtcars')
ps = pandas.Series([i for i in d.cyl])
c = ps.value_counts()
plt.pie(c,  labels=c.index, colors=colors, autopct='%1.1f%%',
shadow=True, startangle=0)
plt.title('Car Distribution by Cylindres', size=18)
plt.show()
~~~~~~~~~~~~~

![](figures/A41Simple_Pie_ChartPy_figure4_1.png)


The online documentation is available in [Seaborn](https://stanford.edu/~mwaskom/software/seaborn/api.html).


### Pyqtgraph


~~~~{.python}
import pyqtgraph as pg
from  PyQt4  import  QtGui
from datos import data
import numpy

win = pg.GraphicsWindow("Car Distribution by Cylindres")
view = win.addViewBox()
view.setAspectLocked()
d=data('mtcars')
t1 = d.pivot_table( values = 'carb',index=['gear'], columns = ['cyl'],
aggfunc = len)
colours = [QtGui.QColor('springgreen'), QtGui.QColor('lightskyblue'),
QtGui.QColor('lightcoral')]
r=[0,0,0]
r[0]= sum(t1[4])/len(d)
r[1]=sum(t1[6]) /len (d)
x=t1[8]
x = x[~numpy.isnan(x)]
r[2]= sum(x) / len(d)
count1=0
labels=['','','']
labels[0]='4 Cyl \n'+str(r[0]*100)+ '%'
labels[1]='6 Cyl \n'+str(r[1]*100) + '%'
labels[2]='8 Cyl \n'+str(r[2]*100) +'%'
position=[ (-1,6), (-5,4), (-5,10)]
set_angle = 0

for x in r:
    angle = x*360*16
    ellipse = QtGui.QGraphicsEllipseItem(0,0,100,100)
    ellipse.setPos(0,0)
    ellipse.setStartAngle(set_angle)
    ellipse.setSpanAngle(angle)
    ellipse.setBrush(colours[count1])
    set_angle = set_angle + angle
    ellipse.setPen(pg.mkPen(5))
    view.addItem(ellipse)
    count1 +=1

j=0
for x in position:
    text = pg.TextItem(labels[j], anchor=(position[j]), color=(0,0,0))
    view.addItem(text)
    j+=1

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore,
'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
~~~~~~~~~~~~~

![](figures/A41Simple_Pie_ChartPy_figure5_1.png)


The complete online documentation is also available at [Pyqtrgaph](http://www.pyqtgraph.org/documentation/).


### References

[^1]: Gautier, Laurent (2016). rpy2. Consultado el 01 de Febrero, 2016 en http://rpy2.bitbucket.org/
[^2]: Hunter, John (2016). matplotlib. Consultado el 03 de Febrero, 2016 en http://matplotlib.org/
[^3]: Waskom, Michael (2016). Seaborn. Consultado el 08 de Febrero, 2016 en https://stanford.edu/~mwaskom/software/seaborn/index.htmltest/
[^4]: Campagnola, Luke (2014). Pyqtgraph. Consultado el 10 de Febrero, 2016 http://www.pyqtgraph.org/
