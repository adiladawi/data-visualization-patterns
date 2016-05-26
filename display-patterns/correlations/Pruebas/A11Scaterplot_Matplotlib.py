import numpy as np
import matplotlib.pyplot as plt
from datos import data

d=data('mtcars')
plt.scatter(d.wt,d.mpg,  c='blue')
plt.title('Scatterplot by Milles per Gallon and  Car Weight', family='serif', size=16)
plt.xlabel('Car Weight', family= 'serif')
plt.ylabel('Miles per Gallon', family='serif')
plt.show()