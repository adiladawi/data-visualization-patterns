import numpy as np
import matplotlib.pyplot as plt
from datos import data
import pandas as pd

d=data('mtcars')
subset1, subset2, subset3= d[d.cyl==4], d[d.cyl==6], d[d.cyl==8]
x=pd.DataFrame ({'Max': [max(subset1.mpg), max(subset2.mpg), max(subset3.mpg)],
			 	 'Min': [min(subset1.mpg), min(subset2.mpg), min(subset3.mpg)],
			 	 'Span': [max(subset1.mpg)-min(subset1.mpg), max(subset2.mpg)-min(subset2.mpg), max(subset3.mpg)-min(subset3.mpg)]})
x.index=[4,6,8]
bar_width = 0.8
opacity = 0.4
plt.bar(x.index,x.Span, bar_width, alpha=opacity,color='g', bottom=x.Min)
plt.xlabel('Cylindres')
plt.ylabel('Miles per Gallon')
plt.title('Range of Milles per Gallon (mpg) by Cylindres (cyl)', size=15)
plt.show()