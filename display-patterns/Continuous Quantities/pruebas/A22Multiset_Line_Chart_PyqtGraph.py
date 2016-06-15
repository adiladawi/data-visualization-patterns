import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from datos import data

d=data('mtcars')
t=d.carb
s= d.wt

plt = pg.plot()
plt.setWindowTitle('pyqtgraph example: Legend')
plt.addLegend()

c1 = plt.plot(t, pen='r',name='red plot')
c2 = plt.plot(s, pen='g', fillLevel=0, name='green plot')

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
