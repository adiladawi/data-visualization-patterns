import pyqtgraph as pg
from  PyQt4  import  QtGui
from datos import data
import numpy

win = pg.GraphicsWindow("Car Distribution by Cylindres")
view = win.addViewBox()
view.setAspectLocked()
d=data('mtcars')
t1 = d.pivot_table( values = 'carb',index=['gear'], columns = ['cyl'], aggfunc = len)
colours = [QtGui.QColor('springgreen'), QtGui.QColor('lightskyblue'), QtGui.QColor('lightcoral')]
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
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()