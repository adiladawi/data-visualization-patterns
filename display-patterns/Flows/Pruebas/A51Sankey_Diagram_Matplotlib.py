import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey
from matplotlib import pyplot
from datos import data

d=data('mtcars')
mpg=d.loc["Datsun 710",'mpg']
disp=d.loc["Datsun 710",'disp']
qsec=d.loc["Datsun 710",'qsec']
gear =d.loc["Datsun 710",'gear']
cyl=d.loc["Datsun 710",'cyl']
hp=d.loc["Datsun 710",'hp']

fig, ax = plt.subplots(figsize=(15, 15))

Sankey(ax,margin=10, flows=[disp, mpg,-qsec, -gear, -hp,-cyl,],
       labels=['Displacement\n', 'Miles/(US) gallo', '1/4 Mile Time',
            'Number of forward gears', 'Gross horsepower', 'Number of
cylinders'],
       orientations=[-1, 0, 1, 0, 0, 0]).finish()

ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
plt.title("Datsun 710 Sankey Diagram")
plt.show()
