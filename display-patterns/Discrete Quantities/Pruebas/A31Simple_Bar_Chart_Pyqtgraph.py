import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from datos import data
import pandas

d=data('mtcars')
ps = pandas.Series([i for i in d.gear])
counts = ps.value_counts()

win = pg.plot(title='Simple Bar Chart')
bg1 = pg.BarGraphItem(x=counts.index, height=counts, width=0.6, brush='b')
win.addItem(bg1)
win.setTitle('Simple Bar Chart: Car Distribution')
win.setLabel('left', "Frequency", )
win.setLabel('bottom', "Number of Gears")

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()