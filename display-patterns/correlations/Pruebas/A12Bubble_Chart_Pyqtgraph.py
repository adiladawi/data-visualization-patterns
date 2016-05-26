import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from datos import data

d=data('mtcars')
win = pg.GraphicsWindow()
win.resize(800,500)
win.setWindowTitle('Bubble Chart')
plt= win.addPlot(title="Scatterplots by Milles per Gallon and  Car Weigh")
plt.plot(d.wt,d.mpg, pen=None, symbol='o', symbolSize=d.cyl, symbolPen=(255,255,255,200), symbolBrush=(0,0,255,150))
plt.setLabel('left', "Miles per Gallon", units='mpg')
plt.setLabel('bottom', "Car Weight", units='lbs')

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()