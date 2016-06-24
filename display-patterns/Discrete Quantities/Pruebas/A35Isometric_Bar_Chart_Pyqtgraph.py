from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
from datos import data

d=data('mtcars')
t1 = d.pivot_table( values = 'carb',index=['cyl'], columns = ['gear'], aggfunc = len)
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
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
