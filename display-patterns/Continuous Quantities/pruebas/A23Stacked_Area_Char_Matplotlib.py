import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
from datos import data

d=data('mtcars')
carb=d.cyl
wt= d.mpg
y0 = carb
y1 = wt

fig, ax = plt.subplots()
ax.plot(y0, label='y0')
ax.plot(y1, label='y1')

update = {'data':[{'fill': 'tonexty'}]}
plot_url = py.plot_mpl(fig, update=update, strip_style=True, filename='mpl-stacked-line')
