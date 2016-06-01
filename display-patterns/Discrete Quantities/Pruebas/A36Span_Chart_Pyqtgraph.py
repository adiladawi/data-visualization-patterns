from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
from datos import data
import pandas as pd


d=data('mtcars')
subset1, subset2, subset3= d[d.cyl==4], d[d.cyl==6], d[d.cyl==8]
datos=pd.DataFrame ({'Max': [max(subset1.mpg), max(subset2.mpg), max(subset3.mpg)],
			 	 'Min': [min(subset1.mpg), min(subset2.mpg), min(subset3.mpg)],
			 	 'Span': [max(subset1.mpg)-min(subset1.mpg), max(subset2.mpg)-min(subset2.mpg), max(subset3.mpg)-min(subset3.mpg)]})
datos.index=[4,6,8]
bar_width = 0.8
win = pg.plot(title='Simple Bar Chart')
bg1 = pg.BarGraphItem(x=datos.index, height=datos.Max, width=bar_width, brush=(96,255,96), pen='k')
bg2 = pg.BarGraphItem(x=datos.index, height=datos.Min, width=bar_width, brush='k', pen='k' )
win.addItem(bg1)
win.addItem(bg2)
win.setTitle('Range of Milles per Gallon (mpg) by Cylindres (cyl) ')
win.setLabel('left', "Cylindres", )
win.setLabel('bottom', "Milles per Gallon")

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()