import cairo
import pycha.pie
import pandas
from datos import data

d=data('mtcars')
ps = pandas.Series([i for i in d.cyl])
c1 = ps.value_counts()
i=0
l=[]
while( i <len(c1)):
	l.append((str(c1.index[i])+' Cylindres', c1.values[i]))
	i=i+1

width, height = (500, 400)

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
dataSet = [(line[0], [[0, line[1]]]) for line in l]
options = {
    'colorScheme': {
        'name': 'fixed',
        'args': {
            'colors': ['#FF9999', '#ffff00', '#66FF66'],
            },
        },
        'title': 'Simple Pie Chart',
     }
chart = pycha.pie.PieChart(surface, options)

chart.addDataset(dataSet)
chart.render()

surface.write_to_png('pie.png')
