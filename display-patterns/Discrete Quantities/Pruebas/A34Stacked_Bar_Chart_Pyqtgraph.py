from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import numpy as np
from datos import data
import pandas

d=data('mtcars')
t1 = d.pivot_table( values = 'carb',index=['cyl'], columns = ['gear'], aggfunc = len)
bar_width = 0.25
win = pg.plot(title='Simple Bar Chart')
bg1 = pg.BarGraphItem(x=t1.columns, height=t1.values[2]+t1.values[1]+t1.values[0], width=bar_width, brush='g')
bg2 = pg.BarGraphItem(x=t1.columns, height=t1.values[1]+t1.values[0], width=bar_width, brush='r')
bg3 = pg.BarGraphItem(x=t1.columns, height=t1.values[0], width=bar_width, brush='y')
win.addItem(bg1)
win.addItem(bg2)
win.addItem(bg3)
win.setTitle('Car Distribution by Gear and Cylindres ')
win.setLabel('left', "Frequency", )
win.setLabel('bottom', "Number of Gears")

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()