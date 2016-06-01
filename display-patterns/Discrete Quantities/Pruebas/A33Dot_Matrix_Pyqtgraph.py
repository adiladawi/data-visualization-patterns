import pyqtgraph as pg
from  PyQt4  import  QtGui
import pandas
from datos import data

win = pg.GraphicsWindow("Dot Matrix ")
win.resize(300,300)
v = win.addViewBox()
v.setAspectLocked()
text = pg.TextItem("Dot Matrix by Number of Gears ", anchor=(-0.1,22.5), color='w')
v.addItem(text)
d=data('mtcars')
ps = pandas.Series([i for i in d.gear])
counts = ps.value_counts()
position=[ (-0.5,15), (-2,15), (-3.5,15)]
colours = [QtGui.QColor('springgreen'), QtGui.QColor('lightskyblue'), QtGui.QColor('lightcoral')]

x=0.0
y=1.0 
m=0
cols=1

for i in counts:	
	for j in range(i):			
		ellipse = QtGui.QGraphicsEllipseItem(x,y,0.05,0.05)
		ellipse.setBrush(colours[m])		
		v.addItem(ellipse)
		x=x+0.05		
		cols=cols+1
		if (cols>10):
			cols=1
			x=0.0
			y=y-0.05		
	m=m+1

x=0
y=0.7
m=0
for i in counts.index:	
	ellipse = QtGui.QGraphicsEllipseItem(x,y,0.05,0.05)
	ellipse.setBrush(colours[m])
	v.addItem(ellipse)	
	x=x+0.15
	m=m+1
j=0
for x in counts.index:
    text = pg.TextItem(str(int(x))+" gear", anchor=(position[j]), color='w')
    v.addItem(text)
    j+=1 
        
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()