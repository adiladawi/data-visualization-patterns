import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.collections import PatchCollection
from datos import data

fig = plt.figure()
ax = fig.add_subplot(111, frameon=False)
d=data('mtcars')
subset1= d[d.cyl==6]
patches = []
arrow = mpatches.Arrow(0.492,0.9, 0, -0.1, width=0.05)
patches.append(arrow)
rect=mpatches.Rectangle((0.35, 0.9), 0.3, 0.1)
fig.text(0.415,0.85,"Car Distribution by Cylindres", fontsize='8')
patches.append(rect)
arrow = mpatches.Arrow(0.492,0.7, 0.0, -0.045, width=0.05)
patches.append(arrow)
rect=mpatches.Rectangle((0.35, 0.7), 0.3, 0.1)
fig.text(0.47,0.7,"6 Cylindres", fontsize='8')
patches.append(rect)
x=0.0
x1=0.13
y=0.45
y1=0.49
xx=0.06
for i in subset1.index:        
    arrow = mpatches.Arrow(xx,0.65, 0.0, -0.1, width=0.05)
    patches.append(arrow)   
    if len(i)>12:
        fig.text(x1,y1,i[0:9]+"\n"+i[9:], fontsize='8')
    else:   
        fig.text(x1,y1,str(i), fontsize='8')
    rect=mpatches.Rectangle((x, y),0.125, 0.1)
    patches.append(rect)
    x=x+0.145
    x1=x1+0.113
    xx=xx+0.145

x, y = np.array([[0.06, 0.93], [0.65, 0.65]])
line = mlines.Line2D(x , y , lw=5., alpha=0.3)
ax.add_line(line)
colors=[0,1]
p = PatchCollection(patches,  alpha=0.3)
p.set_array(np.array(colors))
ax.add_collection(p)
plt.title('Tree Diagram ', family='serif', size=16)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
plt.show()