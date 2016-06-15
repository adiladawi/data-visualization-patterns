from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
from datos import data
d=data("mtcars")

app = QtGui.QApplication([])
view = pg.GraphicsView()
l = pg.GraphicsLayout(border=(100,100,100))
view.setCentralItem(l)
view.show()
view.setWindowTitle('Simple Line Chart Example')
view.resize(800,600)

p1 = l.addPlot(title="Motor Trend Car Road Tests")
p1.plot(d.am,d.gear)


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
