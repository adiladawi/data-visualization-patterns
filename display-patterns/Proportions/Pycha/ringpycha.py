import cairo
import sys
import pycha.ring
import numpy as np
from datos import data

d=data('mtcars')
t1 = d.pivot_table( values = 'carb',index=['gear'], columns = ['cyl'], aggfunc = len)
l=[i for i in t1.index]
li=[]
for i in l:
	t=[]
	t.append(str(i)+ ' Gear ')
	for j in t1.loc[i]:
		if(np.isnan(j)):
			j=0
		t.append(j)	
	li.append(tuple(t))

"""
lines = (
    ('3.0 Gear', 1, 2, 12),
    ('4.0 Gear', 8, 4, 0),
    ('5.0 Gear', 2, 1, 2),
) """

def ringChart(output):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 800, 800)

    dataSet = [(line[0], [[0, line[1]], [1, line[2]], [2, line[3]]])
        for line in li]

    options = {
    'colorScheme': {
        'name': 'fixed',
        'args': {
            'colors': ['#66FF66','#FF9999','#ffff00'],
            },
        },
        'axis': {
            'x': {
                'ticks': [dict(v=i, label=d) for i, d in
                    enumerate(['4 Cylindres', '6 Cylindres', '8 Cylindres'])],        
            }
        },
        'legend': {
            'hide': False,
        },
        'title': 'Ring Chart',
    }
    chart = pycha.ring.RingChart(surface, options)
    chart.addDataset(dataSet)
    chart.render()
    surface.write_to_png(output)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        output = sys.argv[1]
    else:
        output = 'ringchart.png'
    ringChart(output)



